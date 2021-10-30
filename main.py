import json
import sys
import os

from collection.collection.spiders.collector import NoticeSpider
from scrapy.crawler import CrawlerProcess
from schema_check import return_result
from database_creation import create_database

# Request through spider
process = CrawlerProcess()
process.crawl(NoticeSpider)
process.start()

# Get needed data
try:
    with open('data.json', 'r') as file:
        items = json.load(file)
except FileNotFoundError:
    print("File not found! Terminating...")
    sys.exit()

valid_cases = {}
invalid_cases = []
for key in items:
    try:
        id = key['cNoticeId']
        date = key['noticeStateDate'].split("T")[0]
        number = key['noticeNo']
        name = key['contractingAuthorityNameAndFN'].split(" - ")[1]
        procedure_state = key['sysProcedureState']['text']
        contract_type = key['sysContractAssigmentType']['text']
        if key['isOnline']:
            procurement_type = "ONLINE"
        else:
            procurement_type = "OFFLINE"
        estimated_value = f"{key['estimatedValueRon']:,.2f}"
        valid_cases[id] = {'date': date, 'number': number, 'name': name, 'procedure_state': procedure_state,
                           'contract_type': contract_type,
                           'procurement_type': procurement_type, 'estimated_value': estimated_value}
    except:
        invalid_cases.append(key)

# Rewrite data JSON with processed data for debug purposes
createJson = False
if createJson:
    with open('data.json', 'w') as f:
        json.dump(valid_cases, f, indent=4)

# Access database after schema validation
# Check whether there are any entries at all.
isValid = return_result(valid_cases)
if isValid:
    createDatabase = False
    if createDatabase:
        create_database(valid_cases)

# Also catching rare case when valid JSON gets broken for some reason.
else:
    print("JSON integrity broken!")

# Invalid cases can be viewed manually here.
if len(invalid_cases) > 0:
    print("Invalid cases detected:")
    for case in invalid_cases:
        print(case)

# Cleanup of data.json
cleanup = True
if cleanup:
    if os.path.exists("data.json"):
        os.remove("data.json")
    else:
        print("File not found.")