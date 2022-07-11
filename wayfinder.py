# Trivial file left behind to explain work I've done for some of my internship.

from multiprocessing.sharedctypes import Value
import random 
import sys
import time

typing_speed = 80 #wpm

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')

slow_type("Author: Meet Kothari")    
print("\n")
slow_type("Date: 7/08/2022")
print("\n")
slow_type("Welcome...")
print("\n")

slow_type("This is the folder for Project 2, 'BI Trends' from the 2022 Giant Leap program. What would you like help with?")
slow_type("1. 'I can't find a file I'm looking for....'")
slow_type("2. 'What did you do?'")

placeholder = input("? ")

if placeholder in ('1', '2', '3', '4'):
    
        if placeholder == '1': 
            slow_type("\nTell me more. What kind of file are you looking for?")
            slow_type("1. 'I don't remember. Something about data?")
            slow_type("2. 'The final product- what you sent to Dan.'")
            slow_type("3. 'The intermediate product- what you did the work in.'")
            slow_type("4. 'The base product- what you were given by Dan to work with.'")
            
            cin = input("? ")
            
            if int(cin) == 1:
                slow_type("\nThat's kind of broad. Here's an overview of everything in this folder...")
                slow_type("\nThere's 'Constant Inventory.docx' and 'Trends to Watch.docx,' files that contain the products that are constant, and the product that need to be restocked, respectively...")
                slow_type("\nThere's the 'constants.xlsx' and 'BI- trend in Inventory Reports- Finished.xlsx' files, which are the source files for the documents mentioned above...")
                slow_type("\nThere's the folder 'Possible Halts' which contains the finalized version of the constant files that demonstrates products Vaisala seems to have a supply of that hasn't dipped in years...")
                slow_type("\nFinally, there's the folder 'Source Files (BI and Bulk)' which contains the source files given to me, unaltered...")
            
            if int(cin) == 2:
                slow_type("\nI kind of sent Dan the whole folder. This project had a built-in reading guide, so I just sent the whole thing over. Specifically, though, the things to note would be the 'Possible Halts' folder, the 'Bulk Inventory.docx' file, and the 'Trends to Watch.docx' file...")
                
            if int(cin) == 3:
                slow_type("\nYou're looking for the optimized file, 'OptimizedWithDupesColored.xlsx,' which is the precursor to the 'final.xlsx' file...")
            
            if int(cin) == 4:
                 slow_type("\nThere's the 'Source Files (BI and Bulk),' which contains the source file from BI, and my own edited version of it that is a bit more legible...")
           
        if placeholder == '2':
            slow_type("\nThis one, honestly, wasn't that complicated. All I did was take the source file, sort it, and then visualize that data using Excel.")
            
else: slow_type("\nI can't help with that...")

slow_type("\nʕ•́ᴥ•̀ʔっ bye!")
