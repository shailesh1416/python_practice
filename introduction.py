# write a function to introduce yourself

def my_intro():
    print()
    print("************************")
    print("Hello..👋")
    print("My name is Shailesh")
    print("I am a computer Science graduate.💻")
    print("I love Cycling🚴 and Fighting🥷")
    print("************************")
    print()


# function to print table of a number

def print_table(number):
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")

# function to return full name
def full_name(fname,lname):
    return f"{fname} {lname}"

# function to print sum of two number
def add_2_number(num1, num2):
    return num1+num2


# function to print sum of all given number
def my_sum(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum


# **kwargs i.e keywords arguments later
