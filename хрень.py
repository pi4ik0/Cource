with open('quotes.txt',"r", encoding="UTF-8") as file:
    for line in file:
        print(line)

author = input("XTo HanucaB Li pAAK?")

with open('quotes.txt', "a", encoding="UTF-8") as file:
    file.write(f"({author})\n")


while True:
    answer = input("baxaete AonaT ue AHY LWTaTy?(TaK / Hi)")

    answer = answer.lower()
    if answer =="tak":
        quote = input("BBeAiTb LWTaTy:")
        author = input("BBeAiTb aBTopa:")
        file = open("quotes.txt","a",encoding="UTF-8")
        file.write(f"{quote}\n({author})\n")
        file.close()
    else:
        break
with open('quotes.txt', "r", encoding="UTF-8") as file:
    for line in file:
        print(line)
