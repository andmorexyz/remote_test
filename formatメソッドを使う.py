#formatメソッドを使って入力してもらった文字を使う

what=input("何が:")
when=input("いつ:")
where=input("どこで:")
do=input("どうした:")

r="{}は{}に{}で{}。".format(what,when,where,do)
print(r)
