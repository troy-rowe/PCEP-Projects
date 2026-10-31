#This is assigning values used throughout this project
user_name: str = input("Enter your username: ")
num_code: int = int(input("Enter your number code: "))
int_val_num: int = int(input("Enter your internal validation number: "))

#This will convert the numbers into binary bytes
num_code_bin: str = bin(num_code)
val_num_bin: str = bin(int_val_num)