
#!/usr/bin/env python
# coding: utf-8

# In[79]:


# Homework 5
# Testing the avalanche properties of AES using an automated code

# Write a function to test the avalanche property of AES when different single bits of 
# the inputblock are inverted. 

# In this experiment you receive an initial inputblock and key to perform AES encryption and
# find the cipherblock. Then you will use the bitlist provided as the 3rd input to the function
# to decide which bit of the inputblock to invert in additional experiments and then perform the
# AES encryption again on the modified input (with only one bit difference to original input)
# Then you compare the ciphertext for each additional experiment with the ciphertext of the
# original experiment and count the number of bits that are different between them.

# The output of your function will be the list of the number-of-differences from all experiments

# Make sure you test your code before submission by setting the bitlist to [7] and comparing the results 
# with Table 6.5 and Table 6.6 of the textbook. you can also try inverting other bit values manually and generate 
# ciphers using the AES example we did in the class and compare with the output of your function.

# As usual, we will import your submitted python file in another script and just call the aes_input_av_test() and
# aes_key_av_test() functions and check the output list of each function. It's ok if you have other utility functions
# in your submission and they will not be called or tested.

from Crypto.Cipher import AES
def aes_input_av_test(inputblock, key, bitlist):
    # inputblock and key are 16 byte values each
    # bitlist is a list of integers that define the position of the
    # bit in the inputblock that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    
    
    print("inputblock :",inputblock)
   
    cipher = AES.new(key, AES.MODE_ECB)
    
    originalcipher = cipher.encrypt(inputblock)
    print("originalcipher :",originalcipher)
    print("originalcipher :",originalcipher.hex())
    
    orignalbitslist = [bin(int(b))[2:].zfill(8) for b in inputblock]
    
    inputallbits = ''.join(orignalbitslist)
    print("inputallbits: ",inputallbits)
    
    inputallbitlist = [b for b in inputallbits]
    #print("allbitslist: ",allbitslist)
    # 3- for every value given in the bitlist:
    invertallbitlist = inputallbitlist
    for b in bitlist:
        #invert the value of the corresponding bit in the inputblock (doesn't have to be in this exact
        # function form)
     #   newinput = invertbit(inputblock, b)
        if invertallbitlist[b]=='0':
            invertallbitlist[b]='1'
        else:
            invertallbitlist[b]='0'
    #print("invertallbitlist: ",invertallbitlist)
    allnewbits = ''.join(invertallbitlist)
    print("allnewbits: ",allnewbits)
    newinput=int(allnewbits, 2).to_bytes(len(allnewbits) // 8, byteorder='big')
    print("newinput: ",newinput)
            
        # perform encryption
     #   newcipher = aes_enc(newinput, key)
    newcipher = cipher.encrypt(newinput)
    print('new cipher :',newcipher)
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        # Use any method you like to find the difference. 
    numbitdifferences = 0
     #   numbitdifferences = findbitdiff (originalcipher, newcipher)
        
    orignalcipherlist=[bin(int(b))[2:].zfill(8) for b in originalcipher]
    cipherlistallbits = ''.join(orignalcipherlist)
    print("cipherlistallbits :",cipherlistallbits)
    
    newcipherlist=[bin(int(b))[2:].zfill(8) for b in newcipher]
    newcipherlistallbits = ''.join(newcipherlist)
    
    for (i,j) in zip(cipherlistallbits,newcipherlistallbits):
    #for (i,j) in zip('11111111000010111000010001001010000010000101001110111111011111000110100100110100101010110100001101100100000101001000111110111001','01100001001010111000100100111001100011010000011000000000110011011110000100010110001000100111110011100111001001000011001111110000'):
        if i!=j:
            numbitdifferences = numbitdifferences + 1
            #diff_list.append(i)
        
        # add it to the list
     #   diff_list.append(numbitdifferences)
    diff_list.append(numbitdifferences)
    print("numbitdifferences",numbitdifferences)
    print("diff_list :", diff_list)
        
     #return the list of numbers
    return diff_list

# We also perform similar experiment by keeping the inputblocl fixed and changing the
# selected bits of the key
def aes_key_av_test(inputblock, key, bitlist):
    # inputblock and key are 16 byte values each
    # bitlist is a list of integers that define the position of the
    # bit in the key that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    print("inputblock :",inputblock)
   
    cipher = AES.new(key, AES.MODE_ECB)
    
    originalcipher = cipher.encrypt(inputblock)
    print("originalcipher :",originalcipher)
    print("originalcipher :",originalcipher.hex())
    
    orignalbitslist = [bin(int(b))[2:].zfill(8) for b in key]
    
    inputallbits = ''.join(orignalbitslist)
    print("inputallbits: ",inputallbits)
    
    keyallbitlist = [b for b in inputallbits]
    
    invertkeybitlist = keyallbitlist
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the key (doesn't have to be in this exact
        # function form)
        #newkey = invertbit(key, b)
        if invertkeybitlist[b]=='0':
            invertkeybitlist[b]='1'
        else:
            invertkeybitlist[b]='0'
        
        # perform encryption
    allnewbits = ''.join(invertkeybitlist)
    print("allnewbits: ",allnewbits)
    newkey=int(allnewbits, 2).to_bytes(len(allnewbits) // 8, byteorder='big')
    print("newinput: ",newkey)
    cipher_new = AES.new(newkey, AES.MODE_ECB)
    newcipher = cipher_new.encrypt(inputblock)
    print('new cipher :',newcipher)
    numbitdifferences = 0
   
        #newcipher = aes_enc(inputblock, newkey)
         
        #newcipher = AES.new(inputblock, newkey)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
    orignalcipherlist=[bin(int(b))[2:].zfill(8) for b in originalcipher]
    cipherlistallbits = ''.join(orignalcipherlist)
    print("cipherlistallbits :",cipherlistallbits)
    
    newcipherlist=[bin(int(b))[2:].zfill(8) for b in newcipher]
    newcipherlistallbits = ''.join(newcipherlist)
    #numbitdifferences = findbitdiff (originalcipher, newcipher)
        
        # add it to the list
        #diff_list.append(numbitdifferences)
    for (i,j) in zip(cipherlistallbits,newcipherlistallbits):
    #for (i,j) in zip('11111111000010111000010001001010000010000101001110111111011111000110100100110100101010110100001101100100000101001000111110111001','01100001001010111000100100111001100011010000011000000000110011011110000100010110001000100111110011100111001001000011001111110000'):
        if i!=j:
            numbitdifferences = numbitdifferences + 1
            #diff_list.append(i)
        
        # add it to the list
     #   diff_list.append(numbitdifferences)
    diff_list.append(numbitdifferences)
    print("numbitdifferences",numbitdifferences)
    print("diff_list :", diff_list)
        
    # return the list of numbers
    return diff_list

def test_module():
    # aes_input_av_test(bytes.fromhex('0023456789abcdeffedcba9876543210'),bytes.fromhex('0f1571c947d9e8590cb7add6af7f6798'),[0,1])
    # aes_input_av_test(b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98',[7])
    aes_input_av_test(bytes.fromhex('0123456789abcdeffedcba9876543210'),bytes.fromhex('0f1571c947d9e8590cb7add6af7f6798'), [7])
    aes_key_av_test(b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10',b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98',[7])
    #print("textbook")


# test_module()
if __name__ == "__main__":
    test_module()
