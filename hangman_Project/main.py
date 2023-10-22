import random
import word_list
import hangman_stages
def changer(original_word, final_ans, from_user_letter):
    for i in range (len(original_word)):
        if original_word[i] == from_user_letter:
            final_ans[i] = from_user_letter
    return final_ans

chosen_word = random.choice(word_list.list_of_word)
print(chosen_word)
print(hangman_stages.logo)

final_ans = []

for i in range (len(chosen_word)):
    final_ans.append('_')

counter = 6

while counter != -1:
    letter_from_user = input("What letter you will choose?").lower()
    changer(chosen_word, final_ans, letter_from_user)
    print(final_ans)
    if letter_from_user in chosen_word:
        print("Right!")
    elif letter_from_user not in chosen_word:
        print(hangman_stages.stages[counter])
        counter -= 1
        if counter == -1 :
            print("You are loooooooser")
    if '_' not in final_ans:
        print("You are amazing")
        break
