def int2roman(number):
    numeralorder = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    numeralletters = {
        1000 : "M", 900 : "CM", 500 : "D", 400 : "CD",
        100 : "C", 90 : "XC", 50 : "L", 40 : "XL",
        10 : "X", 9 : "IX", 5 : "V", 4 : "IV",
        1 : "I" }
    result = ""
    if number <1 or number > 4999:
        raise ValueError
    for value in numeralorder:
        while number >= value:
            result += numeralletters[value]
            number -= value
    return result

try:
    print(int2roman(int(input("Enter an Integer (1 to 4999): "))))
except ValueError:
    print("Try again")
    
