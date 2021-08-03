def verify_number(phone: str) -> bool:
    string = ''
    for n in phone:
        if n.isnumeric():
            string += n

    if len(string) == 11:
        print(string)
        return True
    
    elif len(string) <= 10:
        if len(string) == 10:
            string = string[0:2] + f'9{string[2:]}'
            print(string)
            return True
        elif len(string) == 9:
            string = '45' + string
            print(string)
            return True
        elif len(string) == 8:
            string = '459' + string
            print(string)
            return True
        else:
            print(string)
            return False
    else:
        print(string)
        return False

print(verify_number('4512345678'))
