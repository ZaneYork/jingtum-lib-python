# coding=gbk
"""
 * User: ������
 * Date: 2018/5/21
 * Time: 11:25
 * Description: ����ģ��
"""
import unittest

#from src.logger import logger
from src.remote import Remote

class RemoteTest(unittest.TestCase):
    def test_create_pay_object(self):
        remote = Remote()
        if not isinstance(remote.connect(None), Exception):
            tx = remote.buildPaymentTx({
                'account': 'j9fE48ebcvwnKSGnPdtN6jGNM9yVBMVaH8',
                'to': 'jEmEWuLQXgtBaro86hScnBpjN3TgKSoQGD',
                'amount': {
                    "value": 0.5,
                    "currency": "SWT",
                    "issuer": ""
                }
            })
            tx.setSecret('ssTkYQLLYiZs7Sosp12sB43TocUbd')
            tx.addMemo('��jDUjqoDZLhzx4DCf6pvSivjkjgtRESY62c֧��0.5swt.')  # ��ѡ
            tx.addMemo('123')
            s=tx.submit()
            print('result is', s)

if __name__ == '__main__':
    unittest.main()
