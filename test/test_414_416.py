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
        remote = Remote(local_sign=True)
        if not isinstance(remote.connect(None), Exception):
            options =  {
                'account': 'j9fE48ebcvwnKSGnPdtN6jGNM9yVBMVaH8',
                'to': 'jEmEWuLQXgtBaro86hScnBpjN3TgKSoQGD',
                'amount': {
                    "value": 0.01,
                    "currency": "SWT",
                    "issuer": ""
                }
            }
            tx = remote.build_payment_tx(options)
            tx.set_secret('ssTkYQLLYiZs7Sosp12sB43TocUbd')
            #tx.add_memo('��jDUjqoDZLhzx4DCf6pvSivjkjgtRESY62c֧��0.5swt.')  # ��ѡ
            #tx.add_memo('��')  # ��ѡ
            s=tx.submit()
            result=remote.parse_payment(s)
            print('test_create_pay_object result is', result)

    def test_set_relation(self):
        remote = Remote()
        options_trust = {
                'type': 'trust',
                'account': 'j9fE48ebcvwnKSGnPdtN6jGNM9yVBMVaH8',
                'target': 'jEmEWuLQXgtBaro86hScnBpjN3TgKSoQGD',
                'limit': {
                    "value": "0.5",
                    "currency": "CCA",
                    "issuer": "js7M6x28mYDiZVJJtfJ84ydrv2PthY9W9u"
                }
        }
        options_authorize = {
                'type': 'authorize',
                'account': 'j9fE48ebcvwnKSGnPdtN6jGNM9yVBMVaH8',
                'target': 'jEmEWuLQXgtBaro86hScnBpjN3TgKSoQGD',
                'limit': {
                    "value": "0.5",
                    "currency": "CCA",
                    "issuer": "js7M6x28mYDiZVJJtfJ84ydrv2PthY9W9u"
                }
        }
        options_freeze = {
            'type': 'freeze',
            'account': 'j9fE48ebcvwnKSGnPdtN6jGNM9yVBMVaH8',
            'target': 'jEmEWuLQXgtBaro86hScnBpjN3TgKSoQGD',
            'limit': {
                "value": "0.5",
                "currency": "CCA",
                "issuer": "js7M6x28mYDiZVJJtfJ84ydrv2PthY9W9u"
            }
        }
        if not isinstance(remote.connect(None), Exception):
            tx = remote.build_relation_tx(options_trust)
            tx.set_secret('ssTkYQLLYiZs7Sosp12sB43TocUbd')
            s=tx.submit()
            result=remote.parse_payment(s)
            print('trust result is', result)

            tx = remote.build_relation_tx(options_authorize)
            tx.set_secret('ssTkYQLLYiZs7Sosp12sB43TocUbd')
            s=tx.submit()
            result=remote.parse_payment(s)
            print('authorize result is', result)

            tx = remote.build_relation_tx(options_freeze)
            tx.set_secret('ssTkYQLLYiZs7Sosp12sB43TocUbd')
            s=tx.submit()
            result=remote.parse_payment(s)
            print('freeze result is', result)

    def test_buildaccount(self):
        remote = Remote()
        options_property = {
                'type': 'property',
                'account': 'j9fE48ebcvwnKSGnPdtN6jGNM9yVBMVaH8',
                'set_flag': '123'
        }
        options_delegate = {
                'type': 'delegate',
                'account': 'j9fE48ebcvwnKSGnPdtN6jGNM9yVBMVaH8',
                'delegate_key': 'jEmEWuLQXgtBaro86hScnBpjN3TgKSoQGD',
                'set_flag': '123'
        }
        if not isinstance(remote.connect(None), Exception):
            tx = remote.build_account_set_tx(options_property)
            tx.set_secret('ssTkYQLLYiZs7Sosp12sB43TocUbd')
            s=tx.submit()
            result=remote.parse_payment(s)
            print('buildAccountSetTx property result is', result)

            tx = remote.build_account_set_tx(options_delegate)
            tx.set_secret('ssTkYQLLYiZs7Sosp12sB43TocUbd')
            s=tx.submit()
            result=remote.parse_payment(s)
            print('buildAccountSetTx delegate result is', result)

if __name__ == '__main__':
    unittest.main()
