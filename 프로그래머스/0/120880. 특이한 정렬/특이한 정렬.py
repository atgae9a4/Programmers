def solution(numlist, n):
    n_list = [abs(i - n) for i in numlist]
    u_list = sorted([j for j in set(n_list)])
    answer = []
    for x in u_list:
        if n_list.count(x) == 1:
            if(n + x) in numlist:
                answer.append(n + x)
            else:
                answer.append(n - x)
        else:
            answer.append(n + x)
            answer.append(n - x)
        
    return answer
    