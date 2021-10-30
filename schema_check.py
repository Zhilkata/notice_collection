import jsonschema
from jsonschema import validate


def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=noticeSchema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


noticeSchema = {
    "type": "object",
    "additionalProperties": {
        "type": "object",
        "required": ["date", "number", "name", "procedure_state", "contract_type", "procurement_type",
                     "estimated_value"],
        "properties": {
            "date": {"type": "string"},
            "number": {"type": "string"},
            "name": {"type": "string"},
            "procedure_state": {"type": "string"},
            "contract_type": {"type": "string"},
            "procurement_type": {"type": "string"},
            "estimated_value": {"type": "string"},
        }
    }
}


def return_result(jsonData):
    isValid = validateJson(jsonData)
    return isValid