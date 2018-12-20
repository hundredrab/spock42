"""Simple module to get results from MAKAUT."""

import subprocess

def fetch_results(roll, sem):
    """Supply a 11-digit roll and a 1-digit semester value.

    Returns the corresponding response payload.
    """
    cmd = "curl 'https://makaut.ucanapply.com/smartexam/public//get-result-details' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://makaut.ucanapply.com/smartexam/public/result-details' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-CSRF-TOKEN: PeVqDxh9ALuh7hqwd1H7dSviIwUMli72E3XXBi6u' -H 'X-Requested-With: XMLHttpRequest' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: XSRF-TOKEN=eyJpdiI6IndVOXJsYlJVeTEzUWxvS0p0USt4c1E9PSIsInZhbHVlIjoiVzh1Zm5ybU9oRm5CUFNQdk9QNHpLSGt1UXdWTnRRMU16NlU5akdwek9sZTZnZk55bVBGY2xkWlpGZ1hpZ0pYZFBYU0hGc1wvNXRRWTh1MnNkOFBDek9BPT0iLCJtYWMiOiJhMWMyMzc2MDhkZjJlYTA3OWU2MDBjZjliNTRkNzdiYWEyOGFhNzUwNjk0OTljODRmODJjMmJlOGJjMjQ2YWFkIn0%3D; examination_session=eyJpdiI6InZwZTNWNVpRRjdSaW9icEcyNmhlc3c9PSIsInZhbHVlIjoiV0VBb1hydTJQc1NwVUdtRDV4OXo3RjA0RmJhend3c2pQbm43dXNxREc0dm9xR0JNY0YrbVNNbXh2aU52ZkZCNjBsNUVKYm9TSFljalIzWFV6QjBiS0E9PSIsIm1hYyI6IjJiOTg4ODBmZjJlZDFkMjI4MDIwMjIzNDU5NWRlNzQ1NGVkMWI0NzMwMzhkN2EzZjA1Y2E4MDZlOWE5YzdlMTgifQ%3D%3D' --data '_token=PeVqDxh9ALuh7hqwd1H7dSviIwUMli72E3XXBi6u&p1=&ROLLNO={}&SEMCODE=SM0{}&examtype=result-details&all=' > {}_{}.json".format(roll, sem, roll, sem)

    print(cmd)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = proc.communicate()

if __name__=='__main__':
    fetch_results(00000000000, 6)
