
def insert_value(arr, index, value):
    arr.insert(index, value)
    return arr


my_array = [10, 20, 30, 40]
modified_array = insert_value(my_array, 0, 25)
print(modified_array)
