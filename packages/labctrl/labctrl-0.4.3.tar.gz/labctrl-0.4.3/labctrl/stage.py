"""
This module contains utilities for staging Resources prior to running experiments.

Resouces can be loaded from .yml config files and can be added and removed on demand.
Only those Resource classes found in Settings().resourcepath can be staged.
The Stage can link up to the Server to retrieve remotely served Resources.
"""

from __future__ import annotations

from pathlib import Path
from tkinter import FALSE

import Pyro5.api as pyro

from labctrl.instrument import Instrument
from labctrl.logger import logger
from labctrl.resource import Resource, locate_resources
from labctrl.settings import Settings
import labctrl.server as server
import labctrl.yamlizer as yml


class StageError(Exception):
    """ """


class Stage:
    """ """

    def __init__(self, name: str, *sources: Path | Resource, remote: bool) -> None:
        """ """
        logger.debug(f"Setting up a Stage with {name = }...")
        self._name: str = str(name)

        configfolder = Path(Settings().configpath)
        configfolder.mkdir(exist_ok=True)
        self._configpath: Path = configfolder / f"{self._name}.yml"
        self._configpath.touch(exist_ok=True)
        # _config is a dict with key: configpath, value: list[Resource] used for saving
        self._config: dict[Path, list[Resource]] = {self._configpath: []}

        # _resources is a list of Resource or resource proxy objects
        self._resources: list[Resource | pyro.Proxy] = []
        resource_classes = locate_resources()
        for resource_class in resource_classes:
            yml.register(resource_class)
        if sources:
            self.add(*sources)

        self._server, self._proxies = None, []  # will be updated by _link()
        if remote:
            self.link()

        logger.debug(f"Setup Stage '{name}' with config saved at '{self._configpath}'.")

    @property
    def name(self) -> str:
        """ """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """ """
        self._name = str(value)

    def link(self) -> None:
        """ """
        self._server, self._proxies = server.link()
        for resource_proxy in self._proxies:
            name = resource_proxy.name
            self._resources.append(resource_proxy)
            logger.debug(f"Staged remote Resource with {name = }.")

    def __enter__(self) -> Stage:
        """ """
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        """ """
        self.teardown()

    def teardown(self) -> None:
        """ """
        self.save()
        for resource in self._resources:
            if isinstance(resource, Instrument) and resource.status:
                resource.disconnect()

        if self._server is not None:
            server.unlink(self._server, *self._proxies)

        logger.debug("Tore down the Stage gracefully!")

    def save(self) -> None:
        """ """
        logger.debug(f"Saving the state of staged resources to their configs...")
        for configpath, resources in self._config.items():
            yml.dump(configpath, *resources)

    @property
    def resources(self) -> list[Resource]:
        """ """
        return self._resources.copy()

    def add(self, *sources: Path | Resource, configpath: Path = None) -> None:
        """ """
        for source in sources:
            if isinstance(source, Resource):  # 'source' is a Resource object
                yml.register(source.__class__)  # necessary for yaml representer to work
                self._add_resource(source, configpath=configpath)
            else:  # 'source' is a path to a yml config file containing Resource objects
                self._add_resource_from_config(source)

    def _add_resource_from_config(self, configpath: Path) -> None:
        """ """
        resources = yml.load(configpath)
        try:
            self.add(*resources, configpath=configpath)
        except TypeError:
            message = f"A list of resources must be specified in {configpath = }."
            raise StageError(message) from None
        else:
            if str(configpath) != str(self._configpath):
                self._config[self._configpath].append(str(configpath))

    def _add_resource(self, resource: Resource, configpath: Path) -> None:
        """ """
        self._resources.append(resource)
        configpath = self._configpath if configpath is None else configpath
        if configpath in self._config:
            self._config[configpath].append(resource)
        else:
            self._config[configpath] = [resource]
        logger.debug(f"Staged {resource = }.")

    def remove(self, resource: Resource) -> None:
        """ """
        try:
            self._resources.remove(resource)
        except ValueError:
            logger.warning(f"Can't remove {resource = } as it does not exist on stage.")
        else:
            if resource in self._proxies:  # resource is a Proxy object
                server.release(resource)
            else:
                for config in self._config.values():  # don't save Resource to yml
                    config.remove(resource)

            logger.debug(f"Unstaged {resource = }.")

    def clear(self) -> None:
        """ """
        self._resources = []
        self._config = {self._configpath: []}

    def get(self, *names: str) -> list[Resource]:
        """ """
        resources = [resource for resource in self._resources if resource.name in names]
        logger.info(f"Retrieved {len(resources)} resources from stage.")
        return resources        
