import json
import objectpath
import sys
import os.path

def openFile(file):
    with open(file) as f:
        data = json.load(f)
    f.close()
    
    return data
    
def createDictFromList(list1, list2):

    d = {}
    for k, v in zip(list1, list2):
        if k in d:
            d[k].append(v)
        else:
            d[k] = [v]

    return d

def getCommandArguments():
    
    print ('Enter The Files You Wish To Use', sys.argv, 'arguments.')
    list = []
    
    for i in sys.argv:
        os.path.exists(i)
        os.path.isfile(i)
        list.append(i)
        
    print(list)
    print ('Starting:', str(sys.argv))
    
    
    return list

def createDict(list1, list2):

    d = {}
    for k, v in zip(list1, list2):
            d[k] = v

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
    dictionary2 = createDict(name, duration)
    
    for k in dictionary.items():
        print(k)
        for k,v in dictionary2.items():
            print("     " + k +"/n   " +v)
    
    dictionary3 = (dictionary,dictionary2)
    
    return dictionary

def createJsonFile(dataFile):
    dataFile = (json.dumps([{'classname': k, 'values': v} for k,v in dataFile.items()], indent=4))
    with open('result.json', 'w') as fp:
        json.dump(dataFile, fp)

#data = openFile('json.json')
#newData = extractInfo(data)
#createJsonFile(newData)
#print("Done")

Files = getCommandArguments()

