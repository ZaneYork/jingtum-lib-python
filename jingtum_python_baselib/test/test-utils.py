# coding=gbk
"""
 * User: ������
 * Date: 2018/5/21
 * Time: 11:25
 * Description: ����ģ��
"""
import sys 
sys.path.append("../src")
from utils import utils

a=utils.hexToBytes('123344')
print(a)
a=utils.bytesToHex('abc')
print(a)
