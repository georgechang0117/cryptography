import string
import random
import re

def random_key(length):
  key = ''
  for i in range(0, length):
   key += random.choice(string.ascii_lowercase)
  print('       Key:'+key)
  return key

def encrypt(msg, key):
  print('   Message:'+msg)
  cipher_text = ''
  for i in range(0, len(msg)):
    cipher_num = (ord(msg[i])-97 ^ ord(key[i])-97) % 26
    cipher_text += chr(cipher_num+97)
  
  return cipher_text

def decrypt(cipher_text, key):
  msg = ''
  for i in range(0, len(cipher_text)):
    decrypt_num = ((ord(cipher_text[i])-97) - (ord(key[i])-97))%26
    msg += chr(decrypt_num+97)
  return msg

print('One Time Pad Mark 1')
msg = input('Input message:')
msg = msg.lower()
pattern = re.compile('[a-z]+')
msg = ''.join(re.findall(pattern, msg))
key = random_key(len(msg))
chpher_text = encrypt(msg, key)
decrypt(chpher_text, key)

