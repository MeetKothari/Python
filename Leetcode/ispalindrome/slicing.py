def is_palindrome(a_string):    # given a palindrome, return its validity 
    if a_string[::-1] == a_string:
        print('Passed.', end = " ")
    else:
        print('Failed.', end = " ")

print('\n') # formatting 
is_palindrome('abba')   # test the function
is_palindrome('pip')
is_palindrome('kobe')
is_palindrome('lester')

 
