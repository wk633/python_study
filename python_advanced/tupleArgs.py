def tupleArgs(arg1, arg2= 'B', *arg3):
    print('arg 1:%s ' % arg1)
    print('arg 2:%s ' % arg2)
    for eachArgNum in range(len(arg3)):
        print('the %d in arg 3 :%s ' % (eachArgNum,arg3[eachArgNum]))
if __name__ == '__main__':
    tupleArgs('A')
    #   arg 1:A
    #   arg 2:B
    tupleArgs('23','C')
    #   arg 1:23
    #   arg 2:C
    tupleArgs('12','A','GF','L')
    #   arg 1:12
    #   arg 2:A
    #   the 0 in arg 3 :GF
    #   the 1 in arg 3 :L 
