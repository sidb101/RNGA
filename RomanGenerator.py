def roman(N):
    assert 0<N<4000, "due to 0<N<4000 is False"
    # ROMAN CHARACTER DICTIONARY
    rc = {
        1    : ['I','V','X'],
        10   : ['X','L','C'],
        100  : ['C','D','M'],
        1000 : ['M']
    }

    # ROMAN NUMBER STRUCTURE
    rs = ['','0','00','000','01','1','10','100','1000','02','2']

    L, fin, j = [int(i) for i in str(N)], [], 1
    for i in L[::-1]:
        fin += [''.join([rc[j][int(k)] for k in rs[i]])]
        j = j*10
    return ''.join(fin[::-1])

if __name__=='__main__':
    N = int(input("Enter N, 0<N<4000 : "))
    print("roman(N): ",roman(N))
