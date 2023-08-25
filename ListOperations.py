
data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]

color_data = ['brown', 'blue', 'green', 'black']

total = 0
total_color = 0
totalpercentage = 0
choose_your_color = input("Choose your color (brown/blue/green/black): ")
index_color = -1

if choose_your_color not in color_data:
  print("Invalid eye color choice.")
else:
  if choose_your_color == 'brown':
    index_color += 1
  elif choose_your_color == 'blue':
    index_color += 2
  elif choose_your_color == 'green':
    index_color += 3
  elif choose_your_color == 'black':
    index_color += 4

  for i in data:
    for k in i:
      total = total + k
      
  for j in data:
    total_color = total_color + j[index_color]

  if(total != 0):
    totalpercentage = (total_color / total) * 100
    print(int(totalpercentage))
  else:
    print("No data available.")

