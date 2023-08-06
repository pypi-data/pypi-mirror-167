import copy

def ThreadTailSeq(lengthWord1, lengthWord2, tailSeqs, sequence_Tail, line1, word1, line2, word2, nextCharacter_Tail):
        
    
    listWord1PostTemp= []
    listWord2PostTemp= []
    
    #// System.out.println("-------");
    #// build final sequence
    for z in range(0, len(sequence_Tail)):
        if (sequence_Tail[z][6] == 9) :

            line1Tail_Inverted= []
            line2Tail_Inverted= []
            line1_Tail= []
            line2_Tail= []

            item1_2 = []
            item2_2 = []

            line1Tail_Inverted.append(copy.deepcopy(sequence_Tail[z][1]))
            line2Tail_Inverted.append(copy.deepcopy(sequence_Tail[z][2]))

            nextCharacter_Tail = sequence_Tail[z][5]

            for i in range(len(sequence_Tail) - 1, -1,-1) :

                if (sequence_Tail[i][4] == nextCharacter_Tail) :
                    nextCharacter_Tail = sequence_Tail[i][5]
                    line1Tail_Inverted.append(copy.deepcopy(sequence_Tail[i][1]))
                    line2Tail_Inverted.append(copy.deepcopy(sequence_Tail[i][2]))

                

            

            for i in range(len(line1Tail_Inverted) - 1,-1,-1):
                line1_Tail.append(copy.deepcopy(line1Tail_Inverted[i]))
                line2_Tail.append(copy.deepcopy(line2Tail_Inverted[i]))
            

            for i in range(0, len(line1Tail_Inverted)):
                line1 = line1 + word1[line1Tail_Inverted[i]]
                line2 = line2 + word2[line2Tail_Inverted[i]]


            gap = 0
            difference = 0

            line1 = line1 + "::"
            line2 = line2 + "::"

            for i in range(0, len(line1_Tail)):
                if (i == 0) :
                    difference = line1_Tail[i] - line2_Tail[i]
                else:
                    difference = (line1_Tail[i] - line1_Tail[i - 1]) - (line2_Tail[i] - line2_Tail[i - 1])



                if (difference == 0) :
                    if (i == 0) :
                        line1 = line1 + word1[line1_Tail[i]]
                        line2 = line2 + word2[line2_Tail[i]]
                        item1_2.append(copy.deepcopy(line1_Tail[i]))
                        item2_2.append(copy.deepcopy(line2_Tail[i]))

                    else :
                        gap = line1_Tail[i] - line1_Tail[i - 1]
                        if (gap == 1) :
                            line1 = line1 + "-" + word1[line1_Tail[i]]
                            line2 = line2 + "-" + word2[line2_Tail[i]]
                            item1_2.append(copy.deepcopy(line1_Tail[i]))
                            item2_2.append(copy.deepcopy(line2_Tail[i]))

                        elif (gap > 1) :
                            for n in range(1, gap):
                                line1 = line1 + "-" + word1[line1_Tail[i - 1] + n] + "-0"
                                line2 = line2 + "-0-" + word2[line2_Tail[i - 1] + n]
                                item1_2.append(copy.deepcopy(line1_Tail[i - 1] + n))
                                item1_2.append(copy.deepcopy(-1))
                                item2_2.append(copy.deepcopy(-1))
                                item2_2.append(copy.deepcopy(line2_Tail[i - 1] + n))


                            line1 = line1 + "-" + word1[line1_Tail[i]]
                            line2 = line2 + "-" + word2[line2_Tail[i]]
                            item1_2.append(copy.deepcopy(line1_Tail[i]))
                            item2_2.append(copy.deepcopy(line2_Tail[i]))



                
                if (difference < 0) :

                    if (i > 0) :
                        gap = line1_Tail[i] - line1_Tail[i - 1]
                    
                    if (gap > 1) :
                        for n in range(1, gap):
                            line1 = line1 + "-" + word1[line1_Tail[i - 1] + n] + "-0"
                            line2 = line2 + "-0-" + word2[line2_Tail[i - 1] + n]
                            item1_2.append(copy.deepcopy(line1_Tail[i - 1] + n))
                            item1_2.append(copy.deepcopy(-1))
                            item2_2.append(copy.deepcopy(-1))
                            item2_2.append(copy.deepcopy(line2_Tail[i - 1] + n))
                        
                    
                    #// ----
                    for n in range(-1 * difference, 0, -1):
                        if (len(item1_2) > 0) :
                            line1 = line1 + "-0"
                            line2 = line2 + "-" + word2[line2_Tail[i] - n]
                            item1_2.append(copy.deepcopy(-1))
                            item2_2.append(copy.deepcopy(line2_Tail[i] - n))
                        
                    

                    line1 = line1 + "-" + word1[line1_Tail[i]]
                    line2 = line2 + "-" + word2[line2_Tail[i]]
                    item1_2.append(copy.deepcopy(line1_Tail[i]))
                    item2_2.append(copy.deepcopy(line2_Tail[i]))
                    #// -------

                elif (difference > 0) :

                    if (i > 0) :
                        gap = line2_Tail[i] - line2_Tail[i - 1]
                    
                    if (gap > 1) :
                        for n in range(1, gap):
                            line1 = line1 + "-" + word1[line1_Tail[i - 1] + n] + "-0"
                            line2 = line2 + "-0-" + word2[line2_Tail[i - 1] + n]
                            item1_2.append(copy.deepcopy(line1_Tail[i - 1] + n))
                            item1_2.append(copy.deepcopy(-1))
                            item2_2.append(copy.deepcopy(-1))
                            item2_2.append(copy.deepcopy(line2_Tail[i - 1] + n))


                    #// ----
                    for n in range(difference, 0, -1):
                        if (len(item1_2) > 0) :
                            line2 = line2 + "-0"
                            line1 = line1 + "-" + word1[line1_Tail[i] - n]
                            item2_2.append(copy.deepcopy(-1))
                            item1_2.append(copy.deepcopy(line1_Tail[i] - n))



                    line1 = line1 + "-" + word1[line1_Tail[i]]
                    line2 = line2 + "-" + word2[line2_Tail[i]]
                    item1_2.append(copy.deepcopy(line1_Tail[i]))
                    item2_2.append(copy.deepcopy(line2_Tail[i]))
                    #// -------





            if (item1_2[len(item1_2) - 1] != lengthWord1 - 1) :
                for i in range(item1_2[len(item1_2) - 1] + 1, lengthWord1):
                    item1_2.append(copy.deepcopy(i))
                    item2_2.append(copy.deepcopy(-1))
                    line1 = line1 + ":" + word1[i]
                    line2 = line2 + "-0"

            elif (item2_2[len(item2_2) - 1] != (lengthWord2 - 1)) :
                for i in range(item2_2[len(item2_2) - 1] + 1, lengthWord2):
                    item1_2.append(copy.deepcopy(-1))
                    item2_2.append(copy.deepcopy(i))
                    line1 = line1 + "-0"
                    line2 = line2 + ":" + word2[i]



            gap = 0
            difference = 0

            line1 = ""
            line2 = ""

            alreadyListed_Post = False
            for g in range(0, len(listWord1PostTemp)) :
                if (listWord1PostTemp[g] == (item1_2) and listWord2PostTemp[g] == (item2_2)) :
                    alreadyListed_Post = True
                    break



            if (alreadyListed_Post == False) :
                listWord1PostTemp.append(copy.deepcopy(item1_2))
                listWord2PostTemp.append(copy.deepcopy(item2_2))
                alreadyListed_Post = True




    
    
    tailSeqs.append(copy.deepcopy(listWord1PostTemp))
    tailSeqs.append(copy.deepcopy(listWord2PostTemp))
    
    
    
    return tailSeqs
		
		
		





