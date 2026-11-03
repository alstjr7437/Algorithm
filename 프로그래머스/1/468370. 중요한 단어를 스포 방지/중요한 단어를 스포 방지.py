def solution(message, spoiler_ranges):
    answer = 0
    index = 0 
    word = {}
    secretWord = {}
    spoiler = []

    # 스포일러 순회하기
    for i in spoiler_ranges:
        for j in range(i[0], i[1]+1):
            spoiler.append(j)
    
    thisWordSecret = False
    
    for i in range(len(message)):
        
        # 스포일러 위치이면 비밀 문자 처리 
        if message[i] != " " and i in spoiler:
            thisWordSecret = True
        
        # 단어 위치 정하기
        if message[i] == " " or i == len(message) - 1:
            if i == len(message) - 1:
                currentWord = message[index:i+1]
            else:
                currentWord = message[index:i]
            
            if thisWordSecret == False :
                if currentWord in word:
                    word[currentWord] += 1
                else:
                    word[currentWord] = 1
            else:
                if currentWord in secretWord:
                    secretWord[currentWord] += 1
                else:
                    secretWord[currentWord] = 1
                    
            index = i+1
            thisWordSecret = False
    
    print(word)
    
    for w in secretWord:
        if w not in word:
            answer += 1
    
    # 모두 순회 후 단어 딕셔너리에 0인 값이 있으면 result +=1   
    
    return answer