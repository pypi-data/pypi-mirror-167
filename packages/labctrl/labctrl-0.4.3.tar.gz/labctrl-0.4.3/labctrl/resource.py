""" """

import importlib.util
import inspect
from pathlib import Path
import pkgutil
from typing import Any

from labctrl.logger import logger
from labctrl import Settings


class ResourceMetaclass(type):
    """ """

    def __init__(cls, name, bases, kwds) -> None:
        """ """
        super().__init__(name, bases, kwds)

        # find the parameters (gettable and settable) of the Resource class
        mro = inspect.getmro(cls)  # mro means method resolution order
        properties = {
            k: v for c in mro for k, v in c.__dict__.items() if isinstance(v, property)
        }
        del properties["parameters"]
        cls.properties = properties.keys()
        cls.gettables = {k for k, v in properties.items() if v.fget is not None}
        cls.settables = {k for k, v in properties.items() if v.fset is not None}

    def __repr__(cls) -> str:
        """ """
        return f"<class '{cls.__name__}'>"


class Resource(metaclass=ResourceMetaclass):
    """ """

    def __init__(self, name: str, **parameters) -> None:
        """ """
        self._name = str(name)
        logger.debug(f"Initialized {self}.")
        if parameters:  # set parameters with values supplied by the user, if available
            self.configure(**parameters)

    def __repr__(self) -> str:
        """ """
        return f"{self.__class__.__name__} '{self._name}'"

    @property
    def name(self) -> str:
        """ """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """ """
        self._name = str(value)

    def _attributes(self) -> set[str]:
        """ """
        return {k for k in self.__dict__.keys() if not k.startswith("_")}

    @property
    def parameters(self) -> set[str]:
        """ """
        return self.__class__.properties | self._attributes()

    def configure(self, **parameters) -> None:
        """ """
        settables = self._attributes() | self.__class__.settables
        for name, value in parameters.items():
            if name in settables:
                setattr(self, name, value)

    def snapshot(self) -> dict[str, Any]:
        """ """
        gettables = self._attributes() | self.__class__.gettables
        return {name: getattr(self, name) for name in sorted(gettables)}


def _locate(source: Path) -> set[Resource]:
    """ "source" is a folder containing modules that contain all instantiable user-defined Resource subclasses. We find all resource classes defined in all modules in all subfolders of the source folder THAT ARE DESIGNATED PYTHON PACKAGES i.e. the folder has an __init__.py file. We return a set of resource classes.

    source must be Path object, strings will throw a TypeError
    """
    resources = set()
    for modfinder, modname, is_pkg in pkgutil.iter_modules([source]):
        if not is_pkg and modname != "labctrl":
            # we have found a module other than labctrl, find Resources defined in it
            modspec = modfinder.find_spec(modname)
            module = importlib.util.module_from_spec(modspec)
            modspec.loader.exec_module(module)  # for module namespace to be populated
            classes = inspect.getmembers(module, inspect.isclass)
            resources |= {cls for _, cls in classes if issubclass(cls, Resource)}
        else:  # we have found a subpackage, let's send it recursively to locate()
            resources |= _locate(source / modname)
    return resources


def locate_resources() -> set[Resource]:
    """ """
    resourcepath_setting = Settings().resourcepath
    try:
        resourcepath = Path(resourcepath_setting)
        return _locate(resourcepath)
    except (TypeError, AttributeError):
        logger.warning(
            f"No/invalid resourcepath '{resourcepath_setting}' found in labctrl "
            "settings. Please specify a valid resourcepath if you want to use labctrl "
            "to load/save Resources from/to yml config files."
        )
    except RecursionError:
        message = (
            "Failed to locate and register Resource classes. Place all Resource "
            "classes in a different folder than that of the script you are "
            "executing to use these Resources."
        )
        raise RuntimeError(message)
