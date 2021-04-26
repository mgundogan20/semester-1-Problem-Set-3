# PS3 - The Word Game
# Deadline: 29/11/2020-23:00

The goal of this assignment is to implement a single-player word game. While working on the assignment, you will practice concepts such as input/output functions, string operations, mathematical calculations, loops, and python data structures.

You will implement a made-up single-player game, inspired by both Scrabble and the Turkish game "Isim-Sehir-Hayvan". The rules of the game are given below.

**IMPORTANT:** Do **not** edit any files other than main.py . If you modify the `data` directory's contents, you might break the code. If you modify the test_ps3.py or test_inputs files you might break the autograder. The autograder is there for you to see if your implementation is working as intended. There will be additional test cases we will use after submission to grade your work.

**Game Rules**

1. The player will be dealt  *HAND_SIZE* number of random letters to play a hand.
2. The player will have the choice to select one letter from their hand, and replace all the copies of that letter with new random letters.
3. The player will be tasked with creating three words using the letters in their hand. The words need to be one English name, one animal, and one city. They do not need to succeed in making words for all three categories, but they can only submit a word for a category once. Similarly, they do not need to use all the letters in their hands, but they can only use a letter once.
4. The player will receive a score based on the words they submitted. The score calculation will be explained in detail later in the document.
5. Steps 1-4 will be repeated for a number of hands, selected by the player at the beginning of the program.


The starter code given to you has some parts of the game already implemented. The instructions in this document will guide you in coding the rest of the game. The code also contains comments meant to help you complete the assignment.

## Problem 1: Word Scores (10 pts)

In the first task, you need to fill in the code for `calculate_score` in main.py according to the function specifications.

The formula for `calculate_score` are as follows:

1. Multiply the lengths of all submitted words.
2. Multiply by the factorial of the number of words.
3. Subtract the square root of the number of letters left in the player's hand, rounded down to the closest integer.
4. Return the score, or if the score is less than 0, return 0.


Note that with this score calculation, it is possible to get 0 points if you only submit one short word for a turn.


## Problem 2: Updating Hands (10 pts)

In each turn of the game, the player starts with a full hand of n letters. As the player spells out words, the letters get removed from the player's hand.

You will fill the function `update_hand` to remove used letters from the player's hand. 

The player's hand is represented as a dictionary, with letters as keys, and the number of that letter found in the hand as values. 

Example:

`hand = {'a':1, 'q':1, 'l':2, 'e':3}`


## Problem 3: Checking for Valid Words (20 pts)

In this part, you need to fill the `is_valid_word` function according to its specifications. 

A valid word in our game:

* needs to belong to one of the three accepted categories (Animal, Name, City)
* must belong to a category that had no words submitted in this turn.
* must be composed entirely of the letters already in the hand.

Note that the valid word lists we give you are not comprehensive. They may not contain some words, like uncommon animals or very small cities. This is fine, you can ignore such cases.


## Problem 4: Wildcards (20 pts)

Now we want to allow hands to contain wildcard letters, which will be denoted by an asterisk (*). The wildcards will be able to **replace any vowel**. Each hand dealt needs to contain exactly one wildcard.

During the game, the player will be able to enter "*" (without quotes) instead of the intended letter.

You need to modify the `deal_hand` function to support always giving one wildcard in each hand. Note that `deal_hand` currently ensures that one third of the letters are vowels and the rest are consonants. Leave the  consonant count intact, and replace one of the vowel slots with the wildcard.

Then you need to modify the `is_valid_word` function to support wildcards. 

**Hint:** Check to see what possible words can be formed by replacing the wildcard with other vowels. You may want to review the [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods) for string module’s `find()` function and make note of its behavior when a character is not found. The constant `VOWELS` defined for you at the top of the file may be helpful as well.

Example:

`Please enter your word: eagl*
Valid word, current score is: 36`


## Problem 5: Play a hand and exit (20 pts)

You are now ready to begin writing the code that interacts with the player.

Implement the `play_hand` function. This function allows the user to play out a single hand.
To end the hand early, the player must type "!!" (two exclamation points).

```
e o o u u a a a i i v v y g z t t h b r r p p c w s m d j f * 
Please choose your category (n/c/a): a
Please enter your word: c*t
Valid word, current score is: 0
e o o u u a a a i i v v y g z t h b r r p p w s m d j f
Please choose your category (n/c/a): n
Please enter your word: sarah
Valid word, current score is: 16
e o o u u a i i v v y g z t b r p p w m d j f
Please choose your category (n/c/a): c
Please enter your word: izmit
Valid word, current score is: 296
Turn over, your score is: 296
```

## Problem 6: Substitution and Playing a Game (5+15 pts)

Implement the `substitute_hand`(5 pts) and `play_game`(15 pts) functions according to their specifications.
For the game, you should use the *HAND_SIZE* constant to determine the number of letters in a hand.

Do not assume that there will always be a set number of letters in a hand! Our goal is to keep the code modular - if you want to try playing your word game with 10 letters or 40 letters you will be able to do it by simply changing the value of *HAND_SIZE*!

When implementing substitution, you might want to check the methods associated with dictionaries, such as `.keys`, or review the `del` keyword. You may also want to look at the code for `deal_hand` to see how `random.choice` can be used to select an element at random from a set of elements (such as a string).

```
Please enter number of hands you wish to play: 3
a a o i i e e e u m p p p g g q q q c c h h v v r l l y y n * 
Would you like to substitute a letter: yes
Please enter letter to substitute: y
a a o i i e e e u m p p p g g q q q c c h h v v r l l n * x s 
Please choose your category (n/c/a): n
Please enter your word: michael
Valid word, current score is: 3
a o i e e u p p p g g q q q c h v v r l n * x s 
Please choose your category (n/c/a): !!
Turn over, your score is: 3
Would you like to replay this turn: yes
a a o i i e e e u m p p p g g q q q c c h h v v r l l n * x s 
Please choose your category (n/c/a):
```


## Submission

Commit your work using the version control tab of repl.it, as you have done in the previous assignments. Your assignment will be graded by an autograder. Please read the outputs of the autograder carefully to understand which part of your code has failed a test.