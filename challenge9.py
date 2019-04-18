#challenge9
"""
#1
import getpath
filename
path =getpath.join("C:","Users","a1514","OneDrive","デスクトップ","3年生課題.txt")
with open(path,"r",encoding = "cp932")as f:
    print(f.read())
print(path)


#2
answer = input("What your name?")
with open("answer.txt","w+",encoding = "utf-8") as f:
    f.write(answer)

#3
import csv
ml = [["Top Gun","RiskyBusiness","Minority Report"],
      ["Titanic","The revenant","Incption"],
      ["Training Day","Man on Fire","Flight"]]
with open("muvie.csv","w",newline = "",encoding = "utf-8") as f:
    w = csv.writer(f,delimiter = ",")
    for m in ml:
        w.writerow(m)
"""
#4
import csv
ml = [["トップガン","リスキービジネス","マイノリティーレポート"],
      ["タイタニック","ザ・レヴェナント","インセプション"],
      ["トレーニング　デイ","マン　オン　ファイア","フライト"]]
with open("muvie.csv","w",newline = "",encoding = "cp932") as f:
    w = csv.writer(f,delimiter = ",")
    for m in ml:
        w.writerow(m)
