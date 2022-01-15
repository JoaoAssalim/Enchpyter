class Enchpyter:


    def __init__(self, word):
        self.jumps = 3
        self.word = word
        self.upperletter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.lowerletter = 'abcdefghijklmnopqrstuvwxyz'


    def encrypt(self):

        self.encrypted = ''
        for letter in word:
            if letter in self.upperletter:
                index = self.upperletter.index(letter)
                index += self.jumps

                if index > 26:
                    index -= 26
                self.encrypted += self.upperletter[index]

            elif letter in self.lowerletter:
                index = self.lowerletter.index(letter)
                index += self.jumps

                if index > 26:
                    index -= 26
                self.encrypted += self.lowerletter[index]

            elif letter == ' ':
                self.encrypted += 'Ç'
            elif letter == '.':
                self.encrypted += 'ç'
            elif letter == ',':
                self.encrypted += '&'
            elif letter == '(':
                self.encrypted += '>'
            elif letter == ')':
                self.encrypted += '<'
            elif letter == '{':
                self.encrypted += ';'
            elif letter == '}':
                self.encrypted += ':'
            elif letter == '[':
                self.encrypted += '|'
            elif letter == ']':
                self.encrypted += '-'
            elif letter.isdigit():
                self.encrypted += letter
            else:
                self.encrypted += letter

        return self.encrypted

    def decrypt(self):

        self.decrypted = ''
        for letter in word:           

            if letter == '>':
                self.decrypted += '('
            elif letter == '<':
                self.decrypted += ')'
            elif letter == ';':
                self.decrypted += '{'
            elif letter == ':':
                self.decrypted += '}'
            elif letter == '|':
                self.decrypted += '['
            elif letter == '-':
                self.decrypted += ']'
            elif letter == 'Ç':
                self.decrypted += ' '
            elif letter == 'ç':
                self.decrypted += '.'
            elif letter == '&':
                self.decrypted += ','
            elif letter.isdigit():
                self.decrypted += letter
            elif letter in self.upperletter:
                index = self.upperletter.index(letter)
                index -= self.jumps
                self.decrypted += self.upperletter[index]
            elif letter in self.lowerletter:
                index = self.lowerletter.index(letter)
                index -= self.jumps
                self.decrypted += self.lowerletter[index]
            else:
                self.decrypted += letter

        return self.decrypted

choice_method = input('[1] - Encrypt\n[2] - Decrypt\n-> ')
if choice_method == '1':
    word = input('Enter a word: ')
    enchpyter = Enchpyter(word)
    print(enchpyter.encrypt())
elif choice_method == '2':
    word = input('Enter a word: ')
    enchpyter = Enchpyter(word)
    print(enchpyter.decrypt())
else:
    print('Invalid Option')
