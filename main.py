# COMP100 Problem Set 3
#
# The Word Game
# Modified by: Ege Onat Özsüer
#
# Name          : <your name>
# Time spent    : <total time>

import math
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 30

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
FILE_NAMES = ['names', 'cities', 'animals']

def load_words():
    """
    Returns a dictionary of categories as keys and
    a list of valid words as values.
    Words are strings of lowercase letters.
    """

    print("Loading categories from files...")

    w_dict = {}
    for name in FILE_NAMES:
        # inFile: file
        in_file = open("data/" + name + '.txt', 'r')
        # wordlist: list of strings
        wordlist = []
        for line in in_file:
            wordlist.append(line.strip().lower())
        w_dict[name] = wordlist
        in_file.close()
        print("{} words loaded from the {} category.".format(len(wordlist), name))
    print("-"*70)
    return w_dict
# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def calculate_score(words):
    """
    words: list of strings
    returns: int >= 0
    """
    used = 0
    score = 1
    for word in words:
        score *= len(word)-int("*" in word)
        used += len(word)
    score *= math.factorial(len(words))

    lettersLeft = HAND_SIZE - used
    lettersLeft = math.floor(math.sqrt(lettersLeft))
    score -= lettersLeft

    return max(0, score)

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={"*" : 1}
    num_vowels = int(math.ceil(n / 3))

    for i in range(1, num_vowels):
        vow = random.choice(VOWELS)
        hand[vow] = hand.get(vow, 0) + 1

    for i in range(num_vowels, n):
        cons = random.choice(CONSONANTS)
        hand[cons] = hand.get(cons, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assume that hand contains every letter in word at least as
    many times as the letter appears in word.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    empty = []
    hand_copy = hand.copy()

    for letter in word:
        hand_copy[letter] -= 1
    for key in hand:
        if hand_copy[key] == 0:
            empty.append(key)
    for key in empty:
        hand_copy.pop(key)
    
    return hand_copy
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    validity = False

    wildcard = word.find("*")
    if wildcard != -1:
        for letter in VOWELS:
            wordRefined = word[0:wildcard] + letter + word[wildcard+1:]
            validity = validity or (wordRefined in word_list)
    else:
        validity = word in word_list

    totalUsed = 0
    for key in hand:
        totalUsed += word.count(key)
        validity = validity and (word.count(key) <= hand[key])
    if totalUsed < len(word):
        validity = False
    
    
    return validity

#
# Problem #5: Playing a hand
#
def play_hand(hand, word_dict):
    words = []
    continue_game = True
    possible_cats = ["n", "c", "a"]
    while continue_game == True:
        """
        Allows the user to play the given hand, as follows:

        1) The hand is displayed.
        """
        display_hand(hand)

        """
        2) The user may select a category by entering "n", "c", or "a"
        without the quotes, meaning name, city and animal respectively.
        If the category is an unexpected value, it should be rejected,
        and the user should be asked to try again.
        """
        
        
        categories = {
            "a" : "animals",
            "n" : "names",
            "c" : "cities"
        }
        """
        3) The user may submit a word for the chosen category
        """
        while True:
            if len(possible_cats) == 0:
                break
            while True:
                category = input("Please choose your category (n/c/a): ").lower()
                if category == "!!":
                    break
                elif category not in possible_cats:
                    print("Please choose a valid category")
                else:
                    possible_cats.remove(category)
                    break
            if category == "!!":
                break

            
            word_is_Valid = False
            word = input("Please enter your word: ").lower()
            
            while not word_is_Valid:
                """
                4) When a valid word is entered, it uses up letters
                from the hand.
                """
                if is_valid_word(word, hand, word_dict[categories[category]]):
                    words.append(word)
                    print("Valid word, current score is: " + str(calculate_score(words)))
                    hand = update_hand(hand, word).copy()
                    display_hand(hand)
                    word_is_Valid = True
                else:
                    word = input("Your word is not valid, please enter another: ").lower()

                """
                5) An invalid word is rejected, and a message is displayed asking
                the user to choose another word. No letters are removed from
                the hand.

        6) After every valid word: the score for that word is displayed,
        the remaining letters in the hand are displayed, and the user
        is asked to input another word.
        """

        print("Turn over, your score is: " + str(calculate_score(words)))
        continue_game = False

        """
        7) The hand score is displayed when the hand finishes.

        8) The hand finishes when the player has submitted a word for all
        three categories. The user can also finish playing the hand by
        inputing two exclamation points ('!!') instead of a category.

        hand: dictionary (string -> int)
        word_dict: dictionary (string -> List of lowercase words).
        returns: the total score for the hand

        """
    return calculate_score(words)

#
# Problem #6: Playing a game
#


#
# Function you will use to substitute a letter in a hand
#
def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':1, 'j':1} -> if the new letters are 'j' and 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    hand_return = hand.copy()
    hand_return.pop(letter)
    alphabet = VOWELS + CONSONANTS
    
    for i in range(hand[letter]):
        let = random.choice(alphabet)
        while let in hand:
            let = random.choice(alphabet)
        hand_return[let] = hand_return.get(let, 0) + 1
    
    return hand_return


def play_game(word_dict):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands
    """
    hands = int(input("Please enter number of hands you wish to play: "))
    total_score = 0
    """
    * Accumulates the score for each hand into a total score for he
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.
    """
    
    sub_permited = True
    retry_permitted = True

    for x in range(hands):
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)
        
        if sub_permited:
            substitute = input("Would you like to substitute a letter: ").lower()
            if substitute == "yes":
                sub_permited = False
                letter_to_sub = input("Please enter letter to substitute: ").lower()
                hand = substitute_hand(hand, letter_to_sub).copy()

        hand_score = play_hand(hand, word_dict)
        if retry_permitted:
            retry = input("Would you like to replay this turn: ")
            if retry == "yes":
                retry_permitted = False
                hand_score = max(hand_score, play_hand(hand, word_dict))
        total_score += hand_score
    return total_score   
        

    """
    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had. If you
                    chose to substitute before, you get the substituted hand
                    again.

    * Returns the total score for the series of hands

    word_dict: A dictionary that has category names as keys and lists of lowercase valid words as values
    """


#
# Build data structures used for entire session and play game
def main():
    word_dict = load_words()
    play_game(word_dict)

#
# This code is executed when the program is run directly,
# instead of through an import statement
#
if __name__ == '__main__':
    main()