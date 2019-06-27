
def encryptXor():

    message = input("Enter the cipher text or plain text: ")
    key = input("Enter the key for encryption or decryption: ")

    output_str = ""

    for i in range(len(message)):
        current = message[i]

        current_key = key[i%len(key)]
        
        output_str += chr(ord(current) ^ ord(current_key))

    print ("Here's the output:" + output_str)

encryptXor()