def hangman_drawings(wrong_guesses):
  hangman_drawings = ['''
  +---+
  |   |   Wrong guesses left:
      |    »»————- 6 ————-««
      |
      |
      |
=========''', '''
  +---+
  |   |   Wrong guesses left:
  O   |    »»————- 5 ————-««
      |
      |
      |
=========''', '''
  +---+
  |   |   Wrong guesses left:
  O   |    »»————- 4 ————-««
  |   |
      |
      |
=========''', '''
  +---+
  |   |   Wrong guesses left:
  O   |    »»————- 3 ————-««
 /|   |
      |
      |
=========''', '''
  +---+
  |   |   Wrong guesses left:
  O   |    »»————- 2 ————-««
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |   Wrong guesses left:
  O   |    »»————- 1 ————-««
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |   Wrong guesses left:
  O   |    »»————- 0 ————-««
 /|\  |      𝙶𝚊𝚖𝚎 𝙾𝚟𝚎𝚛!
 / \  |
      |
=========''']
  return print(hangman_drawings[wrong_guesses])