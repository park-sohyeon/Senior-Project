from collections import defaultdict
import requests as requests
from datetime import datetime, timedelta, date
from maps import ip_to_xy

def rain_check_forecast():
    result = defaultdict()
    now = datetime.now()

    today = datetime.today()  # 현재 지역 날짜 반환
    today_date = today.strftime("%Y%m%d")  # 오늘의 날짜 (연도/월/일 반환)

    # 어제
    yesterday = date.today() - timedelta(days=1)
    yesterday_date = yesterday.strftime('%Y%m%d')

    # 1일 총 8번 데이터가 업데이트(0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300)
    # 현재 api를 가져오려는 시점의 이전 시각에 업데이트된 데이터를 base_time, base_date로 설정
    if now.hour < 2 or (now.hour == 2 and now.minute <= 10):  # 0시~2시 10분 사이
        base_date = yesterday_date  # 구하고자 하는 날짜가 어제의 날짜
        base_time = "2300"
    elif now.hour < 5 or (now.hour == 5 and now.minute <= 10):  # 2시 11분~5시 10분 사이
        base_date = today_date
        base_time = "0200"
    elif now.hour < 8 or (now.hour == 8 and now.minute <= 10):  # 5시 11분~8시 10분 사이
        base_date = today_date
        base_time = "0500"
    elif now.hour <= 11 or (now.hour == 11 and now.minute <= 10):  # 8시 11분~11시 10분 사이
        base_date = today_date
        base_time = "0800"
    elif now.hour < 14 or (now.hour == 14 and now.minute <= 10):  # 11시 11분~14시 10분 사이
        base_date = today_date
        base_time = "1100"
    elif now.hour < 17 or (now.hour == 17 and now.minute <= 10):  # 14시 11분~17시 10분 사이
        base_date = today_date
        base_time = "1400"
    elif now.hour < 20 or (now.hour == 20 and now.minute <= 10):  # 17시 11분~20시 10분 사이
        base_date = today_date
        base_time = "1700"
    elif now.hour < 23 or (now.hour == 23 and now.minute <= 10):  # 20시 11분~23시 10분 사이
        base_date = today_date
        base_time = "2000"
    else:  # 23시 11분~23시 59분
        base_date = today_date
        base_time = "2300"

    API_key = 'P3bUz6M4vxsWYBAm5YVaV/IqweQMb34Dp20QoIb9Sqc4gCwq' \
              '7PLogxoTRZ7NZ9amV8hZMB4QyxAmpybBGz5vyA=='
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0' \
          '/getVilageFcst'
    nx,ny = ip_to_xy()
    queryParams = {'ServiceKey': API_key, 'numOfRows': '50',
                   'pageNo': '1', 'dataType': 'json',
                   'base_date': base_date,
                   'base_time': base_time, 'nx': nx, 'ny': ny}

    response = requests.get(url, queryParams)
    response_body = response.json()['response']['body']['items']['item']

    for body in response_body:
        if body['category'] == 'POP':
            result["강수확률"] = body['fcstValue']
        if body['category'] == 'PCP':
            result["1시간 강수량"] = body['fcstValue']
        if body['category'] == 'PTY':
            if (body['fcstValue']) == '0':
                result["강수형태"] = "없음"
            if (body['fcstValue']) == '1':
                result["강수형태"] = "비"

            if (body['fcstValue']) == '2':
                result["강수형태"] = "비/눈"

            if (body['fcstValue']) == '3':
                result["강수형태"] = "눈"

            if (body['fcstValue']) == '5':
                result["강수형태"] = "빗방울"

            if (body['fcstValue']) == '6':
                result["강수형태"] = "빗방울 눈날림"

            if (body['fcstValue']) == '7':
                result["강수형태"] = "눈날림"

    return result
