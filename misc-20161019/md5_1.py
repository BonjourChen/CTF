import hashlib
import re

s1 = 'asdf133'
s2 = '33fdsa'
s3 = '54'

for i in range(0,100):
	for j in range(0,100):
			str1 = s1 + str(i) + s3 + str(j) + s2
			m = hashlib.md5()
			m.update(str1)
			res = m.hexdigest()
			if res == '269330a3a6ad86f0d7574b78a9a637e6':
				print i
				print j