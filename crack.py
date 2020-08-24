import hashlib


def crackme_pass():
    flag = 0
    md5 = input("insert code md5: ")
    file_pass = input("insert file: ")

    try:
        file_open = open(file_pass, "r")
    except:
        print("file not found")
        quit()

    for word_file in file_open:
        res = word_file.encode("utf-8")
        hash_1 = hashlib.md5(res.strip()).hexdigest()

        if hash_1 == md5:
            print("password found")
            print("password is " + word_file)
            flag = 1
            break


if __name__ == '__main__':
    crackme_pass()
