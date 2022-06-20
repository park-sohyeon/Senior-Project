from collections import defaultdict
import requests as requests
from datetime import datetime, timedelta
from maps import ip_to_xy

def rain_check():
    result = defaultdict()
    now = datetime.now()

    if now.minute <= 40:
        # 단. 00:40분 이전이라면 `base_date`는 전날, `base_time`은 2300
        if now.hour == 0:
            base_date = (now - timedelta(days=1)).strftime('%Y%m%d')
            base_time = '2300'
        else:
            base_date = now.strftime('%Y%m%d')
            base_time = (now - timedelta(hours=1)).strftime('%H00')
    # 40분 이후면 현재 시와 같은 `base_time`을 요청
    else:
        base_date = now.strftime('%Y%m%d')
        base_time = now.strftime('%H00')
    # print(base_date, base_time)


    API_key = 'P3bUz6M4vxsWYBAm5YVaV/IqweQMb34Dp20QoIb9Sqc4gCwq' \
              '7PLogxoTRZ7NZ9amV8hZMB4QyxAmpybBGz5vyA=='
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0' \
          '/getUltraSrtNcst'
    nx,ny = ip_to_xy()

    queryParams = {'ServiceKey': API_key, 'numOfRows': '50',
                   'pageNo': '1', 'dataType': 'json',
                   'base_date': base_date,
                   'base_time': base_time, 'nx': nx, 'ny': ny}

    response = requests.get(url, queryParams)
    response_body = response.json()['response']['body']['items']['item']

    for body in response_body:
        if body['category'] == 'RN1':
            result["강수량"] = body['obsrValue']
    rain_type = ""
    for body in response_body:
        if body['category'] == 'PTY':
            if (body['obsrValue']) == '0':
                rain_type = "없음"

            if (body['obsrValue']) == '1':
                rain_type = "비"

            if (body['obsrValue']) == '2':
                rain_type = "비/눈"

            if (body['obsrValue']) == '3':
                rain_type = "눈"

            if (body['obsrValue']) == '5':
                rain_type = "빗방울"

            if (body['obsrValue']) == '6':
                rain_type = "빗방울 눈날림"

            if (body['obsrValue']) == '7':
                rain_type = "눈날림"
    result["형태"] = rain_type
    return result
