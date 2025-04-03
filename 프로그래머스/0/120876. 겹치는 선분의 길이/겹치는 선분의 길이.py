def solution(lines):
    arr = [0] * 201  # -100 ~ 100 을 0 ~ 200 으로 표현

    for line in lines:
        start, end = line
        for i in range(start + 100, end + 100):  # 우측 미포함
            arr[i] += 1

    answer = 0
    for count in arr:
        if count >= 2:
            answer += 1

    return answer
