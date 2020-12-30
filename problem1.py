string = input('Enter String To Check Unique: ');


# Normalizing all Input to remove spaces and get in lower case
def normalize_str(input_str):
    input_str = input_str.replace(" ", "")
    return input_str.lower()


# Method to Check in Dictionary
def is_unique_1(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True


# Length of Set and length of string
def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)


# Checking character with english alphabet
def is_unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True


unique_str = normalize_str(string)

print('------------------------------')
print('You have Entered: ', unique_str)
print('------------------------------')

print('Testing Unique 1:', is_unique_1(unique_str))
print('------------------------------')

print('Testing Unique 2: ', is_unique_2(unique_str))
print('------------------------------')

print('Testing Unique 3: ', is_unique_3(unique_str))
print('------------------------------')
