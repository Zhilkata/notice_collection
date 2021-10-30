import requests
from datetime import date


def collect():
    year = date.today().year
    month = date.today().month
    day = date.today().day - 1

    URL = "http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/"
    headers = {'Accept': "application/json, text/plain, */*",
               'Content-Type': "application/json;charset=UTF-8",
               'Referer': "http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1",
               'Host': 'www.e-licitatie.ro',
               'Connection': 'keep-alive',
               'Authorization': 'Bearer null',
               'Accept-Encoding': "gzip, deflate",
               'Cookie': "_HttpSessionID=88FC1C590C1247FC926CBE9669D6A7DF; "
                         "sysNoticeTypeIds=null; culture=en-US; isCompact=true",
               'Origin': "http://www.e-licitatie.ro"
               }
    payload = {"sysNoticeTypeIds": [2], "sortProperties": [], "pageSize": 5000,
               "hasUnansweredQuestions": 'false', "startPublicationDate": f"{year}-{month}-{day}T21:00:00.000Z",
               "sysProcedureStateId": 'null', "pageIndex": 0,
               "endPublicationDate": f"{year}-{month}-{day}T21:00:00.000Z"}

    res = requests.post(url=URL, headers=headers, json=payload)
    items = res.json()['items']
    return items