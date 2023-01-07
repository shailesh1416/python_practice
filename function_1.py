# importing a from other module
from introduction import my_intro,print_table,add_2_number,my_sum,full_name

my_intro()

print_table(17)

# enter first name and last name in function
first_name = input("Enter first name : ")
last_name = input("Enter last name : ")
print("Full Name : ",full_name(first_name,last_name))


print("Addition of 2 Number :",add_2_number(5,2))

print("Sum of Numbers :",my_sum(1,2,3,4,5))