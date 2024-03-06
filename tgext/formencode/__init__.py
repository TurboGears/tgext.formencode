from .decorators import variable_decode


def plugme(app_config, options=None):
    from .component import ToscaWidgets2ConfigurationComponent
    app_config.register(ToscaWidgets2ConfigurationComponent, after='caching')
    return dict(appid='tgext.tw2')

