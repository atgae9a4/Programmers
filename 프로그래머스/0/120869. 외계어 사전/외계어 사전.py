def solution(spell, dic):
    dic1 = [''.join(sorted(set(dic[x]))) for x in range(len(dic))]

    right_spell = ''.join(sorted(spell))
    print(right_spell)
    if right_spell in dic1:
        return 1
    else:
        return 2
