'''This program can help you to encrypt some text
it can variate while you configure it

Code in Github: https://github.com/JoaoAssalim/Enchpyter
'''

class Enchpyter:


    def __init__(self, word):
        self.word = word
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÇ'


    def encrypt(self):

        self.encrypted = ''
        for letter in word:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                index += 3

                if index > 26:
                    index -= 26
                self.encrypted += self.alphabet[index]

            elif letter == ' ':
                self.encrypted += 's'
            elif letter == '.':
                self.encrypted += 'd'
            elif letter == ',':
                self.encrypted += 'c'
            elif letter == '(':
                self.encrypted += 'e'
            elif letter == ')':
                self.encrypted += 'r'
            elif letter == '{':
                self.encrypted += 'k'
            elif letter == '}':
                self.encrypted += 'l'
            elif letter == '[':
                self.encrypted += 'b'
            elif letter == ']':
                self.encrypted += 'v'
            elif letter == '!':
                self.encrypted += '!'
            elif letter == '?':
                self.encrypted += '?'
            elif letter == '/':
                self.encrypted += '/'
            elif letter.isdigit():
                self.encrypted += letter

        return self.encrypted

    def decrypt(self):

        self.decrypted = ''
        for letter in word:           

            if letter == 'e':
                self.decrypted += '('
            elif letter == 'r':
                self.decrypted += ')'
            elif letter == 'k':
                self.decrypted += '{'
            elif letter == 'l':
                self.decrypted += '}'
            elif letter == 'b':
                self.decrypted += '['
            elif letter == 'bc':
                self.decrypted += ']'
            elif letter == 's':
                self.decrypted += ' '
            elif letter == 'd':
                self.decrypted += '.'
            elif letter == 'c':
                self.decrypted += ','
            elif letter == '!':
                self.encrypted += '!'
            elif letter == '?':
                self.encrypted += '?'
            elif letter == '/':
                self.encrypted += '/'
            elif letter.isdigit():
                self.decrypted += letter
            else:
                index = self.alphabet.index(letter)
                index -= 3
                self.decrypted += self.alphabet[index]

        return self.decrypted

choice_method = input('[1] - Encrypt\n[2] - Decrypt\n-> ')
if choice_method == '1':
    word = input('Enter a word: ').upper()
    enchpyter = Enchpyter(word)
    print(enchpyter.encrypt())
elif choice_method == '2':
    word = input('Enter a word: ')
    enchpyter = Enchpyter(word)
    print(enchpyter.decrypt())
else:
    print('Invalid Option')
