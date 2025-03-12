def solution(num, total):
    answer = []
    if num % 2 != 0:
        for _ in range(num):
            answer.append(total // num)
        for i in range(num):
            if i <= num // 2:
                answer[i] -= (num // 2) - i
            else:
                answer[i] += i - (num // 2)
            
    else:
        for _ in range(num):
            answer.append(total // num) # [3,3,3,3]
        for j in range(num):
            if j <= num // 2 -1:
                answer[j] -= (num // 2 - 1) - j
                
            else:
                answer[j] += j - (num // 2 - 1)
            
        
        
        
    return answer