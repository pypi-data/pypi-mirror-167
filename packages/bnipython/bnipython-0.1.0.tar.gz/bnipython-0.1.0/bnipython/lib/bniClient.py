from bnipython.lib.net.httpClient import HttpClient
from bnipython.lib.util import constants


class BNIClient:
    def __init__(self, options={'prod': False, 'appName': '', 'clientId': '', 'clientSecret': '', 'apiKey': '', 'apiSecret': ''}):
        self.config = options
        self.httpClient = HttpClient()

    def getConfig(self):
        return self.config

    def getBaseUrl(self):
        if self.config['prod']:
            return constants.PRODUCTION_BASE_URL
        else:
            return constants.SANDBOX_BASE_URL

    def getToken(self):
        token = self.httpClient.tokenRequest({
            'url': self.getBaseUrl(),
            'path': '/api/oauth/token',
            'username': self.config['clientId'],
            'password': self.config['clientSecret']
        })
        return token['access_token']
