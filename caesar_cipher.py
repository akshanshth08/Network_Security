
import sys


def caesar_str_enc(plaintext, K):
    ciphertext=""
    for ch in plaintext:
        encch = caesar_ch_enc(ch, K)
        ciphertext = ciphertext + encch
        
    return ciphertext

def caesar_ch_enc(ch, K):
    if ch == ' ':
        encch = ' '
        return encch
    p = ord(ch)-97
    encch = chr(((p+K) % 26)+97)
    # everything needed to map a char to its encoded char with K as the parameter
    
    return encch
    

def caesar_str_dec(ciphertext, K):
    plaintext = ""
    for ch in ciphertext:
        decch = caesar_ch_dec(ch, K)
        plaintext = plaintext + decch
        
    return plaintext

def caesar_ch_dec (ch, K):
    if ch == ' ':
        decch=' '
        return decch
    p=ord(ch)-97
    decch = chr((((p-K)%26)+97))
    
    return decch


def test_module():
    #K = int(sys.argv[1])
    #input_str = sys.argv[2]
 
    #K =3
    #input_str = "this is a test"
    #print(input_str)
    #encstr = caesar_str_enc(input_str, K)
    #print(encstr)
    encstr='&|sr%u\L(9oE04_>6D0o7E6C0cfnN'
    for i in range(27):
        decstr = caesar_str_dec(encstr, i)
        print(decstr)
    
#test_module()
if __name__=="__main__":
    test_module()
