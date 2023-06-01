import json

# Deserialize JSON into objects
with open('sample.json', 'r') as file:
    data = json.load(file)

# cut
size = 100
last_image_id = data['images'][:size][-1]['id']
annotations=data['annotations']
selected_annotations =[]

for x in annotations:
  if x['image_id']<last_image_id:
    selected_annotations.append(x)

selected_data=data.copy()
selected_data.update({'images': data['images'][:size]})
selected_data.update({'annotations': selected_annotations})


# Store selected data in a separate JSON file
with open('output.json', 'w') as file:
    json.dump(selected_data, file)