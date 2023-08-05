""" Control global settings for labctrl """

from __future__ import annotations

from pathlib import Path
import warnings

import yaml

SETTINGSPATH = Path.home() / ".labctrl/settings.yml"


class Settings:
    """
    Context manager for labctrl global settings
    How to use:
        with Settings() as settings:
            print(settings)  # to get all labctrl settings that a user can specify
            settings.<setting1> = <value1>  # set 'setting1' to 'value1'
            settings.<setting2> = <value2>  # set 'setting2' to 'value2'
            print(settings.settings)  # get latest values of all settings
    Any unrecognized settings will be ignored
    """

    configpath: str = str(SETTINGSPATH.parent / "config")
    logspath: str = str(SETTINGSPATH.parent / "logs")
    resourcepath: str = None

    def __init__(self) -> None:
        """ """
        with SETTINGSPATH.open() as config:
            self._settings = yaml.safe_load(config)

        self._settings_keys = tuple(Settings.__annotations__.keys())
        for key in self._settings_keys:
            if key not in self._settings or self._settings[key] is None:
                message = f"Labctrl setting '{key}' not found, please set it now."
                warnings.warn(message, stacklevel=2)
            else:
                setattr(self, key, self._settings[key])

    def __repr__(self) -> None:
        """ """
        return f"{self.__class__.__name__}({self._settings_keys})"

    @classmethod
    def make_default(cls) -> None:
        """ """
        SETTINGSPATH.parent.mkdir(exist_ok=True)
        SETTINGSPATH.touch(exist_ok=True)
        settings = {key: getattr(cls, key) for key in cls.__annotations__.keys()}
        with open(SETTINGSPATH, "r+") as config:
            yaml.safe_dump(settings, config)

    def __enter__(self) -> Settings:
        """ """
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        """ """
        self.save()

    @property
    def settings(self) -> dict[str, str]:
        """ """
        return {setting: getattr(self, setting) for setting in self._settings_keys}

    def save(self) -> None:
        """ """
        settings = self.settings

        with open(SETTINGSPATH, "w+") as config:
            try:
                yaml.safe_dump(settings, config)
            except yaml.YAMLError:
                Settings.make_default()
                message = "Failed to save labctrl settings, saved default settings."
                warnings.warn(message, stacklevel=2)


if not SETTINGSPATH.exists():
    Settings.make_default()
