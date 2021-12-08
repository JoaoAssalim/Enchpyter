class Enchpyter:
    
    def __init__(self, total_encrypt_number):

        self.alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.total_encrypt_number = total_encrypt_number

    def encrypt(self, word):
    
        self.encrypt_word = ''
        
        for letter in word:
            self.index_letter = self.alfabeto.index(letter) + self.total_encrypt_number
            if self.index_letter > len(self.alfabeto):
                self.index_letter = self.index_letter - len(self.alfabeto) #Subtract the total by 25 and find the index
            self.encrypt_word += self.alfabeto[self.index_letter]
        print(self.encrypt_word)
    
    def decrypt(self, word):
        
        self.decrypt_word = ''
        
        for letter in word:
            self.index_letter = self.alfabeto.index(letter) - self.total_encrypt_number
            self.decrypt_word += self.alfabeto[self.index_letter]
            
        print(self.decrypt_word)


if __name__ == '__main__':
    try:
        total_encrypt_number = int(input('Enter how many numbers to jump index (25 is max): '))
        if total_encrypt_number <= 25:
        
            encpt = Enchpyter(total_encrypt_number)
            option = int(input('[1] - Encrypt\n[2] - Decrypt\n-> '))
            
            if option == 1:
                word = input('Word to encrypt (Just Letters): ').upper()
                if not any(chr.isdigit() for chr in word):
                    encpt.encrypt(word)
                else:
                    print('Number in word')
    
            elif option == 2:
                word = input('Word to decrypt (Just Letters): ').upper()
                if not any(chr.isdigit() for chr in word):
                    encpt.encrypt(word)
                else:
                    print('Number in word')
            else:
                print('Invalid Option!')
        else:
            print('Number greater than 25!')

    except ValueError as e:
        print('Error: ', e)
