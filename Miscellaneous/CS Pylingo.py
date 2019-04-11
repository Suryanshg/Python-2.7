print """Welcome to PyLingo. The rules of the game are:
1. The length of the secret word and guess must be five.
2. Repetition of characters isn't allowed for both the secret word and the guess.
3. You have to guess the word within 7 chances.
4. If you didn't get the word, your guess will be displayed in the following way:
   i. If any of the character of the guess exists in the secret word and at the same position,
      then it will be displayed within [ ].
   ii. If any of the character of the guess exists in the secret word but at some different
   position, then it will be displayed within ( ).
   iii. If  no character is same, then it will be displayed simply.
5. All entries must be in lowercase.
Enjoy the game!
***********************************************************************************************"""
condition=True
import random
while condition:
    L=["tiger","liger","manes","names","watch","snake","wrath","lingo","frank","money","night","might","drunk","young",
       "broke","poker","joker","table","maths","black","niger","flash","tired","slash","latch","patch","match","right",
       "front","slash"]
    word=L[random.randint(0,len(L)-1)]
    word=word.lower()
    lw=list(word)
    if len(set(word))==5 and word.isalpha()==True and len(word)==5:
        guess=str()
        count=1
        while guess!=word and count!=8:
            guess=raw_input("Guess"+str(count)+":")
            guess=guess.lower()
            lg=list(guess)
            if guess.isalpha()==True and len(guess)==5 and len(set(guess))==5:
                for i in lg:
                    if i in lw:
                        if lw.index(i)==lg.index(i):
                            print "[",i,"]",
                        elif lw.index(i)!=lg.index(i):
                            print "(",i,")",
                    elif i not in lw:
                        print i,
                print
            count=count+1
            if guess.isalpha()==False:
                print ("The guess should be made of characters only.")
            elif len(guess)!=5:
                print ("Length of the guess must be five.")
            elif len(set(guess))!=5:
                print ("Repetition of characters isn't allowed.")
        if guess==word:
            print ("Gotcha! You got the word.")
        elif count==8:
            print "Sorry! you have run out of chances. The secret word was:",word
        

        ch=raw_input("Want to play again:Yes(Y)/No(N):")
        print"**************************************************************************************************"
        if ch.lower()=="n":
            condition=False
    elif len(word)!=5:
        print ("Length of the secret word should be five.")
    elif word.isalpha()==False:
        print ("The word should be made of characters only.")
    elif len(set(word))!=5:
        print ("Repetition of characters isn't allowed")
                
                
        
