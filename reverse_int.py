def solution(x):
    string=str(x)

    if string[0]=='-':
        return int('-'+string[:0:-1])
