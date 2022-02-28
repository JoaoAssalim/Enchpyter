class Enchpyter:


    def __init__(self, word):
        self.jumps = 3
        self.word = word
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt(self):

        self.encrypted = ''
        for letter in word:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                index += self.jumps

                if index > 26:
                    index -= 26
                self.encrypted += self.alphabet[index]
                
            else:
                if letter == '(':
                    self.encrypted += 'P'
                elif letter == ')':
                    self.encrypted += 'T'
                elif letter == '{':
                    self.encrypted += 'K'
                elif letter == '}':
                    self.encrypted += 'C'
                elif letter == '-':
                    self.encrypted += 'R'
                elif letter == '_':
                    self.encrypted += 'U'
                elif letter == '/':
                    self.encrypted += 'O'
                elif letter == '.':
                    self.encrypted += 'D'
                else:
                    self.encrypted += letter

        return self.encrypted

    def decrypt(self):

        self.decrypted = ''
        for letter in word:           

            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                index -= self.jumps
                self.decrypted += self.alphabet[index]
            else:
                if letter == 'P':
                    self.decrypted += '('
                elif letter == 'T':
                    self.decrypted += ')'
                elif letter == 'K':
                    self.decrypted += '{'
                elif letter == 'C':
                    self.decrypted += '}'
                elif letter == 'R':
                    self.decrypted += '-'
                elif letter == 'U':
                    self.decrypted += '_'
                elif letter == 'O':
                    self.decrypted += '/'
                elif letter == 'D':
                    self.decrypted += '.'
                else:
                    self.decrypted
                    += letter

        return self.decrypted

choice_method = input('[1] - Encrypt\n[2] - Decrypt\n-> ')
if choice_method == '1':
    word = input('Enter a word: ').lower()
    enchpyter = Enchpyter(word)
    print(enchpyter.encrypt())
elif choice_method == '2':
    word = input('Enter a word: ')
    enchpyter = Enchpyter(word)
    print(enchpyter.decrypt())
else:
    print('Invalid Option')
