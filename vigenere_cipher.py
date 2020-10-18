
#!/usr/bin/env python
# # Homework 2- Part 1: Vigenere Cipher
# ## Write an encryption and a decryption function for Vigenere cipher as described below

# In[42]:


# Hint: You can use your homework1 caesar encryption and decryption functions but you need to copy them
#       here and avoid importing that homework since we won't be able to do the same thing for grading.
# We will be importing this python file and call its functions in another grading script. So we don't need any
# command line argument support like what we did for the caesar cipher.
import numpy as np

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


# Vigenere encryption function
def vigenere_enc(keyword, plaintext):
    # keyword is a string of arbitrary length
    # plaintext is the plaintext string of arbitrary length
    # Both strings will be from {a,b,...,z}
    s = plaintext
    s = s.replace(' ', '')
    #print("plaintext : " + s)
    #print("keyword : " + keyword)

    c = ""
    index = 0
    key = ""
    while index < len(s):
        if index > len(keyword)-1:
            #print("index :%d" % index)
            #print("len(keyword) :%d"%len(keyword))
            #print("remainder %d" %(index % len(keyword)))
            key = keyword[index % len(keyword)]
        else:
            key = keyword[index]
        p = ord(key) - 97
        cip = caesar_str_enc(s[index], p)
        #    print(cip)
        c = c + cip
        index += 1

    # perform the encryption of given plaintext using the given keyword
    # according to the Vigenere cipher. You need to repeat the keyword
    # enough times if needed to make it the same length as plaintext

    # c will be the resulting ciphertext
    # c = ...
    #print(c)
    return c


# Vionegere decryption function
def vigenere_dec(keyword, ciphertext):
    # keyword is a string of arbitrary length
    # ciphertext is the ciphertext string of arbitrary length
    # Both strings will be from {a,b,...,z}
    s = ciphertext
    s = s.replace(' ', '')
    #print("ciphertext : " + s)
    #print("keyword : " + keyword)

    # perform the decryption of given ciphertext using the given keyword
    # according to the Vigenere cipher. You need to repeat the keyword
    # enough times if needed to make it the same length as ciphertext

    p = ""
    index = 0
    key = ""
    while index < len(s):
        if index > len(keyword) - 1:
            # print("index :%d" % index)
            # print("len(keyword) :%d"%len(keyword))
            # print("remainder %d" %(index % len(keyword)))
            key = keyword[index % len(keyword)]
        else:
            key = keyword[index]
        k = ord(key) - 97
        cip = caesar_str_dec(s[index], k)
        #    print(cip)
        p = p + cip
        index += 1

    #print(p)
    # p will be the resulting plaintext
    # p = ...
    return p
    


# # Homework 2- Part 2: Hill Cipher
# ## Write an encryption and a decryption function for Hill cipher as described below

# In[ ]:


# Use the discussion above for finding the mod-26 inverse of a matrix and write the encryption and decryption 
# functions for a 3x3 Hill cipher.


# 1- clean up the inverting operations explained above to get a matrix inversion-mod-26 function
def matrixinvmod26(M):
    # Both the input argument M an doutput Minv26 are in the list of lists format i.e.,
    # [[M11,M12,M13],[M21,M22,M23],[M31,M32,M33]]
    # use np.array() and tolist() functions as described above for conversion between matrix and list-of-lists
    Mod26invTable = {}
    for m in range(26):
        for n in range(26):
            if (m * n) % 26 == 1:
                Mod26invTable[m] = n
               # print(m, n)


    Minv = np.linalg.inv(M)
    Mdet = np.linalg.det(M)

    Mdet26 = Mdet % 26
    if Mdet26 in Mod26invTable:
        Mdetinv26 = Mod26invTable[Mdet26]
    else:
        Mdetinv26 = None
        print("Matrix in not invertable")
        exit()

    Madj = Mdet * Minv
    Madj26 = Madj % 26

    Minv26 = (Mdetinv26 * Madj26) % 26
    Minv26 = np.matrix.round(Minv26, 0) % 26

    #print("Minv26:")
   # print(Minv26)
    Minv26 = Minv26.tolist()
    # Calculate Minv26
    return Minv26

# 2- write the Hill encryption function 
def hill_enc(M, plaintext):
    # M is the encryption matrix - Let's assume it's always 3x3 for now
    # M is in the list of lists format i.e.,
    # [[M11,M12,M13],[M21,M22,M23],[M31,M32,M33]]
    # plaintext is the plaintext string of arbitrary length
    # from {a,b,...,z}
    #   M = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
    # print("M: ")
    # print(M)
    s = plaintext
    s = s.replace(' ', '')
    #print("plain text :%s" % s)
    s = s.lower()
    length = len(plaintext)
    if length % 3 != 0:
        #   print("inside if")
        rem = length % 3
        fill = 3 - rem
        s = s.ljust(length + fill, 'x')
    # print(s)

    s_ind_list = [ord(c) - 97 for c in s]
    # print(s_ind_list)
    c = ""
    # print(s_ind_list)
    for i in range(0, len(s_ind_list), 3):  # it means integers from 0 to len(char_list)-1 with step 3
        sublist = s_ind_list[i:i + 3]  # it means elements i,i+1,i+2 (the last element -1)
        sublist = np.array(sublist)
        # print(sublist)
        #   M=np.array(M)
        enc_mat = np.matmul(M, sublist) % 26
        char_list = [chr(ind + 97) for ind in enc_mat]
        c = c + ''.join(char_list)

    #  print(sublist)
    # perform the encryption of given plaintext using the given matrix M
    # according to the Hill cipher. Pad the plaintext with 'x' characters to
    # make its length a multiple of 3.

    # Some helpful funcitons:
    # len(plaintext) : gives the length of the plaintext string
    # one way of selecting chunks of 3 elements from a list:
    #

    # c will be the resulting ciphertext
    # c = ...
    # c = "cipher"
    #print("cipher text :%s" % c)
    return c


# 3- write the Hill decryption function
def hill_dec(M, ciphertext):
    # M is the encryption matrix - Let's assume it's always 3x3 for now
    # M is in the list of lists format i.e.,
    # [[M11,M12,M13],[M21,M22,M23],[M31,M32,M33]]
    # ciphertext is the ciphertext string of arbitrary length
    # from {a,b,...,z}

    # perform the decryption of given ciphertext using the given matrix M
    # according to the Hill cipher.

    # p will be the resulting plaintext
    # p = ...
    s = ciphertext
    s = s.replace(' ', '')
    #print("cipher text :%s" % s)
    s = s.lower()
    length = len(ciphertext)
    s_ind_list = [ord(c) - 97 for c in s]
    #print(s_ind_list)
    p = ""
    # print(s_ind_list)
    for i in range(0, len(s_ind_list), 3):  # it means integers from 0 to len(char_list)-1 with step 3
        sublist = s_ind_list[i:i + 3]  # it means elements i,i+1,i+2 (the last element -1)
        sublist = np.array(sublist)
        # print(sublist)
        #   M=np.array(M)
        enc_mat = np.matmul(matrixinvmod26(M), sublist)%26
        char_list = [chr((int)(ind) + 97) for ind in enc_mat.tolist()]
        p = p + ''.join(char_list)
    #print("plain text :%s"%p)

    return p


def test_module():
 #   K = int(sys.argv[1])
  #  input_str = sys.argv[2]

    # K =3
    # input_str = "this is a test"
    print("Vigenere")
    #encstr = vigenere_enc("deceptive", "wearediscoveredsaveyourself")
    #print(encstr)
    decstr = vigenere_dec("chemistery", "&|sr%u\L(9oE04_>6D0o7E6C0cfnN")
    print(decstr)


    print("hill")
    encstr = hill_enc([[17, 17, 5], [21, 18, 21], [2, 2, 19]], "aim")
    print(encstr)
    decstr = hill_dec([[17, 17, 5], [21, 18, 21], [2, 2, 19]], "&|sr%u\L(9oE04_>6D0o7E6C0cfnN")
    print(decstr)


# test_module()
if __name__ == "__main__":
    test_module()

