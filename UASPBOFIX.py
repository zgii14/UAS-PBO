import random

kata_kunci = ['apel', 'jeruk', 'mangga', 'pisang', 'semangka', 'nanas']

def ambil_kata_kunci():
    return random.choice(kata_kunci)

def tampilkan_gantungan_hangman(kesalahan):
    gantungan_hangman = [
        '''
          +---+
          |   |
              |
              |
              |
              |
        =========''',
        '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''',
        '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''',
        '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        ========='''
    ]
    return gantungan_hangman[kesalahan]

def tampilkan_kata_tersembunyi(kata, tebakan):
    tebakan_benar = ''.join([c if c in tebakan else '_' for c in kata])
    return tebakan_benar

def tampilkan_status(tebakan, kesalahan):
    print('Tebakan kamu:', ' '.join(tebakan))
    print('Kesalahan:', kesalahan)

def main():
    print('Selamat datang di Hangman!')
    kata = ambil_kata_kunci()
    kesalahan = 0
    tebakan = []
    
    while True:
        tampilan = tampilkan_gantungan_hangman(kesalahan)
        print(tampilan)
        
        kata_tersembunyi = tampilkan_kata_tersembunyi(kata, tebakan)
        print('Kata tersembunyi:', kata_tersembunyi)
        
        tampilkan_status(tebakan, kesalahan)
        
        if kesalahan == 6:
            print('Kamu kalah! Kata yang benar adalah:', kata)
            break
        
        if kata == kata_tersembunyi:
            print('Selamat! Kamu menang!')
            break
        
        huruf = input('Masukkan huruf tebakanmu: ').lower()
        
        if huruf in tebakan:
            print('Kamu sudah menebak huruf ini sebelumnya.')
        elif huruf.isalpha() and len(huruf) == 1:
            if huruf in kata:
                print('Tebakan benar!')
                tebakan.append(huruf)
            else:
                print('Tebakan salah!')
                kesalahan += 1
                tebakan.append(huruf)
        else:
            print('Masukkan hanya satu huruf.')
    
    print('Terima kasih telah bermain Hangman!')

if __name__ == '__main__':
    main()
