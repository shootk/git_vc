#charenge7
"""
#1
movie = ["ウォーキング・デッド","アントラージュ",
         "ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]

for show in movie:
    print(show)

#2
for i in range(25,51):
    print(i)

#3
movie = ["ウォーキング・デッド","アントラージュ",
         "ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]

for i,show in enumerate(movie):
    print(i,":",show)

#4
right = (7,10,11,21)
while True:
    num = input("Input num/if you quit input q:")
    if(num == "q"):
        break;
    else:
        try:
            if(int(num) in right):
                print("Right!")
            else:
                print("Fuck off")
        except ValueError:
            print("Input nunber")
print("See you")

#5
n1 = [8,19,148,4]
n2 = [9,1,33,83]
result = []

for i in n1:
    for j in n2:
        result.append(str(i)+"*"+str(j)+":"+str(i*j))

print(result)
"""
