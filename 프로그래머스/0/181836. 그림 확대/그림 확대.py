def solution(picture, k):
    answer = []
    answer2 = []
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            answer.append(picture[i][j] * k)
        
        for p in range(k):
            answer2.append(''.join(answer))
        answer = []
    return answer2