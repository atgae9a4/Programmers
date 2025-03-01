def solution(dots):
    answer = 0
    x = []
    y = []
    for i in range(len(dots)):
        x.append(dots[i][0])
        y.append(dots[i][1])
    result1 = list(set(x))
    result2  = list(set(y))
    #print(result1)
    #print(result2)
    answer = abs(result1[1] - result1[0]) * abs(result2[1] - result2[0])


    
    return answer