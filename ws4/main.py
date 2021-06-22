# define number system convert function "ConvertNumSystem"
def ConvertNumSystem(num, newBase):
    try:            
        if (newBase not in [2, 8, 16]):
            raise ValueError("Invalid base system")
    except ValueError as e:
        print(e)
        return ""
    if (num == 0):
        return "0"
    
    if (num < 0):
        sign = '-'
    else:
        sign = ""
        num = - num
    res = ""
    digitsHex = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", \
                6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", \
                12: "C", 13: "D", 14: "E", 15: "F"}
    while (num != 0):
        res = str(digitsHex[num % newBase]) + res
        num //= newBase
    return sign + res

# input a decimal number "num"
while True:
    try:
        num = int(input("Enter a DECIMAL number: "))
        break
    except ValueError as e:
        print(e)

# print conversion result
print('The number in DECIMAL is', num)
print("The number in BINARY is", ConvertNumSystem(num, 2))
print("The number in OCTAL is", ConvertNumSystem(num, 8))
print("The number in HEXADECIMAL is", ConvertNumSystem(num, 16))



# testing with the build in functions
print('The number in DECIMAL is', num)
print("The number in BINARY is", bin(num))
print("The number in OCTAL is", oct(num))
print("The number in HEXADECIMAL is", hex(num))