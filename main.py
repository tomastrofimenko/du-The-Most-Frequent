def most_frequent(zoznam:list):
  pomzoz = []
  finalzoz = []
  for i in zoznam:
    pomzoz.append(zoznam.count(i))
  for i in pomzoz:
    if i == max(pomzoz):
      finalzoz.append(zoznam[pomzoz.index(i)])

  return finalzoz

print(most_frequent(["a", "b", "a", "a", "c", "b"]))  

