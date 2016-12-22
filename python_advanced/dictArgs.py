def dictArgs(kw1, kw2= 'B', **kw3):
    print('kw 1:%s ' % kw1)
    print('kw 2:%s ' % kw2)
    for eachKw in kw3:
        print('the %s ---->:%s ' % (eachKw,kw3[eachKw]))
if __name__ == '__main__':
    dictArgs('A')
    #   kw 1:A
    #   kw 2:B
    dictArgs('23','C')
    #   kw 1:23
    #   kw 2:C
    dictArgs('12','A', c = 'C',d = '12121212')
    #   kw 1:12
    #   kw 2:A
    #   the d ---->:12121212
    #   the c ---->:C
    dictArgs('kw',c = 'C',d = '12121212',kw = 'KW')
    #   kw 1:kw
    #   kw 2:B
    #   the kw ---->:KW
    #   the d ---->:12121212
    #   the c ---->:C
