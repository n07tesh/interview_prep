
def matchingStrings(stringList, queries):
    # Write your code here
    return [stringList.count(x) for x in queries]

if __name__ == "__main__":
    stringList = ['ab','ab','abc']
    queries = ['ab','abc','bc']
    matchingStrings(stringList,queries)