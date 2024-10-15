def myDecorator(function):
    
    def wrapper():
        function()
        print("After the function is called, I will be executed")
        
    return wrapper



def sayHello():
    print("Hello")

# implementation of decorator - 01
myDecorator(sayHello)() # a single function under a function -> sayHello(1stFunc)-(2ndFunc)

# implementation of decorator - 02
@myDecorator
def sayBye():
    print("Bye!")


sayBye() # a single function under a function -> sayBye(1stFunc)-(2ndFunc)