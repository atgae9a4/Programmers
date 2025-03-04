def solution(A, B):
    answer = 0
    if A == B:
        return answer
    for _ in range(len(A)):
        A = A[-1] + A[:-1]
        answer += 1
        if A == B:
            return answer
        
    return -1