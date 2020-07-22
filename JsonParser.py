import json
import objectpath

def openFile(file):
    with open(file) as f:
        data = json.load(f)
    f.close()
    
    return data
    
def createDict(list1, list2):

    d = {}
    for k, v in zip(list1, list2):
        if k in d:
            d[k].append(v)
        else:
            d[k] = [v]

    return d

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
    
    rangeItems = len(classes)
    newData = []
    
    for i in range(0,rangeItems):
        newData.append("name:" + name[i]+ " duration:" + str(duration[i]))
        
    dictionary = createDict(classes, newData)
    
    return dictionary

def createJsonFile(dataFile):
    dataFile = (json.dumps([{'classname': k, 'values': v} for k,v in dataFile.items()], indent=4))
    with open('result.json', 'w') as fp:
        json.dump(dataFile, fp)

data = openFile('json.json')
newData = extractInfo(data)
createJsonFile(newData)
print("Done")
