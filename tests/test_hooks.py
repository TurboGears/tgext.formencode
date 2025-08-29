import pytest
import gettext

import tg
from tg import TGController
from tg import FullStackApplicationConfigurator
from tg.util.webtest import test_context
import tgext.formencode


class RootController(TGController):
    pass


def test_set_request_lang_sets_formencode_translation():
    """Hook should set a FormEncode translation for the request.

    TurboGears hooks don't pass request locals; the handler must
    retrieve them from tg.request_local.context. After firing the
    hook, ensure translation is not NullTranslations and language
    metadata corresponds to requested locale.
    """
    configurator = FullStackApplicationConfigurator()
    configurator.update_blueprint({
        'root_controller': RootController()
    })
    tgext.formencode.plugme(configurator)
    configurator.make_wsgi_app()

    with test_context(app=None):
        tg.hooks.notify('set_request_lang', ['pt_BR'])

        # Access the request-local TG context explicitly
        tgl = tg.request_local.context
        trans = getattr(tgl.translator, '_formencode_translation', None)

        assert trans is not None, "FormEncode translation not set on translator"
        assert isinstance(trans, gettext.GNUTranslations), (
            f"Expected GNUTranslations, got {type(trans)}"
        )

        # Sanity check: a well-known message should be translated in pt_BR
        sample = 'Please enter an integer value'
        assert trans.gettext(sample) != sample
