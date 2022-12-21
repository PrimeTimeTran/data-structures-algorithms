# Decrypt Message
# An infamous gang of cyber criminals named “The Gray Cyber Mob”, which is behind many hacking attacks and drug trafficking, has 
# recently become a target for the FBI. After intercepting some of their messages, which looked like complete nonsense, the agency learned that 
# they indeed encrypt their messages, and studied their method of encryption.

# Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:

# Convert every letter to its ASCII value. Add 1 to the first letter, and then for every letter from the second one to the last one, 
# add the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. 
# Convert the values back to letters.

# For instance, to encrypt the word “crime”


def decrypt(word):
  decryption = ""
  prev_letter_val = 1

  for letter in word:
    letter_ascii_val = ord(letter)
    letter_ascii_val -= prev_letter_val

    while letter_ascii_val < ord('a'):
      letter_ascii_val += 26

    decryption += chr(letter_ascii_val)
    prev_letter_val += letter_ascii_val

  return decryption


print(decrypt('dnotq'))

