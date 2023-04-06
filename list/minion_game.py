def minion_game(string):
    # your code goes here
    count_kelvin = 0
    count_surat = 0
    L = len(string)
    for i in range(L):
        if string[i] not in ['A','E','I','O','U']:
            count_surat += (L-i)
        else:
            count_kelvin += (L-i)
    if count_kelvin > count_surat:
        print('kelvin',count_kelvin)
    elif count_surat > count_kelvin:
        print('surat',count_surat)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()#BANANA
    # s = 'BANANA'
    minion_game(s)