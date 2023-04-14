def arrayManipulation(n, queries):
    # Write your code here
    scores = [0] * (n + 1)
    
    for a, b, k in queries:
        scores[a-1] += k
        scores[b-1+1] -= k
        
    running_max = running_sum = 0
    for s in scores:
        running_sum += s
        if running_sum > running_max:
            running_max = running_sum
        
    return running_max

if __name__=="__main__":
    n = 10
    queries = [
        [1 ,2, 100],
        [2, 5, 100],
        [3, 4, 100]
        ]

    arrayManipulation(n,queries)