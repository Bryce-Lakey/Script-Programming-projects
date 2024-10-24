plaintext = input("Enter a word: ")
distance = int(input("Enter a number for distance: "))
code = ""
for ch in plaintext:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                      (ord('z') - ordValue + 1)
    code +=  chr(cipherValue)
print(code)
