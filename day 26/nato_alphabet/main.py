import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_to_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Please enter a word: ").upper()
    try:
        output_list = [alphabet_to_dict[letter] for letter in word]
    except KeyError:
        print("No numbers")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
