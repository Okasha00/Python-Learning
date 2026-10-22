def greet(name):
    print("Hello" + name)
    return
print("The name is:","sameer")

#-----------------------------------------------#---------------------------------

def add (a,b):
    return a+b 

add(3,4)
print("The sum is:", add(3,4))

#-----------------------------------------------#---------------------------------
#Default and keyword arguments


def power(base, exp=2):         # exp is optional
    return base ** exp

power(5)                        # 25
power(2, 3)                     # 8
power(exp=3, base=2)            # 8 (order doesn't matter with names)




def min_max(a, b):
    return min(a, b), max(a, b)

low, high = min_max(7, 3)