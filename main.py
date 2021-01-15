import pandas

#  Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# read csv
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
# print(data.to_dict())
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# print(data_dict)
# Create a list of the phonetic code words from a word that the user inputs.
# we will do list comprehension
# [new_item for letter in word]

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [data_dict[wordGiven] for wordGiven in word]
    except KeyError:
        print("Only letters allowed")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
