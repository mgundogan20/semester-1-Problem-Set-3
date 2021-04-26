import io
import sys
from main import *

#
# Test code
#
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def test_get_word_score():
    """
    Unit test for get_word_score
    """
    failure=False
    # Words and scores
    attempt_scores = [
        (['scozbmy'], 3),
        (['wv*'], 0),
        (['gtk*a'], 0),
        (['cytht*', 'ynzkvju'], 66),
        (['kpomjup', 'ghkg*dqrfe'], 123),
        (['erbs', 'bvd'], 20),
        (['hz', '*nh', 'qzn'], 68),
        (['hghx', 'zcjvjpjk', 'qhdhgprnbn'], 1918),
        (['re*hhr', 'yxlbalfpzz', 'jxhisbpqw'], 2698)]
    for words, true_score in attempt_scores:
        score = calculate_score(words)
        if score != true_score:
            print("FAILURE: test_get_word_score()")
            print("\tExpected",true_score,"points but got '" + \
                  str(score) + "' for words: '" + str(words))
            failure=True

    assert not failure
    if failure:
        return 0
    else:
        print("SUCCESS: test_get_word_score()")
        return 10

# end of test_get_word_score


def test_update_hand():
    """
    Unit test for update_hand
    """
    failure = False
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {'l':1, 'm':1}
    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        failure = True
    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        failure = True
    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "evil"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {'v':1, 'n':1, 'l':1}
    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")        
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        failure = True

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        failure = True

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {}
    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expected_hand1, "or", expected_hand2)

        failure = True

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        failure = True

    assert not failure
    if failure:
        return 0
    else:
        print("SUCCESS: test_update_hand()")
        return 10

# end of test_update_hand

def test_is_valid_word():
    """
    Unit test for is_valid_word
    """
    word_dict = load_words()
    failure=False
    # test 1
    word = "frassilongo"
    handOrig = get_frequency_dict(word)
    handCopy = handOrig.copy()

    if not is_valid_word(word, handCopy, word_dict['cities']):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

        failure = True

    # Test a second time to see if word_dict or hand has been modified
    if not is_valid_word(word, handCopy, word_dict['cities']):
        print("FAILURE: test_is_valid_word()")

        if handCopy != handOrig:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

        else:
            print("\tTesting word", word, "for a second time - have you modified word_dict?")
            wordInWL = word in word_dict
            print("The word", word, "should be in word_dict - is it?", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

        failure = True


    # test 2
    hand = {'a': 2, 'd': 2, 'e': 1, 'n': 1, 'u':1}
    word = "adana"

    if  is_valid_word(word, hand, word_dict['cities']):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True        

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not is_valid_word(word, hand, word_dict['names']):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  is_valid_word(word, hand, word_dict['names']):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        
        failure = True

    # test 5
    hand = {'e':2, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "neville"
    
    if  not is_valid_word(word, hand, word_dict['names']):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)
        
        failure = True
        
    # test 6
    word = "neville"

    if  not  is_valid_word(word, hand, word_dict['names']):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)")        
        
        failure = True        

    # test 7
    hand = {'e':2, 'v':2, 'n':1, 'i':1, 'g':2, 't':1, 'r':3}
    word = "tiger"

    if  not is_valid_word(word, hand, word_dict['animals']):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)
 
        failure = True

    # test 8
    hand = {'e':2, 'v':2, 'n':1, 'i':1, 'l':2, 't':1, 'r':3}
    word = "tiger"

    if is_valid_word(word, hand, word_dict['cities']):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    assert not failure
    if failure:
        return 0
    else:
        print("SUCCESS: test_is_valid_word()")
        return 20


# end of test_is_valid_word

def test_wildcard():
    """
    Unit test for is_valid_word
    """
    word_list = load_words()
    failure=False

    # test 1
    hand = {'a': 1, 'r': 1, 'e': 1, 'l': 2, 'k': 1, '*': 1}
    word = "*lkr"

    if is_valid_word(word, hand, word_list['animals']):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 2
    hand = {'n': 1, 'd': 1, '*': 1, 'y': 1, 'k':1, 'w':1, 'e': 2}
    word = "donkey"

    if is_valid_word(word, hand, word_list['animals']):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 3
    hand = {'n': 1, 'd': 1, '*': 1, 'y': 1, 'k':1, 'w':1, 'e': 2}
    word = "d*nkey"

    if not is_valid_word(word, hand, word_list['animals']):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True

    # test 4
    hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
    word = "c*wz"

    if is_valid_word(word, hand, word_list['names']):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '"+ word +"' and hand:", hand)

        failure = True    

    assert not failure
    if failure:
        return 0
    else:
        print("SUCCESS: test_wildcard()")
        return 20

def test_play_hand():
    word_dict = load_words()
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    failure = False

    hand = {'c':1, 'a':1, 't':1}
    sys.stdin = open('test_inputs/play_hand_test1.txt', 'r')
    score = play_hand(hand, word_dict)
    if score != 0:
        sys.stdout = stdout
        print("FAILURE: test_play_hand on test1")
        failure = True
        sys.stdout = io.StringIO()
    sys.stdin.close()

    hand = {'a':2, 'l':2, 'i':1, 'g':1, 't':1, 'o':1, 'r':1}
    sys.stdin = open('test_inputs/play_hand_test2.txt', 'r')
    score = play_hand(hand, word_dict)
    if score != 5:
        sys.stdout = stdout
        print("FAILURE: test_play_hand on test2")
        failure = True
        sys.stdout = io.StringIO()
    sys.stdin.close()

    hand = {'a':2, 'l':2, 'i':1, 'g':1, 't':1, 'o':2, 'r':1, 'j':1, 'e':1}
    sys.stdin = open('test_inputs/play_hand_test3.txt', 'r')
    score = play_hand(hand, word_dict)
    if score != 50:
        sys.stdout = stdout
        print("FAILURE: test_play_hand on test3")
        failure = True
        sys.stdout = io.StringIO()
    sys.stdin.close()

    hand = {'a':2, 'l':3, 'i':1, 'g':1, 't':1, 'o':4, 's':3, 'r':1, 'j':1, 'e':1}
    sys.stdin = open('test_inputs/play_hand_test4.txt', 'r')
    score = play_hand(hand, word_dict)
    if score != 645:
        sys.stdout = stdout
        print("FAILURE: test_play_hand on test4")
        failure = True
        sys.stdout = io.StringIO()
    sys.stdin.close()

    hand = {'a':2, 'l':3, 'i':1, 'g':1, 't':1, 'o':4, 's':3, 'r':1, 'j':1, 'e':1}
    sys.stdin = open('test_inputs/play_hand_test5.txt', 'r')
    score = play_hand(hand, word_dict)
    if score != 645:
        sys.stdout = stdout
        print("FAILURE: test_play_hand on test5")
        failure = True
        sys.stdout = io.StringIO()
    sys.stdin.close()

    hand = {'b':2, 'l':3, 'i':1, 'g':1, 'p':1, 'o':3, 's':3, 'u':1, 'm':1, 'e':1}
    sys.stdin = open('test_inputs/play_hand_test6.txt', 'r')
    score = play_hand(hand, word_dict)
    if score != 36:
        assert score == 36
        sys.stdout = stdout
        print("FAILURE: test_play_hand on test6")
        failure = True
        sys.stdout = io.StringIO()
    sys.stdin.close()

    sys.stdout = stdout
    assert not failure
    if failure:
        return 0
    else:
        print("SUCCESS: test_play_hand")
        return 20

def test_substitute_hand():
    failure = False

    hand = {'h':1, 'e':1, 'l':2, 'o':1}
    old_hand = hand.copy()
    sub_let = 'l'
    new_hand = substitute_hand(hand, sub_let)

    if not new_hand:
        print("FAILURE: substitute_hand function returned None.")
        print("Old hand was:", hand)
        print("Substituted hand is: ", new_hand)
        failure = True

    if not old_hand == hand:
        print("FAILURE: substitute_hand() is not supposed to modify the input hand")
        print("Old hand was:", hand)
        print("Substituted hand is: ", new_hand)
        failure = True

    old_size = sum(old_hand.values())
    new_size = sum(new_hand.values())
    if not old_size == new_size:
        print("FAILURE: input hand had {} letters, output has {}".format(old_size, new_size))
        print("Old hand was:", hand)
        print("Substituted hand is: ", new_hand)
        failure = True

    sub_let_gone = sub_let not in new_hand.keys() or new_hand[sub_let] == 0
    if not sub_let_gone:
        print("FAILURE: the substituted letter is still in the hand!")
        print("Old hand was:", hand)
        print("Substituted hand is: ", new_hand)
        failure = True

    no_side_effects = True
    for k in [k for k in hand.keys() if k != sub_let]:
        if hand[k] != new_hand[k]:
            no_side_effects = False
    if not no_side_effects:
        print("FAILURE: wrong letters changed in the hand")
        print("Old hand was:", hand)
        print("Substituted hand is: ", new_hand)
        failure = True

    for i in range(100):
        hand = {'a':2, 'l':3, 'i':1, 'g':1, 't':1, 'o':4, 's':3, 'r':1, 'j':1, 'e':1}
        sub_let = 'l'
        old_hand = hand.copy()
        new_hand = substitute_hand(hand, sub_let)
        hand_unchanged = old_hand == hand
        correct_letter_num = sum(old_hand.values()) == sum(new_hand.values())
        no_side_effects = True
        for k in [k for k in hand.keys() if k != sub_let]:
            if hand[k] != new_hand[k]:
                no_side_effects = False
        if not (hand_unchanged and correct_letter_num and no_side_effects):
            failure = True

    assert not failure
    if failure:
        print("FAILURE: test_substitute_hand")
        return 0
    else:
        print("SUCCESS: test_substitute_hand")
        return 5

def test_play_game():
    word_dict = load_words()
    stdin = sys.stdin
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    failure = False

    hand = {'c':1, 'a':1, 't':1}
    sys.stdin = open('test_inputs/play_game_test1.txt', 'r') 
    score = play_hand(hand, word_dict)
    if score != 0:
        sys.stdout = stdout
        print("FAILURE: test_play_game on test1")
        failure = True
        sys.stdout = io.StringIO()
    sys.stdin.close()

    hand = {'c':1, 'a':1, 't':1}
    sys.stdin = open('test_inputs/play_game_test2.txt', 'r') 
    score = play_hand(hand, word_dict)
    if score != 0:
        sys.stdout = stdout
        print("FAILURE: test_play_game on test2")
        failure = True
        sys.stdout = io.StringIO()
    sys.stdin.close()

    sys.stdout = stdout
    sys.stdin = stdin
    assert not failure
    if failure:
        return 0
    else:
        print("SUCCESS: test_play_game")
        return 15