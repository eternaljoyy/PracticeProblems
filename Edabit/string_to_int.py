def string_int(txt):
    if(txt.isdigit()):
        return int(txt)
    else:
        raise Exception("Please input a valid string")

print(string_int("10"))
print(string_int(""))