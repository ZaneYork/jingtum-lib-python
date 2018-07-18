# coding=gbk
"""
 * User: ������
 * Date: 2018/5/21
 * Time: 11:25
 * Description: ����ģ��
"""
import sys

#from src.logger import logger

sys.path.append("..\src")
from src.remote import Remote
from src.util import *

def CheckErr(err, result):
    if (err):
        print('err:', err)
    elif result:
        print('res:', result)


def test(err, callback):
    if err:
        return print('err:', err)
    tx = remote.buildPaymentTx({
        'account': 'jB7rxgh43ncbTX4WeMoeadiGMfmfqY2xLZ',
        'to': 'jDUjqoDZLhzx4DCf6pvSivjkjgtRESY62c',
        'amount': {
            "value": 0.5,
            "currency": "SWT",
            "issuer": ""
        }
    })
    tx.setSecret('sn37nYrQ6KPJvTFmaBYokS3FjXUWd')
    tx.addMemo('��jDUjqoDZLhzx4DCf6pvSivjkjgtRESY62c֧��0.5swt.')  # ��ѡ
    tx.addMemo('123')
    tx.submit(CheckErr)
    #logger.info(callback)

remote = Remote({'server': 'ws://ts5.jingtum.com:5020', 'local_sign': True})
result = remote.connect(None)
#logger.info(result)
test(None, None)
