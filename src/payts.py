# coding=gbk
"""
 * User: ������
 * Date: 2018/5/16
 * Time: 11:25
 * Description: ֧�������ù�ϵģ��
"""
def __stringToHex(s):
	result = ''
	for c in s:
		d = hex(ord(c)).replace('0x', '')
		if ord(c) > 16:
			result +=  ''.join(d)
		else:
			result +=  ''.join(d)
	return result
		
class Transaction:
	"""
	 * set secret
	 * @param secret
	 * come from transaction.js
	 * ������Կ
	"""
	def __init__(self, remote):
		self._remote = remote;
		self.tx_json = {Flags: 0, Fee: fee};
		#self._filter = filter or function(v) {return v};
		self._secret = void(0);
    
	def setSecret(self, secret):
		self._secret = secret
	
	"""
	 * just only memo data
	 * @param memo
	 * ���ñ�ע
	"""
	def addMemo(self, memo):
		if not isinstance(memo, str):
			self.tx_json.memo_type = Error('invalid memo type')
			return self
		if (len(memo) > 2048):
			self.tx_json.memo_len = Error('memo is too long')
			return self
		_memo = {}
		_memo.MemoData = __stringToHex(memo.encode('utf-8'))
		self.tx_json.Memos = self.tx_json.Memos + Memo
		
	"""
	 * submit request to server
	 * @param callback
	 * �ύ֧��
	"""
	def submit(self, callback):
		for key in self.tx_json:
			if instanceof(self.tx_json[key], Error):
				return callback(self.tx_json[key].message)
        
		data = {}
		if self._remote._local_sign: #ǩ��֮�󴫸��ײ�
			self.sign(Error, blob)
			if Error:
				return callback('sign error: ', Error)
			else:
				data = {
					tx_blob: self.tx_json.blob
				}
				self._remote._submit('submit', data, self._filter, callback)
		elif self.tx_json.TransactionType == 'Signer': #ֱ�ӽ�blob�����ײ�
			data = {
				tx_blob: self.tx_json.blob
			};
			self._remote._submit('submit', data, self._filter, callback)
		else: #��ǩ�����״����ײ�
			data = {
				secret: self._secret,
				tx_json: self.tx_json
			}
			self._remote._submit('submit', data, self._filter, callback)
