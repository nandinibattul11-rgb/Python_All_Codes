# *args & **kwargs
#They allows function to Accept Unknown no of Arguments

def my_function(*args):
    print("First Argument:",args[0])
    print("Second Argument:",args[1])
    print("All Arguments:",args)
    print("\nArgument Type is: ",type(args))
my_function(12,23,"Jay")
    