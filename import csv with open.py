import csv
import os

#csvファイルを書き込む

with open("st.csv","w",newline='') as f :
          w = csv.writer(f,delimiter=",")
          w.writerow(["one","two","three","unti"]) #一行目
          w.writerow(["four","five","six","buriburi"]) #二行目
          
print(os.getcwd())#ファイルがどこに書き込まれたか

#csvファイルを読み込む

with open("st.csv","r") as f :
          r = csv.reader(f,delimiter=",")
          for row in r:　#forループで取り出して,を付けて結合している
              print(",".join(row))
        
