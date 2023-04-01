def specified(new,speci_str):
    # if new[0] == speci_str[0]:
    #     print("True")
    # else:
    #     print("False")                                
    speci_str.startswith(new)
if __name__=='__main__':
    new = input("enter the string")
    speci_str = input("enter the string")
    specified(new,speci_str)