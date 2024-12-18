#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Defines a placeholder(string) that will be replaced with actual names in the letter template
PLACEHOLDER = "[name]"

#Opens the file that contains a list of invited names and read all the lines.
#Each line in the file corresponds to a name
with open("file_merge_stuff/Input/Letters/Names/invited_names.txt") as names_file: 
    names = names_file.readlines() #Reads all the names into a list, where each item is a name string

#Opens file that contains ste starting letter template and read its content
with open("file_merge_stuff/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read() #Read the entire template letter into a single string
    #Iterate over each name in the list of names
    for name in names:
        stripped_name = name.strip() #Removes any trailing whitespace from name
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name) #Replace placeholder in the letter template with current name
        #Create new file for completed letter addressed to the current name
        with open(f"file_merge_stuff/Output/ReadyToSend/Letter_for_{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(new_letter) #Writes personalized letter content to the new file
