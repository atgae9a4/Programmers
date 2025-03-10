def solution(polynomial):
    n_list = polynomial.split()
    x_sum = 0  # x 계수 합
    c_sum = 0  # 상수항 합
    
    for i in n_list:
        if 'x' in i:
            if i == 'x':
                x_sum += 1
            else:
                x_sum += int(i[:-1])         
        elif i != '+':  # 숫자인 경우
            c_sum += int(i)

    # 최종 정리된 다항식 문자열 구성
    if x_sum == 0:  # x 항이 없을 경우
        return str(c_sum)
    elif c_sum == 0:  # 상수항이 없을 경우
        return "x" if x_sum == 1 else f"{x_sum}x"
    else:
        return ("x" if x_sum == 1 else f"{x_sum}x") + " + " + str(c_sum)
