import re

# s = "python itheima"

# result = re.match("python", s)
# print(result)

s = "1pythone 3l#sj()afo*ij5 @ith8eima python"

# result = re.search("python", s)
# print(result)

# result = re.findall("python", s)
# print(result)

# result = re.findall(r'\d', s)
# result = re.findall(r'\W', s)
# result = re.findall(r'[azA-Z9]', s)
# print(result)

# r = '^[0-9a-zA-Z]{6,10}$'
# s = '1234567Ab_'
# print(re.findall(r,s))

# r = '^[1-9][0-9]{4,10}$'
# s = '12345678'

# print(re.findall(r, s))

r = r'^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$'
s = 'a.b.c.e.f.g@163.com'
print(re.match(r, s))
s = 'a.b.c.e.f.g@126.com'
# print(re.findall(r, s))
print(re.match(r, s))