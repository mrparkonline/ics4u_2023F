'''Highest Scrabble Word

Given a list of strings, determine the string with the highest scrabble score.

The Scrabble Point System:
1 point: E,A,I,O,N,R,T,L,S,U
2 points: D,G
3 points: B,C,M,P
4 points: F,H,V,W,Y
5 points: K
8 points: J,X
10 points: Q,Z

The characters of the word will be totaled up for a score. Example: CAT has a score of 5 (3+1+1).

Write a function that takes a list of strings as an argument and returns a list with two items → [highest_scoring_word, highest_score]
'''

def scrabble(word):
    ''' Given a string argument, determine the integer score of the word
    
    argument:
        word : a string value
    
    return
        integer : the total scrabble score
    '''
    total_score = 0
    for character in word:
        current_character = character.upper()
        if current_character in "EAIONRTLSU":
            total_score += 1
        elif current_character in "DG":
            total_score += 2
        elif current_character in "BCMP":
            total_score += 3
        elif current_character in "FHVWY":
            total_score += 4
        elif current_character == "K":
            total_score += 5
        elif current_character == "JX":
            total_score += 8
        elif current_character == "QZ":
            total_score += 10
    # end of for loop
    return total_score
# end of scrabble()
    

def best_score(a_list):
    ''' Given a list of words, we are going to determine which word has the highest scrabble score

    argument:
        a_list : list of strings
    
    return
        a list or a tuple:
            item1 --> the highest scoring word
            item2 --> the total scrabble score
    '''
    result_list = ["", 0]
    for word in a_list:
        current_score = scrabble(word)

        if current_score > result_list[1]:
            result_list[0] = word
            result_list[1] = current_score
    
    return result_list
# end of best_score()

words = [
    'despair',
    'choose',
    'notice',
    'history',
    'appetite',
    'dominant',
    'implicit',
    'or',
    'prediction'
]
#print(scrabble('graphic'))
answer, score = best_score(words)
print(f"{answer} had the highest scrabble score with {score}.")