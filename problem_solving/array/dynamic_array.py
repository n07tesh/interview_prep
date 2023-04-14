import os
def dynamic_array(n,queries):
    seqlist= [[] for i in range(n)]
    lastAnswer =0
    result = []
    for q in queries:
        if q[0]==1:
            seq=(q[1] ^ lastAnswer)%n
            seqlist[seq].append(q[2])
        else:
            seq=(q[1]^ lastAnswer)%n
            lastAnswer=seqlist[seq][q[2]%len(seqlist[seq])]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamic_array(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')