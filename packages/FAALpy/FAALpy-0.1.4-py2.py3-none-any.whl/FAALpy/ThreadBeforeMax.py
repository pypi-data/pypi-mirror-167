import copy

def ThreadBeforeMax(bestPairs, sequence, matrixResultComparison, sequenceCount,  index):
		
		#// loop to build the matches - before max value
		for a in range(0, len(bestPairs)):
			bestPairs[a] = 0
		
		z = 0
		while (z < len(sequence)):
		#for z in range(0, len(sequence)):
			if (sequence[z][1] > 0 and sequence[z][2] > 0) :
				#// search for max values
				for n in range(0, sequence[z][2]):
					i = sequence[z][1] - 1
					for a in range(0, len(bestPairs)):
						if (matrixResultComparison[i][n] > 0 and matrixResultComparison[i][n] == bestPairs[a]) :
							break
						
						if (matrixResultComparison[i][n] < 0) :
							break
						
						if (matrixResultComparison[i][n] > bestPairs[a]) :
							if (a < len(bestPairs)) :
								for x in range(len(bestPairs)-1, a, -1):
									bestPairs[x] = bestPairs[x - 1]
								
							
							bestPairs[a] = matrixResultComparison[i][n]
							break
						
					
					
				
				
				for i in range(0, sequence[z][1]):
					n = sequence[z][2] - 1
					for a in range(0, len(bestPairs)):
						if (matrixResultComparison[i][n] > 0 and matrixResultComparison[i][n] == bestPairs[a]) :
							break
						
						if (matrixResultComparison[i][n] < 0) :
							break
						
						if (matrixResultComparison[i][n] > bestPairs[a]) :
							if (a < len(bestPairs)) :
								for x in range(len(bestPairs) -1, a, -1):
									bestPairs[x] = bestPairs[x - 1]
								
							
							bestPairs[a] = matrixResultComparison[i][n]
							break
						
					
					
				
				
				#// - store max values
				for i in range(0, sequence[z][1]):
					for n in range(0, sequence[z][2]):
						for x in range(0, len(bestPairs)):
							if (matrixResultComparison[i][n] == bestPairs[x]) :

								sequenceData = [ sequenceCount, i, n, matrixResultComparison[i][n], index, z, 0 ]
								sequence.append(copy.deepcopy(sequenceData))
								sequenceCount += 1
								index += 1








				for a in range(0, len(bestPairs)):
					bestPairs[a] = 0

			else :
				sequence[z][6] = 1

			z += 1


		
		return sequence


