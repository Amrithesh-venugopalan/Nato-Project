import pandas
nato_data=pandas.read_csv("../Desktop/python codes/NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_dataframe=pandas.DataFrame(nato_data)
# print(nato_dataframe)

nato_dict={}
for (index,row) in nato_dataframe.iterrows():
    nato_dict[f"{row.letter}"]=f"{row.code}"
# print(nato_dict)
def natolize():
    word=input("enter the word you want to natolize :\n")
    try:
        word_list=[letter.upper() for letter in word]
        for i in word_list:
            if i==" ":
                word_list.remove(i)
        nato_list=[nato_dict[letter] for letter in word_list]
        print(nato_list)
    except KeyError:
        print("sorry,only letters allowed in alphabet")
        natolize()
natolize()