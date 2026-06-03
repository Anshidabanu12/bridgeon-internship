def log_call(func):

    def wrapper(*args, **kwargs):
        print(f"function name: {func.__name__}")
        print(f"arguments:{args}")
        result =  func(*args, **kwargs)

        return result
    
    return wrapper
@log_call
def add(a,b):
    return(a+b)

@log_call
def multiplye(a,b):
    return(a*b)

@log_call
def greet(name):
    return f"hello{name}"
print(add(19,36))
print(multiplye(12,4))
print(greet("zara"))



