"""Simple module to get results from MAKAUT."""


def fetch_results(roll, sem):
    """Supply a 11-digit roll and a 1-digit semester value.

    Returns the corresponding response payload.
    """

    import requests

    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IndVOXJsYlJVeTEzUWxvS0p0USt4c1E9PSIsInZhbHVlIjoiVzh1Zm5ybU9oRm5CUFNQdk9QNHpLSGt1UXdWTnRRMU16NlU5akdwek9sZTZnZk55bVBGY2xkWlpGZ1hpZ0pYZFBYU0hGc1wvNXRRWTh1MnNkOFBDek9BPT0iLCJtYWMiOiJhMWMyMzc2MDhkZjJlYTA3OWU2MDBjZjliNTRkNzdiYWEyOGFhNzUwNjk0OTljODRmODJjMmJlOGJjMjQ2YWFkIn0%3D',
        'examination_session': 'eyJpdiI6InZwZTNWNVpRRjdSaW9icEcyNmhlc3c9PSIsInZhbHVlIjoiV0VBb1hydTJQc1NwVUdtRDV4OXo3RjA0RmJhend3c2pQbm43dXNxREc0dm9xR0JNY0YrbVNNbXh2aU52ZkZCNjBsNUVKYm9TSFljalIzWFV6QjBiS0E9PSIsIm1hYyI6IjJiOTg4ODBmZjJlZDFkMjI4MDIwMjIzNDU5NWRlNzQ1NGVkMWI0NzMwMzhkN2EzZjA1Y2E4MDZlOWE5YzdlMTgifQ%3D%3D',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://makaut.ucanapply.com/smartexam/public/result-details',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-CSRF-TOKEN': 'PeVqDxh9ALuh7hqwd1H7dSviIwUMli72E3XXBi6u',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    data = {
        '_token': 'PeVqDxh9ALuh7hqwd1H7dSviIwUMli72E3XXBi6u',
        'p1': '',
        'ROLLNO': str(roll),
        'SEMCODE': 'SM0'+str(sem),
        'examtype': 'result-details',
        'all': ''
    }

    response = requests.post('https://makaut.ucanapply.com/smartexam/public//get-result-details',
                             headers=headers, cookies=cookies, data=data)
    if '200' in str(response):
        print("Success")
        print("Response: " + response.text[:100] + "...")
        with open("res_{}_0{}.json".format(roll, sem), 'w') as f:
            f.write(response.text)
    else:
        print(response)


if __name__ == '__main__':
    fetch_results(00000000000, 6)
