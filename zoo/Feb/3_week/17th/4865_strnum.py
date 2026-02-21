t = int(input())
for tc in range(1, t+1):
    # 길이가 n인 문자열 str1(여기에 들은 원소가 str2에 몇 개 들었는지 세야함)
    str1 = set(input())
    # 길이가 m인 문자열 str2(검색대상)
    str2 = input()
    
    # 출력 -> str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 max 글자 개수.
    
    # str1에 포함된 글자들이 str2에 몇개 들었을까 확인하기 위해
    
    ## str1의 원소들을 key로 하고 값을 0으로 하는 딕셔너리 추가
    str_cnt_dict = {key : 0 for key in str1}
    
    ## str2의 글자들을 순회하면서 key에 있는지 확인하여 있다면 개수 +1
    for char in str2:
        if char in str_cnt_dict:
            str_cnt_dict[char] += 1
    
    ## 최대 글자 개수를 구하기 위해 values활용
    ### 이때 딕셔너리는 빈 딕셔너리가 절대 아님 -> max 사용 가능
    answer = max(str_cnt_dict.values())
    
    print(f"#{tc} {answer}")