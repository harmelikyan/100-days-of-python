#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(data)
alphabet_to_dict = {row.letter: row.code for (index,row) in data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Please enter a word: ").upper()
output_list = [alphabet_to_dict[letter] for letter in word]
print(output_list)

