name="masuda ryouta"
for character in name:
    print(character)

shows=["GOT","Narcos","Vice"]
for show in shows:
    print(show)

people={"G.Bluth II":"A.Development",
        "Barney":"HIMYM",
        "Dennis":"Always Sunny",
        }

for character in people:
    print(character)

#forループを使ってミュータブル（変更可能）なイテラブル（繰り返し可能な要素）を更新する（大文字化）
tv=["GOT","Narcos","Vice"]
#インデックス変数（要素の位置）
i=0
for show in tv:
    #newという変数にリストを取り出す
    new=tv[i]
    #new変数に.upper（大文字化）メソッドで結果をnewに再代入
    new=new.upper()
    #新しくなったnewの値でリストの元の値を書き換える為に、インデックス変数でリストの位置を指定して代入
    tv[i]=new
    #ループの最後にiをインクリメント（増加）して、次のループで扱う要素と、インデックス変数の値を合わせる
    i+=1


print(tv)#全然わからん・・・わかった

#各要素のインデックス値を自動的に用意してくれるenumerate関数を使う

tv=["GOT","Narcos","Vice"]
for i, new in enumerate(tv):
    new=tv[i]
    new=new.upper()
    tv[i]=new

print(tv)


#forループの中でデータを加工して別のリストに追加する。（このコードは大文字化）
tv=["GOT","Narcos","Vice"]
coms=["Arrested Development","friends","Always Sunny"]
all_shows=[]

for show in tv:
    show=show.upper()
    all_shows.append(show)

for show in coms:
    show=show.upper()
    all_shows.append(show)

print(all_shows)

