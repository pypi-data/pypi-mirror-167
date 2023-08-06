import traceback

from .container import Container
from .container import Log
from .container import Setting
from .application.tools import pprint

from wsgiref.simple_server import make_server


class Fast:
    def __init__(self, setting_path: str = None, setting_data: dict = None):
        self.setting = Setting(setting_path, setting_data)
        self._container = Container()
        self._server = None
        self._log = Log()

    def set_setting(self, setting_path: str = None, setting_data: dict = None):
        self.setting.init(setting_path, setting_data)

    def start(self, constructor=None):
        self.__init(constructor)

        self._server.serve_forever()

    def __init(self, constructor):
        # 初始化容器
        self._container.init(self.setting)
        # 初始化服务器
        if constructor is None:
            self._server = make_server(self.setting.server_host, self.setting.server_post, self)
        elif type(constructor) == type(make_server):
            try:
                self._server = constructor(self.setting.server_host, self.setting.server_post, self)
            except TypeError:
                traceback.print_exc()
                pprint("An exception occurred while your constructor was executing", color='red')
                pprint("Now we will use the default constructor to ensure that the program continues to execute", 'red')
                self._server = make_server(self.setting.server_host, self.setting.server_post, self)
        else:
            pprint("The type of the constructor you provide is {}".format(type(constructor)), 'red')
            pprint(",but wo need {}".format(type(make_server)), 'red')
            pprint("Now we will use the default constructor to ensure that the program continues to execute", 'red')
            self._server = make_server(self.setting.server_host, self.setting.server_post, self)
        print('serve on %s:%d' % (self.setting.server_host, self.setting.server_post))

    def wsgi_app(self, environ, start_response):
        response = self._container.dispatch(environ)
        start_response(response.status, response.response_headers())
        return response.response_data()

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)
