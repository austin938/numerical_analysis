# List comprehension
new_list = [i*2 for i in range(10)]



def increment():
    # The x here is a global variable
    x = 10
    x += 1
    return x

print(increment())