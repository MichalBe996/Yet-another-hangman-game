import random


list_of_words = ["spot", "cake", "wonder", "apparel", "mammoth", "middle", "leader",
                 "throne", "stroke", "spotless", "breathe", "act", "infamous"]

while True:
    lives = 3
    word = random.choice(list_of_words)
    list_from_word = list(word)
    for x in range(len(word)):
        list_from_word[x] = "_"
    print(" ".join(list_from_word))
    while lives >= 0:

        guess = input("Guess the letter: ")
        if guess not in word:
            print("WRONG!")
            lives -= 1
        elif guess in word:
            for x in range(len(word)):
                if guess == word[x]:
                    list_from_word[x] = guess

        print(" ".join(list_from_word))
        print("Lives left: ", lives)
        if guess == word:
            print("YOU WON!")
            break
        if lives == 0:
            print("YOU LOST")
            break
    cont = input("Do you want to play again? [Y/N]")
    if cont == "Y" or cont == "y":
        continue
    elif cont == "N" or cont == "n":
        print("Thank you, see you later!")
        break

