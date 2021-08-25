def rotate_string(my_string, b):
   
    if len(my_string) > 0:
        b = b % len(my_string) # handle wraparound
    return my_string[-b:] + my_string[:-b]

    from rotate import rotate_string

print(rotate_string("MyString", 2))
# -> "ngMyStri"