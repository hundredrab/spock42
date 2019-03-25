"""Simple module to get results from MAKAUT."""

import sys


def fetch_results(roll, sem):
    """Supply a 11-digit roll and a 1-digit semester value.

    Returns the corresponding response payload.
    """

    # import requests

    # cookies = {
    # 'XSRF-TOKEN': 'eyJpdiI6ImhyVHRxODBldVhRUGtCcFltSXc3eVE9PSIsInZhbHVlIjoiU29pTlwvTmNKUGU2VlIzUExMTytMTTNIaStKbndwRnp2c2FQYlorQ0ZWMG9MQUdWSnZsMHBtSGNQMTAzZGJHbURHRmtaQW5aM1hWem9abWhxU1paRUl3PT0iLCJtYWMiOiIyMGM1NTZjMmM1M2I5YmZiN2E1ZDM1NmRjY2FiYTFmZDI1NzE2MzUxZjk5ZmJjYTFmM2ZhZTE3ZDIxMmJkYTllIn0%3D',
    # 'examination_session': 'eyJpdiI6IkF1UGw3RldwSnpnSDRmN2Nkcm9BNFE9PSIsInZhbHVlIjoiRThsdE12eFcrZExwZDRCdWEwUWdQM3VzUmdzWnZhRmFGWFl4ZWdiTlEyK0RIZHlXNURcL3c3dWJpdDVPVW5IQ1wvM2NXWHZOZGhtZ0xyK2lPNTdDWlwvSGc9PSIsIm1hYyI6IjQ3ODU2ZTIzNTNkMjFhNmFlYTVjNDAzMTFkMTg0NTQyOWM0YTg0NzkzMTBmNTI5ZGZjYWI5YWJkNTc1NmNjMWEifQ%3D%3D',
    # }
    # headers = {
    # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Language': 'en-US,en;q=0.5',
    # 'Referer': 'https://makaut.ucanapply.com/smartexam/public/result-details',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # # 'X-CSRF-TOKEN': 'adLWtsloK2nY6xX1J0bLsPrTbNRpXcBpWBdEtUVm',
    # # 'X-Requested-With': 'XMLHttpRequest',
    # 'DNT': '1',
    # 'Connection': 'keep-alive',
    # 'Upgrade-Insecure-Requests': '1',
    # }

    # data = {
    # '_token': 'uVOoESG1ggHcTvBpphH95ybguZojThbTqWN8x3bs',
    # 'p1': '',
    # 'ROLLNO': str(roll),
    # 'SEMCODE': 'SM0'+str(sem),
    # 'examtype': 'result-details',
    # 'all': ''
    # }

    # response = requests.post('https://makaut.ucanapply.com/smartexam/public/result-details',
    #                          headers=headers, cookies=cookies, data=data)

    import requests

    cookies = {
        'examination_session': 'eyJpdiI6IlpcL2NpV0lHSDBZUkNIdmd0UStmOERnPT0iLCJ2YWx1ZSI6IkphY3l2OXJYM1kyWk1nelcwakNJMjgyd2ladUpXblNQVUl5S0l4cU9mNk9VelZ5VVBSMmlSOHZBNjlLUGM3YXBNSkJyZzhVV01JUHhMSEZQNTI4N2xRPT0iLCJtYWMiOiJlMGYxNjNiZmVmZjVlZDRiNmM1NTcxYTYzMGJkY2FlYTM5MGZhMjYxMDBhZjkxYWNiNzY5Y2E0MWIxNzIxNzUxIn0%3D', 'XSRF-TOKEN': 'eyJpdiI6IlJcL2V6d1BEVHRjZXhSTm5Hc2RxUGdRPT0iLCJ2YWx1ZSI6IlR0K3lpVFwvS1lhOFUrR0RnWXV5ZFBwQkZkXC9IOGFuZ0M4d092Yzh1S3Fid1JMZitwVU9ZRVEraXdnMGx3c1wvcFwvYnF4YzdzYmdjSXY5Ukg3aXc3RmdDUT09IiwibWFjIjoiYzEwMTM3NGIzOTY1MTA2NDcyZGI0ODhiMjdlNGY1MGZiOWI3ZDA5NWRmZDFjNDYxMmM2YmNiMTA0OTQxNzg4YyJ9'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://makaut.ucanapply.com/smartexam/public/result-details',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-CSRF-TOKEN': 'KwHpVNgXXrDPRqKcbYJNk6vRWrjNiP33Q7qXMKsn',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    data = {
        '_token': '4jFerFGEx1sBIsLsnSOzPqv0T9Rcrio3SAq7QIlV',
        'p1': '',
        'ROLLNO': str(roll),
        'SEMCODE': 'SM0' + str(sem),
        'examtype': 'result-details',
        'all': ''
    }

    response = requests.post('https://makaut.ucanapply.com/smartexam/public//get-result-details',
                             headers=headers, cookies=cookies, data=data)

    if '200' in str(response):
        print("Success")
        print("Response: " + response.text[:100] + "...")
        with open("res_{}_0{}.html".format(roll, sem), 'w') as f:
            f.write(response.json()['html'])
    else:
        print(response)
    return str(response)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("Tryna get particular result: " + sys.argv[1])
        while True:
            try:
                if '200' in fetch_results(sys.argv[1], 7):
                    print("Done: " + sys.argv[1])
                    break
            except Exception as e:
                print(e)
        exit()
    for i in range(10200116001, 10200116016):
        print("Trying for: ", i)
        while True:
            try:
                if '200' in fetch_results(i, 7):
                    print("Done: ", i)
                    break
            except Exception as e:
                print(e)
