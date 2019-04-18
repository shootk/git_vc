"""
c = "カミュ"
print(c[0])
print(c[1])
print(c[2])
main = "私の名前は{}です。年齢は{}です。"
name = input("What's your name:")
age = input("How old:")

main = main.format(name,age)
print(main)

words = "aldous Huxley was born in 1894"
words = words.capitalize()
print(words)

words2 = "だれが? どこで? いつ?"
my_list = words2.split(" ")
print(my_list)


words_list = ["The","fox","jumped","over","the","fence","."]
result = " ".join(words_list)
result = result.replace(" .",".")
print(result)


print("A screaming comes across the sky".replace("s","$"))

print("Hemingway".index("m"))


words = 'Please enjoy our "Safe" and "Comfortable" flight.'
print(words)

three = "three"+" "+"three"+" "+"three"
three_3 = "three "*3
three_3 = three_3[0:-1]
print(three)
print(three_3)

"""
w = "四月の晴れた寒い日で、時計がどれも十三時を打っていた"
n = w.index("、")
w = w[0:n]
print(w)
