def greet():
    print("hello")
greet() 

#create decoration
def my_decoration(func):
    def wrapper():
        print("befor function")
        func() 
        print("after function")
    return wrapper
@my_decoration
def greet():
    print("hello")
greet() 
        
        
        
def my_decorator(func):
    def wrapper (*args, **kwargs):
        # print("before function run")
        result = func(*args, **kwargs)
        print("function ended")
        return result
    return wrapper
@my_decorator
def greet():
 print("hello")
greet()