try:
    from xmlrpclib import ServerProxy, Error
except ImportError:
    from xmlrpc.client import ServerProxy, Error


class BaseService:
    xmlrpc_url = 'https://api.infusionsoft.com/crm/xmlrpc/v1'
    _service = None
    client = None

    def __init__(self, keap):
        self.keap = keap
        self.get_xmlrpc_client()

    @property
    def token(self):
        return self.keap.token

    def get_xmlrpc_client(self):
        uri = f"{self.xmlrpc_url}?access_token={self.token.access_token}"
        self.client = ServerProxy(uri, use_datetime=self.use_datetime, allow_none=True)
        self.client.error = Error
        return self.client

    def __getattr__(self, method):
        def function(*args):
            return self.call(method, *args)

        return function

    @property
    def service(self):
        return self._service if self._service else self.__class__.__name__

    def call(self, method, *args):
        call = getattr(self.client, f"{self.service}.{method}")
        try:
            return call(self.token.access_token, *args)
        except self.client.error as v:
            return "ERROR", v

    def server(self):
        return self.client
