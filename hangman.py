import random
from hangman_words import word_list
from hangman_art import stages,logo
chosen_word=random.choice(word_list)
lives=len(chosen_word)
#Testing Code
print(f'The solution is {chosen_word}.')
print(logo)
#print(len(word_list))
#print(len(stages))
print(len(chosen_word))
display=[]
live=6
for i in range(len(chosen_word)):
    display.append("_")

while "_" in display:
    guess=input("Guess a letter: ").lower()
    
    for i in range(len(chosen_word)):
        letter=chosen_word[i]

        if letter==guess:
            display[i]=letter

    if guess not in chosen_word:
        lives-=1
        live-=1
        if lives==0:
            print("You Loose")
            exit(1)

    print(f"{' '.join(display)}")
    print(stages[live])

else:
    print("You have won")
            

        
