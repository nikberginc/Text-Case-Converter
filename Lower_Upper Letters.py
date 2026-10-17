i = 0
new_word = ""
dot = False
space = False
count = 0



#program asks for the text
word = input("Give your text:\n")




#loop will continue until the user inserts a valid option
while True:
    type = input("\nType 'UP' for all letters to be upper case;\nType 'LOW' for all letters to be lower case;\nType 'DOT' for all letters to be upper case after the dot;\nType 'DOTS' for all letters to be lower case after the dot\n\n")


    #program will check for all posabilitys and if nothink is maching it will restart the loop



    #algoritem for input UP
    if type.lower() == "up":

        #will go throu all of the letters and change them in upper
        for i in range(len(word)):

            new_word += (word[i]).upper()
        
        print("\n\033[4mYour text is now converted to a FULL UPPER CASE\033[0m\n\n"+new_word)
        break




    #algoritem for input LOW
    elif type.lower() == "low":

        #will go throu all of the letters and change them in lower
        for i in range(len(word)):

            new_word += (word[i]).lower()
        
        print("\n\033[4mYour text is now converted to a FULL LOWER CASE\033[0m\n\n"+new_word)
        break




    #algoritem for input DOT
    elif type.lower() == "dot":

        #will go throu all of the letters and change them in upper if they are next to dot='.'
        for i in range(len(word)):

            if count == 2:
                count = 0


            #add word to new word
            new_word += (word[i])
            letter = ord(word[i])


            #will check if dot is the letter and then  it will enable dot=True, if space is next it will enable space=True and if letter is between 96 and 123 after dot and space it will be upper
            if letter == 46 or dot:
                dot = True

                #checks for spaces
                if letter == 32 or space:
                    space = True

                    #checks for ASCII
                    if letter >96 and letter<123:
                        
                        #deletes the letter and then adds it back but now its upper case
                        new_word = new_word[:-1]

                        new_word += (word[i]).upper()

                        space = False
                        dot = False
                        count = 0
                        continue


                    # if after spaces the isnt a 96-123 ASCII code, it will close the routs to the algoritem
                    elif letter != 32:

                        space = False
                        dot = False
                        count = 0
                        continue                        

                
                #if space isnt after the dot it will close all routs to the algoritem
                else:
                    count+=1
                    if count >1:
                        dot = False

        print("\nConverted text:\n" + new_word)
        break
                        




    #algoritem for input DOTS
    elif type.lower() == "dots":

        #will go throu all of the letters and change them in upper if they are next to dot='.'
        for i in range(len(word)):

            if count == 2:
                count = 0


            #add word to new word
            new_word += (word[i])
            letter = ord(word[i])


            #will check if dot is the letter and then  it will enable dot=True, if space is next it will enable space=True and if letter is between 96 and 123 after dot and space it will be upper
            if letter == 46 or dot:
                dot = True

                #checks for spaces
                if letter == 32 or space:
                    space = True

                    #checks for ASCII
                    if letter >=65 and letter<=90:
                        
                        #deletes the letter and then adds it back but now its upper case
                        new_word = new_word[:-1]

                        new_word += (word[i]).lower()

                        space = False
                        dot = False
                        count = 0
                        continue


                    # if after spaces the isnt a 96-123 ASCII code, it will close the routs to the algoritem
                    elif letter != 32:

                        space = False
                        dot = False
                        count = 0
                        continue                        

                
                #if space isnt after the dot it will close all routs to the algoritem
                else:
                    count+=1
                    if count >1:
                        dot = False



        
        print("\n\033[4mYour text is now converted to UPPER CASE AFTER DOTs\033[0m\n\n"+new_word)
        break

    else:
        print("\n\033[4mYou used the wrong comand, please try again!\033[0m")
        continue


