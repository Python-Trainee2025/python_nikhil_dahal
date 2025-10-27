#Question no.1

word1=input('Enter the first word: ').lower()
word2=input('Enter the second word: ').lower()
print(f'The given words are: {word1} and {word2}.')
if sorted(word1)==sorted(word2):
    print('The given words are the anagrams.')
else:
    print('The given words are not the anagrams.')


# Question no 2.

word=input('Enter a word:')
print('The given word is: ',word)
pal=(word[::-1])
if pal==word :
    print('This word is palindrome.')
else:
    print('This word is not palindrome.')



# Question no.3

text = input('Enter a sentence or paragraph: ')
words = text.lower().split()
unique_words = set(words)
print("The unique word count is: ", len(unique_words))


# Question no.4

create_dic={
    'Nikhil':9863471425,
    'Samir':9812345678,
    'Mehul':9856970345
}
userinput=input('Enter the name to be searched: ')
cap_userinput=userinput.capitalize()
if cap_userinput in create_dic:
    print(f"{cap_userinput}'s contact info is {create_dic[cap_userinput]}")
else:
    print(f"Sorry, No,{cap_userinput} found in dictionary.")



