import json
import jsonschema
from jsonschema import validate
from b_clean import cleanJson


## valid schema
validSchema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "source": {
      "type": "string"
    },
    "destination": {
      "type": "string"
    },
    "timeout": {
      "type": "integer",
      "minimum": 0,
      "maximum": 32767
    },
    "chunks": {
      "type": "object",
      "properties": {
        "size": {
          "type": "integer"
        },
        "number": {
          "type": "integer"
        }
      },
      "required": ["size"]
    }
  },
  "required": ["source", "destination"]
}

## match provided json to valid schema
def validateJson(sample):
    try:
        validate(instance=sample, schema=validSchema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        return False

## function only utlised for testing sample data
def testValidate():
    f = open('storage/config.json')
    sample = json.load(f)
    sample = cleanJson(sample)

    isValid = validateJson(sample)
    print(isValid)

#testValidate()
