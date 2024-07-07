def romanToInt(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    subtraction_dict = {'IV': 4, 'IX': 9, 'XL': 49, 'XC': 90, 'CD': 400, 'CM': 900}
    result=0
    i=0
    while i < len(s):
        if i+1 == len(s):
            concat = s[i]
        else:
            concat = s[i] + s[i+1]
        if concat in subtraction_dict:
            result = result + (subtraction_dict.get(concat))
            i = i+2
        elif s[i] in roman_dict:
            result = result + roman_dict.get(s[i])
            i = i+1
    return result


print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))

