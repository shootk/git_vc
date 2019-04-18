wordlist = ["apple","mujic","magic","words","class",
            "homes","lover","shoot","games","dream",
            "king","child","human","black"]
import random

def hangman(word):
    wrong = 0
    stages = ["",
              "______        ",
              "|     |       ",
              "|     |       ",
              "|     O       ",
              "|     A       ",
              "|     A       ",
              "|             "
              ]
    rletterts = list(word)
    board = ["_"]*len(word)
    win = False
    print("ハングマンへようこそ")

    while wrong < len(stages) -1:
        print("\n")
        mag = "1文字を予想してね"
        char = input(mag)
        if char in rletterts:
            cind = rletterts.index(char)
            board[cind] = char
            rletterts[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong +1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break
    if win == False:
        print("あなたの負け\n正解は{}".format(word))
        print("\n".join(stages))

hangman(str(wordlist[random.randint(0,len(wordlist))]))
