def solution(quiz):
    answer = []
    string = []
    for i in quiz:
        string = i.split()
        
        if string[1] == "+":
            if int(string[0]) + int(string[2]) == int(string[4]):
                answer.append("O")
            else:
                answer.append("X")
        
        else:
            if int(string[0]) - int(string[2]) == int(string[4]):
                answer.append("O")
            else:
                answer.append("X")
        string = []    
                
    return answer   
                
    return answer