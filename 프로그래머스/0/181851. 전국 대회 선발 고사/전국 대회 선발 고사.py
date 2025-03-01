def solution(rank, attendance):
    answer = 0
    ranking = []
    for i in range(len((rank))):
        if attendance[i]:
            ranking.append(rank[i])
    ranking.sort()
    
    answer = 10000 * rank.index(ranking[0]) + 100 * rank.index(ranking[1]) + rank.index(ranking[2])
            
            
    return answer