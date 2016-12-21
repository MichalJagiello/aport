from flask import Flask

from aport.api.api import AportApi
from aport.cache.cache import MemoryCache


class AportApp(Flask):

    def __init__(self):
        super(AportApp, self).__init__('aport')
        self.cache = MemoryCache()
        self.api = AportApi(self, self.cache)
        self.debug = True
