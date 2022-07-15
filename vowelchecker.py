# Trivial function to test whether a passed string or sentence has any vowels in it.

vowels = ['a','e','i','o','u']

test = input("\nPlease enter a word or words: ")

if any( x in vowels for x in test): print("\nThere's vowels here...")
else: print("\nYou passed!")
