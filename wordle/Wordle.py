from wordle.util import pretty_word, get_info, read_file, valid_guess, print_history, clear_screen, hard_most_consistent
from random import choice

class Wordle:
    def __init__(self) -> None:
        pass
    
    def play(self, hard_mode: bool = False) -> bool:
        words: list[str] = read_file('wordle/words/words.txt')
        available: list[str] = read_file('wordle/words/available.txt')
        
        guesses: int = 6
        word: str = choice(words)
        history: list[tuple[str, list[int]]] = []
        
        previous: str | None = None
        while guesses > 0:
            guess: str | None = None
            while not guess:
                clear_screen()
                print('---------------')
                print_history(history)
                i = input('Your Guess: ')
                if valid_guess(word, i, words, available) and ((hard_mode and hard_most_consistent(word, i, previous)) or not hard_mode):
                    guess = i
                    previous = i
            history.append((guess, get_info(word, guess)))
            
            if guess.lower() == word.lower():
                break
            else:
                print(pretty_word(guess, get_info(word, guess)))
                guesses -= 1
                
        clear_screen()
        print('---------------')
        print_history(history)
        print('---------------')
            
        return True if guesses > 0 else False