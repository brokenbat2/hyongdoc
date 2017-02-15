for num in range(1,6):
    # 매 loop 마다 리스트 초기화
    list_a = [0,0,0,0,0]

    # 3을 기준으로 나눔.
    if num <= 3:
        # 1, 2, 3열은 1이 각각 1개, 3개, 5개로 등차수열.
        for num2 in range(3-num, 2+num):
            list_a[num2] = 1
    else:
        #3, 4, 5열은 1이 각각 5개, 3개, 1개로 등차수열임.
        for num2 in range(-3+num, 8-num):
            list_a[num2] = 1

    print(list_a)
