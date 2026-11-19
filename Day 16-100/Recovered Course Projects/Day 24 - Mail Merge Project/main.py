PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as name_file:
    names = name_file.readlines()
with open("./input/letters/starting_letter.txt") as letter_file:
    letters = letter_file.read()
for name in names:
    stripped_name = name.strip()
    letter = letters.replace(PLACEHOLDER, stripped_name)
    with (open(f"./output/ReadyToSend/"  f"letter_for_{stripped_name}.txt", "w")as completed_letter):
        completed_letter.write(letter)
