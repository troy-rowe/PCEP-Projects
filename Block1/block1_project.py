#This is assigning values used throughout this project
user_name: str = input("Enter your username: ")
num_code: int = int(input("Enter your number code: "))
int_val_num: int = int(input("Enter your internal validation number: "))

#This will convert the numbers into binary bytes
num_code_bin: int = int(bin(num_code))
val_num_bin: int = int(bin(int_val_num))

#This will perform a numeric operation. I am unsure to what I should do for the time being. It will have a placeholder. I need this to satisfy the step 3 requirements
add = num_code + int_val_num
sub = num_code - int_val_num
mul = num_code * int_val_num
div = num_code / int_val_num
mod = num_code % int_val_num
floor_div = num_code // int_val_num

#I might do some operations with binary. These will also be placeholders. I might use this to fulfill step 3 requirements
add_bin = num_code_bin + val_num_bin
sub_bin = num_code_bin - val_num_bin
mul_bin = num_code_bin * val_num_bin
div_bin = num_code_bin / val_num_bin
mod_bin = num_code_bin % val_num_bin
floor_div_bin = num_code_bin // val_num_bin
and_bin = num_code_bin & val_num_bin
or_bin = num_code_bin | val_num_bin
xor_bin = num_code_bin ^ val_num_bin
left_shift_bin = num_code_bin << val_num_bin
right_shift_bin = num_code_bin >> val_num_bin