import unittest
import json

from iplocate.iplocate import locateip, myip
from mock import patch


class IPLocateTests(unittest.TestCase):

    def setUp(self):
        self.urlopen_patcher = patch("iplocate.iplocate.urlopen")
        self._urlopen = self.urlopen_patcher.start()
        self.ip_data = {u'loc': u'1.000,101.000',
                                u'city': u'Kuala Lumpur',
                                u'country': u'MY',
                                u'region': u'Kuala Lumpur',
                                u'hostname': u'sdg-24-164.tm.net.my',
                                u'ip': u'127.0.0.1',
                                u'org': u'Internet Service Provider',
                                u'postal': u'58200'}

    def tearDown(self):
        self.urlopen_patcher.stop()

    def test_locateip(self):
        self._urlopen.return_value.read.return_value = '{"id": "hulahoop"}'
        result = locateip("http://ww.google.com")
        self.assertEqual(result, {u'id': u'hulahoop'})

    def test_myip(self):
        self._urlopen.return_value.read.return_value = json.dumps(self.ip_data)
        result = myip()
        self.assertEqual(result, self.ip_data)

if __name__ == '__main__':
    unittest.main()
