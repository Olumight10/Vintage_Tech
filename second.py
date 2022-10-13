given_strings = ["my string", "5 naira", "3books"]
output_boxes = [[], [], []]
update = 0
for i in given_strings:
  for j in i:
    try:
      j = int(j)
      if j < 4:
        output_boxes[update].append(j)
    except:
      if j != ' ' and type(j) is str:
        output_boxes[update].append(j)
  print(output_boxes[update])
  update += 1 
