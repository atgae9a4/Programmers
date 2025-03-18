def solution(dots):
    # 가능한 모든 직선 쌍의 기울기 비교 (총 3가지 경우)
    pairs = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]
    
    for a, b, c, d in pairs:
        # 기울기 계산
        if dots[a][0] == dots[b][0]:  # x 좌표가 같으면 수직선 (기울기 무한대)
            slope1 = float('inf')
        else:
            slope1 = (dots[a][1] - dots[b][1]) / (dots[a][0] - dots[b][0])

        if dots[c][0] == dots[d][0]:  # x 좌표가 같으면 수직선 (기울기 무한대)
            slope2 = float('inf')
        else:
            slope2 = (dots[c][1] - dots[d][1]) / (dots[c][0] - dots[d][0])

        # 기울기가 같다면 평행한 두 직선이 존재하는 것이므로 1 반환
        if slope1 == slope2:
            return 1
    
    return 0
