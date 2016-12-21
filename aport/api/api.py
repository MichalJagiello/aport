from flask_restful import abort, Api, Resource, fields, marshal_with, reqparse

from aport.exceptions import CacheKeyNotExistError


class KeyValueResource(Resource):

    marshal = {
        'key': fields.String,
        'value': fields.String,
    }

    def __init__(self, cache):
        self.cache = cache
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('value')

    @staticmethod
    def abort_does_not_exist():
        abort(404, message="Given key does not exist")

    @marshal_with(marshal)
    def get(self, key):
        try:
            cache_data = self.cache.get(key)
            return cache_data
        except CacheKeyNotExistError:
            self.abort_does_not_exist()

    @marshal_with(marshal)
    def put(self, key):
        args = self.parser.parse_args()
        value = args.get('value')
        if self.cache.exists(key):
            return_code = 200
        else:
            return_code = 201
        self.cache.set(key, value)
        cache_data = self.cache.get(key)
        return cache_data, return_code

    def delete(self, key):
        if self.cache.exists(key):
            self.cache.delete(key)
            return '', 204
        else:
            self.abort_does_not_exist()


class AportApi(Api):
    """
    Aport API class
    """

    def __init__(self, app, cache=None):
        super().__init__(app)
        self.cache = cache
        self.add_resource(KeyValueResource,
                          '/<string:key>/',
                          resource_class_args=(self.cache,))
