import os

def test_os():
    print(os.listdir("./file"))
    print(os.path.isdir("./file/error.txt"))
    print(os.path.isdir("./file/word.txt"))

def get_files_recursion_from_dir(path):

    print(f"the current directory is: {path}")
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                # is dir not a file
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"the directory does not exist")
        return []

    return file_list 

if __name__ == '__main__' :
    print(get_files_recursion_from_dir("./"))
