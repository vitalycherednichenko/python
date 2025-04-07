def increment_string(string):
    integer = ''
    for i in range(1, len(string) + 1):
        if string[-i].isdigit():
            integer = string[-i] + integer
        else:
            break

    integer_length = len(integer)

    if integer:
        string = string[:-integer_length]
        integer = int(integer) + 1
    else:
        integer = 1

    return string + f'{integer:0{integer_length}}'

print(increment_string('f1oo9999'))