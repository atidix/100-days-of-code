#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names = []

with open("day-24/Input/Names/invited_names.txt") as name:
    names = name.readlines()

new_names = []

for person in names:
    person = person.strip()
    new_names.append(person)

with open ("day-24/Input/Letter/starting_letter.txt") as starting:
    invite = starting.read()


for person in new_names:
    without_quote_person = person.strip('"\'')
    with open(f"day-24/Output/Ready To Send/{person}.txt", "w") as letter:
        final = invite.replace(f"[name]", (without_quote_person))
        letter.write(final)
        

        
