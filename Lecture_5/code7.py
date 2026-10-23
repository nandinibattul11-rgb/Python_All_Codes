#Position Only Parameter
def my_function(name,/):
    print("Hello",name)
my_function("Nandini")
my_function(name = "Nandini")