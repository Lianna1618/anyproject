import json
from jsonschema import validate, ValidationError
from schema_val import ExpectedSchema

# Load JSON data from file
with open("data.json", "a") as file:
    json_data = json.load(file)

# Validate JSON data against the schema
try:
    validate(instance=json_data, schema=ExpectedSchema())
    print("Validation passed!")
except ValidationError as e:
    print(f"Validation failed: {e}")
    exit()

# Parse JSON and print the data
club_name = json_data["club_name"]
club_country = json_data["club_country"]
club_value = json_data["club_value"]
club_owner = json_data["club_owner"]
club_president = json_data["club_president"]
club_manager = json_data["club_manager"]

print(f"Club_name: {club_name}")
print(f"Club Country: {club_country}")
print(f"Club Value: {club_value}")
print(f"Club Owner: {club_owner}")
print(f"Club President: {club_president}")
print(f"Club Manager: {club_manager}")

