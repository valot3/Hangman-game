import subprocess
import random
from time import sleep

from templates import *

class HangmanGame():

    def __init__(self):
        self.mistakes = 0
        self.current_level = 0

        self.chosen_word = ''
        self.word_brackets = ''

        self.right_letters = []
        self.letters_of_chosen_word = []


    def _rewrite_word_brackets(self, chosen_word):

        new_word_brackets = ''

        for letter in chosen_word:

            if letter in self.right_letters:
                new_word_brackets += letter
            else:
                new_word_brackets += '_'

        self.word_brackets = new_word_brackets


    def _read_data(self, filepath = './data.txt'):
        words_list = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    words_list.append(line.strip().upper())
            
            return words_list

        except Exception as ex:
            print('The file path was not specified.')
            print('Exception: \n\t', ex)


    def graphics_engine(self, template = None):
        template = str(template or self.mistakes)

        clear()
        level_template(self.current_level)
        main_template()
        print(hangman_pics[template])


    def next_level(self):
        response = input('Next level?\n[y/n]>>> ')
    
        if response == 'y':
            self.config_word()

            self.mistakes = 0
            self.current_level += 1

            self.right_letters = []
        
        elif response == 'n':
            print('Bye!')
            sleep(1)
            self._clear()
        
        else:
            print('Invalid option.')

    
    def config_word(self):
        words_list = self._read_data()

        self.chosen_word = random.choice(words_list)
        filtered_chosen_word = ''
        #------------------Transforming string.
        replacements = {
            'Á' : 'A',
            'É' : 'E',
            'Í' : 'I',
            'Ó' : 'O',
            'Ú' : 'U'
        }

        for letter in self.chosen_word:
            if letter in replacements.keys():
                filtered_chosen_word += replacements[letter]
            else:
                filtered_chosen_word += letter
        
        self.chosen_word = filtered_chosen_word
        #------------------

        self.word_brackets = '_' * len(self.chosen_word)
        self.letters_of_chosen_word = [letter.upper() for letter in self.chosen_word]
            

    def run_game(self):
        self.config_word()
        self.current_level += 1


        while True:

            if self.mistakes == 7:
               self.graphics_engine('you_lost')
               play_again()
               break

            elif '_' not in self.word_brackets:
                self.graphics_engine('you_won')
                self.next_level()
                continue


            #------------------------------------------------------


            self.graphics_engine()
            #print('WORD: ', self.chosen_word) #Temporal line
            print('WORD: ', self.word_brackets, '\n\n')
            print('Type a letter and press [enter]')
            input_letter = input('>>> ').upper()

            if input_letter in self.letters_of_chosen_word:
                self.right_letters.append(input_letter)
                self._rewrite_word_brackets(self.chosen_word)
                continue
            else:
                self.mistakes += 1
                continue      


def clear():
    subprocess.run('clear')


def play_again():
    response = input('Do you want to play again?\n[y/n]>>> ')
    
    if response == 'y':
        runApp()
    
    elif response == 'n':
        print('Bye!')
        sleep(1)
        clear()
    
    else:
        print('Invalid option.')


def runApp():
    game = HangmanGame()
    game.run_game()


if __name__ == '__main__':
    runApp()