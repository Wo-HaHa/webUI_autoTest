def sort(num, type):
    x = 0
    y = 0
    while num>0:
        if type == 0:
            x = y+2
            break
        elif type == 1:
            x = y+10
            break
        else:
            x = y+20
            break
    return x