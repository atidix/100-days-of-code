alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def remove(text):
  return text.replace(" ", "")

message = remove(text)
message = list(message)
print(message)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

 

def encrypt(message, shift):
  encrypted_message = ""
  for i in range(len(message)):
    values = (alphabet.index(message[i]))
    if (values + shift) > 25:
       N = (values+shift) - 26
       secret_message = alphabet[N]
    else:
       secret_message = alphabet[values + shift]
    for x in secret_message:
      encrypted_message += str(x)
  print(f"The ecoded text is {encrypted_message}")

encrypt(message, shift)
