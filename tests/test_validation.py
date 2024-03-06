from webtest import TestApp
import tg
from tg import TGController, expose, validate, FullStackApplicationConfigurator
from tg.controllers.util import validation_errors_response

from formencode import validators


class RootController(TGController):
    @expose()
    @validate({'param': validators.Int()},
              error_handler=validation_errors_response)
    def formencode_dict_validation(self, **kwargs):
        return 'NO_ERROR'


class TestFormencodeValidation:
    def setup_method(self):
        configurator = FullStackApplicationConfigurator()
        configurator.update_blueprint({
            'root_controller': RootController()
        })
        self.app = TestApp(configurator.make_wsgi_app())

    def test_formencode_dict_validation(self):
        resp = self.app.post('/formencode_dict_validation', {'param': "7"})
        assert 'NO_ERROR' in str(resp.body), resp

        resp = self.app.post('/formencode_dict_validation', {'param': "hello"}, status=412)
        assert 'Please enter an integer value' in str(resp.body), resp

