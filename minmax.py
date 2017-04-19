def minmax(input_list):
    if min(input_list) == max(input_list):
        return [min(input_list)]
    else:
        return [min(input_list), max(input_list)]

print (minmax([1, 2, 3, 4]))