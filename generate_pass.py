import random 

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@?=+/#$&"

lenght_psswd = 12
use_for = lower_case + upper_case + numbers + symbols 

password = "".join(random.sample(use_for, lenght_psswd))

print(("Your generated password is : ") + password)
