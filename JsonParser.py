import json
import objectpath

def openFile(file):
    with open(file) as f:
        data = json.load(f)
    f.close()
    return data

def extractInfo(data):
    jsonnn_tree = objectpath.Tree(data['suites'])

    classes = []
    durations = []

    result_case = tuple(jsonnn_tree.execute('$..className'))
    result_duration = tuple(jsonnn_tree.execute('$..duration'))
    result_name = tuple(jsonnn_tree.execute('$..name'))

    classes = list(result_case)
    duration = list(result_duration)
    name = list(result_name)
    
    duration.remove(duration[0])
    name.remove(name[0])
    
    print("result classname: " + str(len(classes)))
    print("result name: " + str(len(name)))
    print("result duration: " + str(len(duration)))
    
    print(classes[1] + " " + name[1] + " " + str(duration[1]))



data = openFile('json.json')
newData = extractInfo(data)

#for x, y in dictionary.items():
    #print(x,y)
