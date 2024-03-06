# -*- coding: utf-8 -*-
from tg.configuration.utils import TGConfigError
from tg.configurator.base import (ConfigurationComponent,
                                  BeforeConfigConfigurationAction,
                                  ConfigReadyConfigurationAction,
                                  AppReadyConfigurationAction)


class FormencodeConfigurationComponent(ConfigurationComponent):
    """Support for Formencode validation"""
    id = 'formencode'

    def get_defaults(self):
        return {
        }

    def get_coercion(self):
        return {
        }

    def get_actions(self):
        return (
            BeforeConfigConfigurationAction(self._configure),
            ConfigReadyConfigurationAction(self._setup_validation),
            AppReadyConfigurationAction(self._add_middleware),
        )

    def _configure(self, conf, app):
        pass

    def _setup_validation(self, conf, app):
        pass

    def _add_middleware(self, conf, app):
        pass
