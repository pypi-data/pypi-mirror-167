import copy

def ThreadAfterMax(lengthWord1, lengthWord2, bestPairs, sequence_Tail, matrixResultComparison, sequenceCount_Tail, index_Tail):


    #// =========
    #// loop to build the matches - after max value
    for a in range(0, len(bestPairs)):
        bestPairs[a] = 0
    
    z = 0
    while (z < len(sequence_Tail)):
    #for z in range(0, len(sequence_Tail)):
        for a in range(0, len(bestPairs)):
            bestPairs[a] = 0
        
        if (sequence_Tail[z][1] + 1 < lengthWord1 and sequence_Tail[z][2] + 1 < lengthWord2) :
            #// search for max values
            for i in range(sequence_Tail[z][1] + 1, lengthWord1):
                n = sequence_Tail[z][2] + 1
                #// for(int n = sequence_Tail[z][2]+1; n < lengthWord2; n++){
                #// int check = 0;
                for a in range(0, len(bestPairs)):
                    #// check = matrixResultComparison[i][n];
                    if (matrixResultComparison[i][n] > 0 and matrixResultComparison[i][n] == bestPairs[a]) :
                        break

                    if (matrixResultComparison[i][n] < 0) :
                        break

                    if (matrixResultComparison[i][n] > bestPairs[a]) :
                        if (a < len(bestPairs)) :
                            for x in range(len(bestPairs) - 1, a, -1):
                                bestPairs[x] = bestPairs[x - 1]


                        bestPairs[a] = matrixResultComparison[i][n]
                        break



                #// };



            #// for(int i = sequence_Tail[z][1]+1; i < lengthWord1; i++){

            for n in range(sequence_Tail[z][2] + 1, lengthWord2):
                i = sequence_Tail[z][1] + 1
                #// int check = 0;
                for a in range(0, len(bestPairs)):
                    #// check = matrixResultComparison[i][n];
                    if (matrixResultComparison[i][n] > 0 and matrixResultComparison[i][n] == bestPairs[a]) :
                        break

                    if (matrixResultComparison[i][n] < 0) :
                        break

                    if (matrixResultComparison[i][n] > bestPairs[a]) :
                        if (a < len(bestPairs)):
                            for x in range (len(bestPairs)-1, a, -1):
                                bestPairs[x] = bestPairs[x - 1]


                        bestPairs[a] = matrixResultComparison[i][n]
                        break



                #// };


            #// ---- store max values
            for i in range(sequence_Tail[z][1] + 1, lengthWord1):
                for n in range(sequence_Tail[z][2] + 1, lengthWord2):
                    for x in range(0, len(bestPairs)):
                        if (matrixResultComparison[i][n] == bestPairs[x]) :

                            sequenceData_Tail = [ sequenceCount_Tail, i, n, matrixResultComparison[i][n],
                                    index_Tail, z, 0 ]
                            sequence_Tail.append(copy.deepcopy(sequenceData_Tail))
                            sequenceCount_Tail += 1
                            index_Tail += 1








            for a in range(0, len(bestPairs)):
                bestPairs[a] = 0

        else:
            sequence_Tail[z][6] = 9

        for a in range(0, len(bestPairs)):
            bestPairs[a] = 0

        z += 1




    return sequence_Tail


