# # coding=gbk
#
"""
 * Created with PyCharm.
 * User: ��ʫ��
 * Date: 2018/6/15
 * Time: 0:27
 * Description:
"""
import unittest

from src.logger import logger
from src.remote import Remote

class RemoteTest(unittest.TestCase):
    def test_requestOrderBook(self):
        remote = Remote(local_sign=True)
        if not isinstance(remote.connect(None), Exception):
            req = remote.request_order_book({'gets': {'currency': 'SWT', 'issuer': '777'},
                  'pays': {'currency': 'CNY', 'issuer': 'jBciDE8Q3uJjf111VeiUNM775AMKHEbBLS'}})
            temp = req.submit()
            result = remote.parse_orderbook_info(temp)
            logger.info(result)

if __name__ == '__main__':
    unittest.main()

