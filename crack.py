import hashlib

flag = 0

pass_hash = input("Enter md5 hash: ")

word_list = input("File name: ")

try:
    pass_file = open (word_list, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    if digest == pass_hash:
        print("password found")
        print("password is " + word)
        flag = 1
        break

if flag == 0:
    print("password/passphrase is not in the list")
