#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
placeholder = "[name]"

with open("Mail Merge Project/Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()
    # print(names)

with open("Mail Merge Project/Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip() # this works for /n, which is what we need it to work for
        # print(stripped_name)
        new_letter = letter_contents.replace(placeholder, stripped_name)
        # print(new_letter)
        with open(f"Mail Merge Project/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter) 