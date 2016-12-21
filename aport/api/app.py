from flask import Flask

from aport.api.api import AportApi
from aport.cache.cache import MemoryCache, RedisCache


class AportApp(Flask):

    def __init__(self, test=False):
        super(AportApp, self).__init__('aport')
        if test:
            self.cache = MemoryCache()
        else:
            self.cache = RedisCache()
        self.api = AportApi(self, self.cache)
        self.debug = True
