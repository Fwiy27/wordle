from colorama import Fore

class Letters:
    def __init__(self) -> None:
        self.top: list[list[str]] = [[letter, Fore.WHITE] for letter in ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']]
        self.middle: list[list[str]] = [[letter, Fore.WHITE] for letter in ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']]
        self.bottom: list[list[str]] = [[letter, Fore.WHITE] for letter in ['Z', 'X', 'C', 'V', 'B', 'N', 'M']]
        self.letters: list[list[list[str]]] = [self.top, self.middle, self.bottom]
        
    def print_letters(self) -> None:
        for i, row in enumerate(self.letters):
            if i != 0: print()
            for letter, color in row:
                print(color + letter + Fore.RESET, end=' ')
        print()
        
    def update_letters(self, guess: str, info: list[int]) -> None:
        for l, i in zip(guess, info):
            for row_index in range(len(self.letters)):
                for letter_index in range(len(self.letters[row_index])):
                    if self.letters[row_index][letter_index][0].lower() == l.lower():
                        match i:
                            case 0:
                                if self.letters[row_index][letter_index][1] == Fore.WHITE:
                                    color = Fore.RED
                                    self.letters[row_index][letter_index][1] = color
                            case 1:
                                color = Fore.GREEN
                                self.letters[row_index][letter_index][1] = color
                            case 2:
                                if self.letters[row_index][letter_index][1] != Fore.GREEN:
                                    color = Fore.YELLOW
                                    self.letters[row_index][letter_index][1] = color
                            case _:
                                color = Fore.WHITE
                                self.letters[row_index][letter_index][1] = color