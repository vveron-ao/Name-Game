#List assignments
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 
                     'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'q', 'x', 'y', 'z']
name = []

#Variable assignment
x = str(input("What is your name? "))
name.append(x)
first_letter = name[0][0] if name[0][0] not in ["'", '’'] else name[0][1]
second_letter = name[0][1] if name[0][1] not in ["'", '’'] else name[0][2]
third_letter = name[0][2] if name[0][2] not in ["'", '’'] else name[0][3]
lower_vow_name = x.lower()
consonant_count1 = consonants.count(first_letter)
consonant_count2 = consonants.count(second_letter)
consonant_count3 = consonants.count(third_letter)
consonant_total = consonant_count1 + consonant_count2

#Initialize variable for when the amount of consonants is 2 or greater.
if consonant_count2 >= 1:
    consonant_total = consonant_count1 + consonant_count2 + consonant_count3

#If name begins with a vowel, run this code.
for vowel_name in (vowels):
    if first_letter == vowel_name:
        print(f'{x}, {x}, Bo-B{lower_vow_name}\nBanana-Fana Fo-F{lower_vow_name}\nMe Mi Mo-M{lower_vow_name}\n{x}!')
        break 

#If name doesn't begin with a vowel, run this code.
else:
    for consonant_name in (consonants):
    #If name has one consonant, run this code.
        if consonant_total == 1:
            one_consonant_name = name[0][1:]
            print(f'{x}, {x}, Bo-B{one_consonant_name}\nBanana-Fana Fo-F{one_consonant_name}\nMe Mi Mo-M{one_consonant_name}\n{x}!')
            break

    #If name has two consonants, run this code.
        elif consonant_total == 2:
            two_consonant_name = name[0][2:]
            print(f'{x}, {x}, Bo-B{two_consonant_name}\nBanana-Fana Fo-F{two_consonant_name}\nMe Mi Mo-M{two_consonant_name}\n{x}!')
            break
    
    #If name has more than 2 consonants, run this code.
        elif consonant_total > 2:
            three_consonant_name = name[0][3:]
            print(f'{x}, {x}, Bo-B{three_consonant_name}\nBanana-Fana Fo-F{three_consonant_name}\nMe Mi Mo-M{three_consonant_name}\n{x}!')
            break
