#the file manage

def print_file_info(file_name):
    # parameter file_name
    # return: None
    f = None
    try:
        open(file_name, "r", encoding = "UTF-8")
        content = f.read()
        print(f"the following content is the whole: {content}")
    except Exception as e:
        print()
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    f = open(file_name, 'a', encoding = "UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    #print_file_info
    append_to_file("../file/word.txt", "This is my first python project")