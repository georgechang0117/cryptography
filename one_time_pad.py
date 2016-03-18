import string
import random
import re

print('One Time Pad Mark 1')
msg = input('Input message:')
msg = msg.lower()
pattern = re.compile('[a-z]+')
msg = ''.join(re.findall(pattern, msg))
msg_num = []
key = ''
key_num = []
chpher_text = ''
for c in msg:
  msg_num.append(str(ord(c)-97))
  key_letter = random.choice(string.ascii_lowercase)
  key += key_letter
  cipher_num = (ord(c)-97 ^ ord(key_letter)-97) % 26
  chpher_text += chr(cipher_num+97)
  key_num.append(str(ord(key_letter)-97))
  
print('   Message:'+msg)
print('  MsgToNum:'+','.join(msg_num))
print('       Key:'+key)
print('  KeyToNum:'+','.join(key_num))
print('CipherText:'+chpher_text)