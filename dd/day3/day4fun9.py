#scop 
# local:
def demo():
    x=10
    print(x)
demo()
#global
x=100
def demo():
    print(x)
demo()