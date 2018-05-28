# coding=gbk
"""
 * User: ������
 * Date: 2018/5/16
 * Time: 11:25
 * Description: Ǯ��������ģ��
"""
import hashlib

class sha512:
	def add(self, bytes):
		self.hash.update(bytes)
		return self

	def addU32(self):
		return self.add([i >> 24 & 0xFF, i >> 16 & 0xFF, i >> 8 & 0xFF, i & 0xFF])

	def finish(self):
		return self.hash.digest()

	def first256(self):
		return self.finish().slice(0, 32)

	def first256BN(self):
		return BN(self.first256())
