 passwordFile = open('SecretPasswordFile.txt')
 
 secretPassword = passwordFile.read()
 print('Enter your password.')
 
 typedPassword = input()
 
  if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
  else:
    print('Access denied')
    
 # Above is a snippet from the Textbook titled, "Automate the Boring Stuff with Python" by Al Sweigart
 # This snippet, taken directly from the source, is a simple Python program that opens a file to compare 
 # the user input to a provided string inside of the file. There are reactions built into the code for 
 # correct guesses, incorrect guesses, and specific guesses. 
