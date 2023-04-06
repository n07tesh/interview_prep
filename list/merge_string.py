import textwrap

def merge_the_tools(string, k):
    arr = textwrap.wrap(string, k)
    for i in arr:
        oneSub = []
        for j in list(i):
            if j not in oneSub:
                oneSub.append(j)
        print("".join(oneSub))

if __name__ == "__main__":
    string = input()
    k = int(input())
    merge_the_tools(string, k)
