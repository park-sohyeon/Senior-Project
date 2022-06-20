from collections import defaultdict
import requests

def dust_check():
    address_file = open("address.txt", "r", encoding="utf-8")
    sidoName = address_file.readline().strip()
    stationName = address_file.readline()

    API_key = 'P3bUz6M4vxsWYBAm5YVaV/IqweQMb34Dp20QoIb9Sqc4gCwq7PLogxoTRZ7NZ9amV8hZMB4QyxAmpybBGz5vyA=='
    url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
    queryParams = {'ServiceKey': API_key, 'returnType': 'JSON', 'numOfRows': '300',
                   'pageNo': '1', 'sidoName': sidoName,
                   'ver': '1.3'}
    response = requests.get(url, queryParams)
    response_body = response.json()['response']['body']['items']

    result = defaultdict()
    dust_type = ""

    for body in response_body:

        if ((body['stationName']).find(stationName)) == 0:
            result["sidoName"] = body['sidoName']
            result["stationName"] = body['stationName']
            result["pm10수치"] = body['pm10Value']


            if (body['pm10Grade1h']) == '1':
                    dust_type = "좋음"
            if (body['pm10Grade1h']) == '2':
                    dust_type = "보통"
            if (body['pm10Grade1h']) == '3':
                    dust_type = "나쁨"
            if (body['pm10Grade1h']) == '4':
                    dust_type = "매우 나쁨"

            result["pm2.5수치"] = body['pm25Value']

            if (body['pm25Grade1h']) == '1':
                    dust_type1 = "좋음"
            if (body['pm25Grade1h']) == '2':
                    dust_type1 = "보통"
            if (body['pm25Grade1h']) == '3':
                    dust_type1 = "나쁨"
            if (body['pm25Grade1h']) == '4':
                    dust_type1 = "매우 나쁨"

    result["10형태"] = dust_type
    result["2.5형태"] = dust_type1

    return result



if __name__ == '__main__':
    dust_check()