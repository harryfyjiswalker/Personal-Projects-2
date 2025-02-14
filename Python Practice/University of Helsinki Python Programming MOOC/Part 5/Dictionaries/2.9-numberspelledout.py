def dict_of_numbers():
    dict1 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
         9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
         20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
         80: 'eighty', 90: 'ninety'}
    dict2 ={}
    dict2.update(dict1)
    for i in range(100):
        if i not in dict1:
            if (i//10) * 10 in dict1:
                dict2[i] = dict1[(i//10)*10] + "-" + dict1[i%10]
    return dict2

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
