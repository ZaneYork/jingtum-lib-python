# coding=gbk
"""
 * User: ������
 * Date: 2018/5/16
 * Time: 11:25
 * Description: Ǯ��������ģ��
"""
#BN = require('bn.js')
#import random
import binascii
#random.randrange(0, 255)

def byteValue(src):
	#print
	hexvalue = binascii.hexlify(src.encode()).upper()
	#hexvalue = binascii.hexlify(str.encode('utf8')).upper()
	if len(hexvalue) > 1:
		#print(hexvalue)
		return str(hexvalue)
	else:
		#print(hexvalue)
		return str('0' + hexvalue)
		
class utils:
	def bytesToHex(srcinfo):
		#return "".join(str(map(byteValue, srcinfo)))
		return "".join(map(byteValue, srcinfo))
		#z = ""
		#y = z.join(x)
		#return y
		#return ''.join(map(byteValue, srcinfo))		
		#return map(byteValue, srcinfo) + ''

	def hexToBytes(srcinfo):
		assert(len(srcinfo) % 2 == 0)
		#return BN(srcinfo, 16).toArray(null, len(srcinfo) / 2)
		i = 0
		dst = []
		while i < len(srcinfo):
			k = str(srcinfo[i: i+2])
			dst.append(int(str(srcinfo[i: i+2]), 16))
			i += 2 
		return dst
