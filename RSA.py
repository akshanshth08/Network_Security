
#!/usr/bin/env python
# coding: utf-8

# ## Homework 6
# ### Review the example usages of the RSA-related operations of the Crypto package given below and
# ### refer to online documents of the package and google search for learning more about it.
# ###
# ### 1- Use the ssh-keygen on your computer to create the two id_rsa and id_rsa.pub files for a 2048 bit keys
# ### 2- create your python script hw6_rsa.py with the following functions
# ####
# #### As one of the tests for grading, we will provide our own keys and test for given plaintexts whete sequences of 
# #### rsa_enc_public() + rsa_dec_private() and also rsa_end_private() + rsa_dec_public() recover the original plaintexts
#  
# #### Function:

# In[1]:


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import binascii
def importkeys(id_rsa_filename):
    # This function receives the full path of the id_rsa file as a string (including the file name itself) and
    # import the key information and returns the keypair
    # example 'c:/myfolder/id_rsa' (using forward '/' helps avoid some string issues)
    
    f = open(id_rsa_filename,'r')
    keypair = RSA.importKey(f.read())
    #print('keypair :',keypair)
    f.close()
    #print(f"Keys:  (n={hex(keypair.n)}\ne={hex(keypair.e)}\nd={hex(keypair.d)})")
    f = open(id_rsa_filename+'.pub','r')
    pubkey = RSA.importKey(f.read())
    f.close()
    #print(pubkey)
    print(f"Pub Keys:  (n={hex(pubkey.n)}\ne={hex(pubkey.e)})")    
    # return the complete keypair in the keypair format used in Crypto RSA module.  
    return keypair
importkeys("c:/Users/aksha/Downloads/id_rsa")

def rsa_enc_public(inputblock, keypair):
    # inputblock is a plaintext defined as a byte sequence
    # ciphertext is the encrypted data as byte sequence encrypted using the public key
    pubKey = keypair.publickey()
    
    encryptor = PKCS1_v1_5.new(pubKey)
    ciphertext = encryptor.encrypt(inputblock)
    print("Encrypted:", binascii.hexlify(ciphertext))
    
    return ciphertext

def rsa_enc_private(inputblock, keypair):
    # inputblock is a plaintext defined as a byte sequence
    # ciphertext is the encrypted data as byte sequence encrypted using the private key
 #   print("keypair :",keypair)
 #   privKeyPEM = keypair.exportKey()
 #   print("private key :",privKeyPEM)
 #   encryptor = PKCS1_v1_5.new(privKeyPEM)
 #   encrypted = encryptor.encrypt(inputblock)
 #   print("Encrypted:", binascii.hexlify(encrypted))    
    return ciphertext

#rsa_enc_private('A message for encryption',importkeys("c:/Users/aksha/Downloads/id_rsa"))

def rsa_dec_public(cipherblock, keypair):
    # cipherblock is a given ciphertext defined as a byte sequence
    # plaintext is the decrypted data as byte sequence decrypted using the public key
    
    return plaintext

def rsa_dec_private(cipherblock, keypair):
    # cipherblock is a given ciphertext defined as a byte sequence
    # plaintext is the decrypted data as byte sequence decrypted using the private key
    
    decryptor = PKCS1_v1_5.new(keypair)
    plaintext = decryptor.decrypt(cipherblock, None)
    print('Decrypted:', plaintext)
    
    return plaintext


def test_module():
    importkeys("c:/Users/aksha/Downloads/id_rsa")
    rsa_enc_public(b'A message for encryption', importkeys("c:/Users/aksha/Downloads/id_rsa"))
    rsa_dec_private(rsa_enc_public(b'ABCDE', importkeys("c:/Users/aksha/Downloads/id_rsa")),
    importkeys("c:/Users/aksha/Downloads/id_rsa"))

# test_module()
if __name__ == "__main__":
    test_module()
