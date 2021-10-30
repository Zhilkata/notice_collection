import scrapy
import json
from datetime import date

year = date.today().year
month = date.today().month
day = date.today().day - 1


class NoticeSpider(scrapy.Spider):
    name = 'collector'
    allowed_domains = ['e-licitatie.ro']
    start_urls = ['http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1']

    def parse(self, response):
        url = 'http://www.e-licitatie.ro/api-pub/NoticeCommon/GetCNoticeList/'
        headers = {'Accept': "application/json, text/plain, */*",
                   'Content-Type': "application/json;charset=UTF-8",
                   'Referer': "http://www.e-licitatie.ro/pub/notices/contract-notices/list/2/1",
                   'Host': 'www.e-licitatie.ro',
                   'Connection': 'keep-alive',
                   'Authorization': 'Bearer null',
                   'Accept-Encoding': "gzip, deflate",
                   'Cookie': "_HttpSessionID=88FC1C590C1247FC926CBE9669D6A7DF; "
                             "sysNoticeTypeIds=null; culture=en-US; isCompact=true",
                   'Origin': "http://www.e-licitatie.ro"}
        cookies = {"sysNoticeTypeIds": "null", "culture": "en-US", "isCompact": "true"}
        payload = {"sysNoticeTypeIds": [2], "sortProperties": [], "pageSize": 5000,
                   "hasUnansweredQuestions": 'false', "startPublicationDate": f"{year}-{month}-{day}T21:00:00.000Z",
                   "sysProcedureStateId": 'null', "pageIndex": 0,
                   "endPublicationDate": f"{year}-{month}-{day}T21:00:00.000Z"}

        yield scrapy.Request(url, method="POST", body=json.dumps(payload), headers=headers, cookies=cookies,
                             callback=self.parse_entry)

    def parse_entry(self, response):
        items = json.loads(response.text)['items']
        with open('./data.json', 'w') as file:
            json.dump(items, file, indent=4)