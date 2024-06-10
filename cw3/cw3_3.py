
def capitalize_last_name(fullname):
    for i in fullname:
        if i.isalpha() or i.isspace():
            continue
        else:
            raise TypeError("Must be alphabet!")
    name = fullname.split()
    if len(name) != 2:
        raise ValueError("Must be exactly two parts")

    firstname = name[0].capitalize()
    lastname = name[1].upper()

    return f"{firstname} {lastname}"

inp = input("Input:\n")
out = capitalize_last_name(inp)
print(out)