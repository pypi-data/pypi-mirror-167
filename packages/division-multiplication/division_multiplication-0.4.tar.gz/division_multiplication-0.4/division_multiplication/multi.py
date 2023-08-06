import math

def multiplication_by_three(num):
    return num * 3

def compare_sqrt_with_num(num1, num2):
    val = math.sqrt(num1)
    number_dec = str(val-int(val))

    if number_dec == "0.0":
        if int(val) > num2:
            return f"square root of {num1} is greater than {num2}"
        
        elif int(val) == num2:
            return f"square root of {num1} is equal to {num2}"
        
        elif int(val) < num2:
            return f"square root of {num1} is less than {num2}"
        
        else:
            return f"Something went wrong"
        
    else:
        return f"Can't find a round figured square root of {num1}"
