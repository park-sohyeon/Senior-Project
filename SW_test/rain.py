from collections import defaultdict

import requests as requests

import nxny
from datetime import datetime, timedelta

from maps import ip_to_xy


def rain_check():
    result = defaultdict()
    now = datetime.now()

    if now.minute <= 40:
        # 단. 00:40분 이전이라면 `base_date`는 전날이고 `base_time`은 2300이다.
        if now.hour == 0:
            base_date = (now - timedelta(days=1)).strftime('%Y%m%d')
            base_time = '2300'
        else:
            base_date = now.strftime('%Y%m%d')
            base_time = (now - timedelta(hours=1)).strftime('%H00')
    # 40분 이후면 현재 시와 같은 `base_time`을 요청한다.
    else:
        base_date = now.strftime('%Y%m%d')
        base_time = now.strftime('%H00')
    # print(base_date, base_time)

    # API Set 1
    API_key = 'P3bUz6M4vxsWYBAm5YVaV/IqweQMb34Dp20QoIb9Sqc4gCwq7PLogxoTRZ7NZ9amV8hZMB4QyxAmpybBGz5vyA=='
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    # nx,ny = ip_to_xy()
    nx, ny = 61, 121
    queryParams = {'ServiceKey': API_key, 'numOfRows': '50', 'pageNo': '1', 'dataType': 'json', 'base_date': base_date,
                   'base_time': base_time, 'nx': nx, 'ny': ny}

    # API Call(For dustcheck)
    response = requests.get(url, queryParams)
    # request.get_method = lambda: 'GET'
    response_body = response.json()['response']['body']['items']['item']

    for body in response_body:
        if body['category'] == 'T1H':
            result["기온"] = body['obsrValue']


    for body in response_body:
        if body['category'] == 'REH':
            result["습도"] = body['obsrValue']

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
