import json
from schema_check import return_result
from database_creation import create_database
from collect_method import collect

# Make API request, get list
items = collect()

# Get needed data
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

# Create JSON file for debug purposes
createJson = False
if createJson:
    with open('debug.json', 'w') as f:
        json.dump(valid_cases, f, indent=4)

# Access database after schema validation
# Check whether there are any entries at all.
isValid = return_result(valid_cases)
if isValid:
    createDatabase = True
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