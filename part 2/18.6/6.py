import json
import os

def compare_json_objects(old_obj, new_obj, diff_list):
    result = {}
    for key in diff_list:
        if key in old_obj and key in new_obj and old_obj[key] != new_obj[key]:
            result[key] = new_obj[key]
    return result

path = os.path.dirname(os.path.abspath(__file__))
old_json_path = os.path.join(path, 'json_old.json')
new_json_path = os.path.join(path, 'json_new.json')
result_path = os.path.join(path, 'result.json')


with open(old_json_path, 'r') as old_file, open(new_json_path, 'r') as new_file:
    json_old = json.load(old_file)
    json_new = json.load(new_file)

diff_list = ['services', 'staff', 'datetime']

result = compare_json_objects(json_old, json_new, diff_list)

print(result)

with open(result_path, 'w') as result_file:
    json.dump(result, result_file, indent=2)
