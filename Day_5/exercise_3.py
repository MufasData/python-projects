
def double_zero(*args):

    zero_list = []
    index = 0

    for i in args:
        zero_list.append(i)
    
    for i in range(len(zero_list)):
        if zero_list[i] == 0:
            if zero_list[i+1] == 0:
                return True
            else:
                continue
        
    return False

print(double_zero(4,0,0.9,33,5,0,9,5,3,2))