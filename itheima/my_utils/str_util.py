#relevant string
def str_reverse(s):
    return s[::-1]

def substr(s, x, y):
    #s is the string being striped
    #x is the start 
    #y is the end
    return s[x : y]

if __name__ == "__main__":
    print(str_reverse("heimachengxuyuan"))
    print(substr("heimachengxuyuan", 2, 10))
    