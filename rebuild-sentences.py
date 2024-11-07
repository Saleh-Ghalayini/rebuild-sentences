def rebuild_sentences(words, lengths):

    #defining a new empty list that will be the sentence after the extraction of each word from the words list
    sentence = []

    #looping through each word in the words list
    for i in range(len(words)):
            
            #extracting the specified length in the lengths list from the words list and appending it to the sentence list
            sentence.append(words[i][:lengths[i]])
    #joining the values of sentence so it would be displayed as a string and adding a space between each word        
    print(" ".join(sentence))

rebuild_sentences( [ "the", "sky", "is", "blue" ] , [ 3, 2, 2, 1 ] )    