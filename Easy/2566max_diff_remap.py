num = int(input())
str_num = str(num)
def find_max(num_str):
    for i in range(len(num_str)):
        if num_str[i]=='9':
            continue
        else:
            n = num_str[i]
            num_str = num_str.replace(n,'9')
            break
    return num_str

def find_min(num_str):
    for i in range(len(num_str)):
        if num_str[i]=='0':
            continue
        else:
            n = num_str[i]
            num_str = num_str.replace(n,'0')
            break
    return num_str
print(find_max(str_num))
print(find_min(str_num))


# Passed