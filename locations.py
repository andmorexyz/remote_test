#リストの要素にタプルを持たせている

locations=[]

la=(34.0522,188.2437)
chicago=(41.8781,87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

#タプルの要素にリストを持たせている

eights=["Edgar Allan Poe","Charles Dickens"]
nines=["Hemingway","Fitzgerald","Orwell"]

authors=(eights,nines)
print(authors)

#リストやタプルの要素に辞書を持たせる事も出来る

#これは辞書
bday={"Hemingway":"7.21.1899",
      "Fitzgerald":"9.24.1896"}

#これはリスト
my_list=[bday]
print(my_list)
#これはタプル
my_tuple=(bday,)
print(my_tuple)


