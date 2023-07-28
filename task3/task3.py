import json
with open('tests.json', 'r') as tests_file:
    tests_data = json.load(tests_file)
with open('values.json', 'r') as values_file:
    values_data = json.load(values_file)
def fill_values(tests_data, values_data):
    if 'values' in tests_data:
        for test in tests_data['values']:
            for value in values_data:
                if test['id'] == value['id']:
                    test['value'] = value['value']
                    break
            fill_values(test, values_data)
fill_values(tests_data, values_data)
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)
