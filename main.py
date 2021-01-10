import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# read csv
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
# print(data.to_dict())
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(data_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
# we will do list comprehension
# [new_item for letter in word]
output_list = [data_dict[wordGiven] for wordGiven in word]
print(output_list)
