import json
import objectpath

with open('json.json') as f:
  data = json.load(f)
f.close()

jsonnn_tree = objectpath.Tree(data['suites'])

classes = []
durations = []

result_case = tuple(jsonnn_tree.execute('$..className'))
result_duration = tuple(jsonnn_tree.execute('$..duration'))

classes = list(result_case)
duration = list(result_duration)

print(classes)
