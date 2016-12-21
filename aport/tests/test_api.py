import json
import unittest

from aport.api.app import AportApp


class AportApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = AportApp().test_client()

    def test_api_just_call_methods(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)

        response = self.app.post('/')
        self.assertEqual(response.status_code, 404)

        key = 'test_key'
        value = '1'
        response = self.app.put('/{}/'.format(key), data={'value': value})
        self.assertEqual(response.status_code, 201)
        content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(content['key'], key)
        self.assertEqual(content['value'], value)

        response = self.app.get('/{}/'.format(key))
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(content['key'], key)
        self.assertEqual(content['value'], value)

        key = 'test_key'
        value = '2'
        response = self.app.put('/{}/'.format(key), data={'value': value})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(content['key'], key)
        self.assertEqual(content['value'], value)

        response = self.app.get('/{}/'.format(key))
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.data.decode('utf-8'))
        self.assertEqual(content['key'], key)
        self.assertEqual(content['value'], value)

        response = self.app.delete('/{}/'.format(key))
        self.assertEqual(response.status_code, 204)

        response = self.app.get('/{}/'.format(key))
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
