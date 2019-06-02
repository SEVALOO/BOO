
# coding: utf-8

# In[ ]:


import random    # here it allows us to use the benefits of the functions random.
#function 1 which is just a screen organized wordings
def screen():
    screeninstructions()
    name = input("Your Name :  ")
    print('Welcome', name, 'This is a simple guessing game')
    print('____________________________________________________')
    print('Now', name, 'let the guessing begin with only 9 tries')
    print('make them count, lets goooo')
    #calling out the function
    hangman()
    print()
#second functions that tells the person or the player a random fact as a treat of guessing correct
def randomfact(animal):
    if animal == 'cheeta':
        print("did you know that cheetas reaches their max speed which is 65mph")
    elif animal == 'lion' :
        print("a lion's claws can reach lengths of up to 1.5 inches")
    elif animal == 'crocodile' :
        print("the smallest crocodile species is the dwarf crocodile which can be 5 feet in length and weigh up to 40-70lb")
    elif animal == 'giraff' :
        print("Giraffe's can eat 70-80 pounds of leaves a day and feed 16-20 hours")
    elif animal == 'monkey' :
        print("There are currently 264 known monkey species, but there are others to discover!")
    elif animal == 'zeebra' :
        print("Did you know that every zebra has a unique pattern of black and white stripes")
    elif animal == 'deer' :
        print("Each year, antlers fall off and regrow")
    elif animal == 'penguin' :
        print("The fastest species is the Gentoo Penguin, which can reach swimming speeds up to 22 mph")
    elif animal == 'Magpies' :
        print("Magpies Dont Like Shiny Things — They are Scared of Them because that is how their survival nature taught them")
    elif animal == 'parrot':
        print("Parrots are intelligent birds and like us humans they have feelings and can get sad and throw tantrums, fun right!")
    elif animal == 'camel' :
        print("Camels rarely sweat, even when ambient temperatures reach 49 °C and their title is The Ship Of The Desert")
    elif animal == 'leapord' :
        print("Sadly Leopards are predominantly solitary animals that have large territories and they fight to the death")
    elif animal == 'gazelle' :
        print("The tiny Thompsons gazelle's exhibit the very distinctive behavior of stotting which is jumping up to 10 feet")
    
    #a third function of the screeen before entering the game. explains the guesser what will happen.  
def screeninstructions():
    print('instructions:')
    print('you will have 9 trials to guess what word has been picked')
    print('each mistak will cause you to lose a limb, be careful!')
    print('once the correct asnwer is found, you will learn a random fact about the animal')
    
    #main function which is all the actoin happens.
def hangman():
    #random picks one of these randomly
    word = random.choice(['crocodile','lion','cheeta', 'giraff', 'monkey','magpies', 'zeebra', 'deer', 'penguin','camel',
'leapord', 'gazelle','parrot'])
    #choosing randomly strictly only letters
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #setting turns to 9 and slowly decreasing it to 0
    turns = 9
    guessed = ''  #letters that are used by the player will be added here
    #conditional to keep going if input is still empty
    while len(word) > 0 :
        empty_string = ''
        #missed trials which are zero then increased by 1 each time the guess is wrong
        missed = 0
        #conditional if word is one of the letters then add the letter to the empty string
        for letter in word:
            if letter in guessed:
                empty_string = empty_string + letter
            else:
                empty_string = empty_string + '_ ' + ''
                missed = missed + 1 #where the missed trials are increased after each attempt
        #if it is a word from the list then print the letter which is all the letters guessed if were correct
        if empty_string == word:
            print(empty_string)
            #funfact about the animal they guessed
            print("")
            print('Marvelous!you are correct! the word was', word)
            print("")
            print('fun fact about', word)
            print('')
            #calling the function randomfact onto word
            randomfact(word)
            break #stop the loop if his right
        print("Guessing Time! : ", empty_string) # other wise keep guessing
        guess = input().lower() #all ipnuts are lower cased even if user put upper case
        # if not a letter then will say invalid
        if guess in letters:
               guessed = guessed + guess 
        else :
            print('Enter a valid letter! : ')
            guess = input().lower() # again lower case every letter or input
            #if guessed incorrect then decreas his turns by one
        if guess not in word:
            turns = turns - 1
            if turns == 4:
                print("nice try but again")
                print('  o' )
            if turns == 3:
                print("come on think about it a little bit")
                print('  o')
                print(' / \'')
            if turns == 2:
                print("Third time a charm ok what about a fourth from the north!")
                print(' o')
                print('/|\'')
                print('/   ')  
            if turns == 1:
                print("OOOOOoooohhh so close dont lose hope")
                print('  o')
                print(' /|\ ')
                print(' / \ ')
                print('Your out of tries but good luck next time')
                break


# In[1]:


assert isinstance(random.choice, str)

