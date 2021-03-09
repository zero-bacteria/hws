from django.shortcuts import render
import random
import requests
# Create your views here.

def lotto(request):
    # url을 받아와서 지정해주었다.
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    # 해당 url에 요청
    res = requests.get(url)
    # 요청한것을 딕셔너리 형태로
    win_info = res.json()
    # 당첨번호 초기화
    winning_number = []
    # 키밸류 값으로 반복
    for k,v in win_info.items():
        # 순서 구분을 위해서 당첨 번호 먼저 받아오기
        # 그냥 해당 글자가 들어가면 당첨번호니까 그원리 이용
        if 'drwtNo' in k:
            winning_number.append(v)
    # 마지막으로 보너스 넘버 받아오기
    bnus_number = win_info.get('bnusNo')
    

    # 등수들 초기화
    fifth = 0
    fourth = 0
    third = 0
    second = 0
    first = 0
    boom = 0

    for _ in range(1000):
        numbers = random.sample(range(1,46),6)
        # 카운트 변수 초기화
        cnt = 0
        for i in range(len(numbers)):
            if numbers[i] in winning_number:
                cnt += 1

        if cnt == 3:
            fifth += 1
        elif cnt == 4:
            fourth += 1
        elif cnt == 5:
            if bnus_number in numbers:
                second += 1
            else:
                third += 1
        elif cnt == 6:
            first += 1 
        else:
            boom += 1

    # 다 실행한 후에 context로 넘겨주기
    context = {
    'fifth':fifth,
    'fourth': fourth,
    'third': third, 
    'second': second,
    'first': first,
    'boom': boom,
    'winning_number': winning_number,
    'bnus_number': bnus_number,
    }

    return render(request, 'pages/lotto.html', context)
