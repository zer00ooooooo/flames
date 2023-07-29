#  FLAMES CANDLE
import re

print("*"*20, "FLAMES CANDLE", "*"*20)
print("")

name_1 = input("ENTER YOUR NAME: \t\t\t")
name_2 = input("ENTER YOUR CRUSH'S NAME: \t")

name1 = re.sub("\s", "", name_1.upper())
name2 = re.sub("\s", "", name_2.upper())

alike = []
for x in name1:
    if x in name2:
        alike.append(x)

alike_2 = []
for y in name2:
    if y in name1:
        alike_2.append(y)

total_alike_letters = len(alike) + len(alike_2)
print("")
print(f"{name_1} x {name_2} = {total_alike_letters}")


def flames_candles(val):
    meanings = ["FRIENDS", "LOVERS", "ANGER", "MARRIAGE", "ENGAGEMENT", "SOULMATES"]
    length = len(meanings)
    if val <= length:
        print(meanings[val - 1])
    else:
        while val != length:
            for count, m in enumerate(meanings, length + 1):
                length += 1
                if val == count:
                    print(m)
                    break


flames_candles(total_alike_letters)
