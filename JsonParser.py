import json
import objectpath

def openFile(file):
    with open(file) as f:
        data = json.load(f)
    f.close()
    return data

def createDictionary(data):
    jsonnn_tree = objectpath.Tree(data['suites'])

    classes = []
    durations = []

    result_case = tuple(jsonnn_tree.execute('$..className'))
    result_duration = tuple(jsonnn_tree.execute('$..duration'))

    classes = list(result_case)
    duration = list(result_duration)

    duration.remove(duration[0])

    name_value_tuples = zip(classes, duration)
    name_to_value_dict = {}
    for key, value in name_value_tuples:
        if key in name_to_value_dict:
            pass
        else:
            name_to_value_dict[key] = value

    return name_to_value_dict



data = openFile('json.json')
dictionary = createDictionary(data)

for x, y in dictionary.items():
    print(x,y)
