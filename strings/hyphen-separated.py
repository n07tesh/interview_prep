from join import join


def hypen_separated(string):
    lst = [n for n in string.split('-')]
    lst.sort(key=None,reverse=False)
    print(lst)
    print('-',join(lst))

if __name__=='__main__':
    string = 'hello-world is good developer-python'
    hypen_separated(string)