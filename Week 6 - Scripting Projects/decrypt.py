code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plaintext = ''

for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - (distance - \
                                  (ordValue - ord('a')) - 1)
    plaintext +=  chr(cipherValue)
print(plaintext)
