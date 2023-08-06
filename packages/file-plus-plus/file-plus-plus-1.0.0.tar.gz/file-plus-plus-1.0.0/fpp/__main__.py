from . import *
put_file("hello.txt", "w", data="hello!")
print(get_file("hello.txt"))
