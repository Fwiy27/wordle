from colorama import Fore, Style
import os

# Info should be a list[int] of where 0 <= int <= 2
# 0 is for WHITE | Not in word
# 1 is for GREEN | In word and correct place
# 2 is for YELLOW | In word but not in correct place
def pretty_word(word: str, info: list[int]) -> str:
    '''Returns a colorized version of the word given the word and info'''
    colors = {
        0: Fore.WHITE,
        1: Fore.GREEN,
        2: Fore.YELLOW
    }
    if len(word) != len(info):
        raise IndexError('Word and Info are not the same length')
    
    return ''.join([f'{colors[pair[1]]}[{pair[0].upper()}]{Fore.RESET}' for pair in zip(word, info)])

# Same format as function above, gives list[int] where 0 <= int <= 2
def get_info(word: str, guess: str) -> list[int]:
    '''Returns info given the word and guess'''
    
    # Ensure correct length
    if len(word) != len(guess):
        raise IndexError('Word and Guess are not the same length')
    
    # Ensure matching casing
    word, guess = word.lower(), guess.lower()
    
    info: list[int] = []
    leftover: list[str] = []
    
    # Check for letters in correct places
    for i in range(len(guess)):
        num = 1 if guess[i] == word[i] else 0
        info.append(num)
        if num == 0: leftover.append(word[i])
        
    # Check for letters in word but not in correct place
    for i in range(len(info)):
        if info[i] == 0 and guess[i] in word and guess[i] in leftover:
            info[i] = 2
            leftover.remove(guess[i])
            
    return info

def hard_most_consistent(word: str, guess: str, previous_guess: str | None) -> bool:
    '''Returns True if guess is in accordance with hard mode else False'''
    # Return True if there is no previous guess
    if not previous_guess: 
        return True

    # Ensure consistent casing
    word, guess, previous_guess = word.lower(), guess.lower(), previous_guess.lower()

    # Get info for previous guess
    previous_info: list[int] = get_info(word, previous_guess)

    # Check letters in the correct place
    leftover: list[str] = []
    for i, value in enumerate(previous_info):
        if value == 1:  # Letter is in the correct position
            if guess[i] != previous_guess[i]:  # Must use the same letter in the same position
                return False
        elif value == 2:
            leftover.append(previous_guess[i])
            
    # Check for letters in word but not correct place
    for i, value in enumerate(previous_info):
        if value != 1 and guess[i] in leftover:
            leftover.remove(guess[i])
    
    if len(leftover) != 0: return False

    # All checks passed
    return True

# Read a file into a list of the lines
def read_file(file_name: str) -> list[str]:
    '''Returns list[str] of lines of given {file_name}'''
    with open(file_name, 'r') as file:
        return file.read().strip().split()

# Checks validity of guess
def valid_guess(word: str, guess: str, words: list[str], available: list[str]) -> bool:
    # Make sure capitalization is consistent
    word, guess = word.lower(), guess.lower()
    
    if len(guess) != len(word) or guess not in words + available: return False
    return True

# Prints history of guesses
def print_history(history: list[tuple[str, list[int]]]) -> None:
    for word, info in history:
        print(pretty_word(word, info))
        
def clear_screen() -> None:
    os.system('clear')