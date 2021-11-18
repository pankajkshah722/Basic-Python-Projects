## The Challenge
## Count the number of words provided. For this problem, a word is any-sequence of lowercase letters. For example, 
## hello is a word, but so are non-English “words” like bbaabbb.

## Input
## The input is one line of text, consisting of lowercase letters and spaces.
## There is exactly one space between each pair of words, and there are no
## spaces before the first word or after the last word.
## The maximum length of the line is 80 characters

## Output
## Output the number of words in the input line


line = input()
total_words = line.count(' ')+1
print(total_words)
