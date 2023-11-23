PLACEHOLDER = "[name]"

with open("mail_names.txt") as names_file:
    names = names_file.readlines()  # readlines returns a list

with open("/Users/User/Desktop/letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()  # strip cancel spaces
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)  # replace changes content of sth to another
        with open(f"/Users/User/Desktop/letter_for_{stripped_name}.txt", 'w') as completed_letter:
            completed_letter.write(new_letter)
