print("This is a program where it replaces vowels with *.")
user_input = input("Input a sentence, phrase, or word: ")

input_to_list_and_final_output = str(list(user_input))


print("You entered : " + input_to_list_and_final_output)

input_to_list_and_final_output.replace("a", "*")
input_to_list_and_final_output.replace("e", "*")
input_to_list_and_final_output.replace("i", "*")
input_to_list_and_final_output.replace("o", "*")
input_to_list_and_final_output.replace("u", "*")

final_output = str(input_to_list_and_final_output)
vowels_replaced = 0
for vowel in final_output:
    if vowel == "*":
        vowels_replaced += 1


print("The final output is: " + final_output)
print("The number of vowels replaced is: " + str(vowels_replaced))
