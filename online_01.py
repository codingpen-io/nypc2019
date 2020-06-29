# 예선 연습 문제 비밀번호 검사
# input : {NYPC2019} output: invalid
# input : {NYPc2019} output: valid


def is_valid(password):
    if len(password) < 8:
        return False
    if len(password) > 15:
        return False
    
    num_upper = 0
    num_lower = 0
    num_special = 0
    special = '!@#$%^&*()-=_+|;:\'"/?,.<>~[]{}`'
    
    for c in password:
        if c.isupper():
            num_upper += 1
        elif c.islower():
            num_lower += 1
        elif special.find(c) >= 0:
            num_special += 1
     
    print(num_upper, num_lower, num_special)
    if num_upper == 0:
        return False
    if num_lower == 0:
        return False
    if num_special == 0:
        return False
    return True
    
r = is_valid(input())

if r:
    print("valid")
else:
    print("invalid")


    


