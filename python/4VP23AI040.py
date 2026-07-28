print(len([1,2,3]))
a=10
def outer_function():
    b=20
    def  inner_function():
        c=30
        print("Local c:",c)
        print("Enclosing b:",b)
        print("Global a:",a)
        print("Built_in len:",len([1,2,3]))
    inner_function()
outer_function()
