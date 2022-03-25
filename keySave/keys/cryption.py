"""
传入明文进行加密;
传入密文进行解密
"""
import binascii
from pyDes import des, CBC, PAD_PKCS5
#需要安装 pip install pyDes
#目前这两个函数，处于黑盒操作阶段。

"""
des加密函数：
    secretKey: 密钥. 密钥不指定，默认是admin123.
    s: 明文字符串
"""
def desEncryption(s,secretKey="admin123"):
    iv = secretKey
    k = des(secretKey, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    binString = binascii.b2a_hex(en)
    return binString.decode() #二进制转字符串
    
"""
des解密函数:
    secreKey: 密钥. 密钥不指定，默认是admin123
    s: 密文字符串
"""
def desDecryption(s,secretKey="admin123"):
    iv = secretKey
    k = des(secretKey, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de.decode() #二进制转字符串

# ciphertext = desEncryption("test123")
# print(ciphertext)
# print(type(ciphertext))
#
# plaintext = desDecryption(ciphertext)
# print(plaintext)
# print(type(plaintext))