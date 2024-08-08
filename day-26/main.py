import pandas

nato_alpbt = "day-26/nato_phonetic_alphabet.csv"
data = pandas.read_csv(nato_alpbt)
#dF = pandas.DataFrame(data)

alpbt_dict = {row.letter:row.code for (index, row) in data.iterrows()}

name = input("Enter a name: ").upper()
new_n = [x for x in name]

final_list = [alpbt_dict[letter] for letter in new_n]

print(final_list)