def int_to_roman(num):
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ""
    for value, symbol in roman_map:
        count = num // value
        result += symbol * count
        num -= value * count
    return result
number = int(input("Enter a number (1-3999): "))
print("Roman numeral:", int_to_roman(number))
