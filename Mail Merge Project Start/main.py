starting_letter = open("Input/Letters/starting_letter.txt")
invited_names = open("Input/Names/invited_names.txt")


letter = starting_letter.read().strip()
inv = invited_names.readlines()
for i in inv:
    file = open(f"Output/ReadyToSend/letter_for_{i[:-1]}", mode="w")
    file.write(letter[0:5] + i[:-1] + letter[11:])
    file.close()
