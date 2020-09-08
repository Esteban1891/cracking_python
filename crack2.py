import hashlib
"""create funtion md5b encrypt md5"""


def function_md5():
    """create function md4"""
    flag = 0
    pass_md5 = input("pass md5: ")
    pass_file = input("pass file:  ")

    try:
        file_open = open(pass_file, "r")
    except:
        print("file not found")
        quit()


    for word_file in file_open:
        file_encode = word_file.encode("utf-8")
        file_encripty = hashlib.md5(file_encode.strip()).hexdigest


        if file_encripty() == pass_md5:
            print("file found")
            print("password is " +  word_file)
            flag = 1
            break


if __name__ == '__main__':
    function_md5()
