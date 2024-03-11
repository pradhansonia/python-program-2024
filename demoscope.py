def myfunc():
    x = 30
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

x = 300
def myfunc():
    print(x)
myfunc()
print(x)


x = 300
def myfunc():
    print("inside function",x)
myfunc()
print("outside function",x)


def myfunc_global():
    global x 
    x = 300

myfunc_global()
print(x)