import copy

def ThreadInitialSeq(initialSeqs, sequence, line1, word1,  line2,  word2,  nextCharacter) :
		
	
		
		listWord1PreTemp = []
		listWord2PreTemp = []

		

		for z in range(0, len(sequence)):

			if (sequence[z][6] == 1) :

				listLine1 = []
				listLine2 = []

				item1 = []
				item2 = []

				line1 = line1 + word1[sequence[z][1]]
				line2 = line2 + word2[sequence[z][2]]

				listLine1.append(copy.deepcopy(sequence[z][1]))
				listLine2.append(copy.deepcopy(sequence[z][2]))

				nextCharacter = sequence[z][5]


				for i in range(len(sequence)-1, -1, -1):

					if (sequence[i][4] == nextCharacter) :
						nextCharacter = sequence[i][5]
						listLine1.append(copy.deepcopy(sequence[i][1]))
						listLine2.append(copy.deepcopy(sequence[i][2]))

						line1 = line1 + word1[sequence[i][1]]
						line2 = line2 + word2[sequence[i][2]]
					

				

				gap = 0
				difference = 0

				line1 = line1 + ":"
				line2 = line2 + ":"

				for i in range(0, len(listLine1)):
					if i != 0:
						difference = (listLine1[i] - listLine1[i - 1]) - (listLine2[i] - listLine2[i - 1])
					else :
						difference = listLine1[i] - listLine2[i]

					if (difference == 0) :
						if (i == 0) :
							line1 = line1 + word1[listLine1[i]]
							line2 = line2 + word2[listLine2[i]]
							item1.append(copy.deepcopy(listLine1[i]))
							item2.append(copy.deepcopy(listLine2[i]))
						else :
							gap = listLine1[i] - listLine1[i - 1]
							if (gap == 1) :
								line1 = line1 + "-" + word1[listLine1[i]]
								line2 = line2 + "-" + word2[listLine2[i]]
								item1.append(copy.deepcopy(listLine1[i]))
								item2.append(copy.deepcopy(listLine2[i]))
							elif (gap > 1) :
								for n in range (1, gap) :
									line1 = line1 + word1[listLine1[i - 1] + n] + "-0"
									line2 = line2 + "-0" + word2[listLine2[i - 1] + n]
									item1.append(copy.deepcopy(listLine1[i - 1] + n))
									item1.append(copy.deepcopy(-1))
									item2.append(copy.deepcopy(-1))
									item2.append(copy.deepcopy(listLine2[i - 1] + n))


								line1 = line1 + "-" + word1[listLine1[i]]
								line2 = line2 + "-" + word2[listLine2[i]]
								item1.append(copy.deepcopy(listLine1[i]))
								item2.append(copy.deepcopy(listLine2[i]))




					if (difference < 0) :

						if (i > 0) :
							gap = listLine1[i] - listLine1[i - 1]

						if (gap > 1) :
							for n in range(1, gap):
								line1 = line1 + "-" + word1[listLine1[i - 1] + n] + "-0"
								line2 = line2 + "-0-" + word2[listLine2[i - 1] + n]
								item1.append(copy.deepcopy(listLine1[i - 1] + n))
								item1.append(copy.deepcopy(-1))
								item2.append(copy.deepcopy(-1))
								item2.append(copy.deepcopy(listLine2[i - 1] + n))


						#// ----
						for n in range(-1 * difference, 0, -1):
							line1 = line1 + "-0"
							line2 = line2 + "-" + word2[listLine2[i] - n]
							item1.append(copy.deepcopy(-1))
							item2.append(copy.deepcopy(listLine2[i] - n))


						line1 = line1 + "-" + word1[listLine1[i]]
						line2 = line2 + "-" + word2[listLine2[i]]
						item1.append(copy.deepcopy(listLine1[i]))
						item2.append(copy.deepcopy(listLine2[i]))
						#// -------

					elif (difference > 0) :

						if (i > 0) :
							gap = listLine2[i] - listLine2[i - 1]

						if (gap > 1) :
							for n in range(1, gap):
								line1 = line1 + "-" + word1[listLine1[i - 1] + n] + "-0"
								line2 = line2 + "-0-" + word2[listLine2[i - 1] + n]
								item1.append(copy.deepcopy(listLine1[i - 1] + n))
								item1.append(copy.deepcopy(-1))
								item2.append(copy.deepcopy(-1))
								item2.append(copy.deepcopy(listLine2[i - 1] + n))


						#// ----
						for n in range(difference, 0, -1):
							line2 = line2 + "-0"
							line1 = line1 + "-" + word1[listLine1[i] - n]
							item2.append(copy.deepcopy(-1))
							item1.append(copy.deepcopy(listLine1[i] - n))


						line1 = line1 + "-" + word1[listLine1[i]]
						line2 = line2 + "-" + word2[listLine2[i]]
						item1.append(copy.deepcopy(listLine1[i]))
						item2.append(copy.deepcopy(listLine2[i]))
						#// -------



				
				gap = 0
				difference = 0

				line1 = ""
				line2 = ""

				alreadyListed_Pre = False

				for g in range(0, len(listWord1PreTemp)):
					if (listWord1PreTemp[g] == (item1) and listWord2PreTemp[g] == (item2)) :
						alreadyListed_Pre = True
						break



				if (alreadyListed_Pre == False) :
					listWord1PreTemp.append(copy.deepcopy(item1))
					listWord2PreTemp.append(copy.deepcopy(item2))
					alreadyListed_Pre = True



			


		
		initialSeqs.append(copy.deepcopy(listWord1PreTemp))
		initialSeqs.append(copy.deepcopy(listWord2PreTemp))
		
		
		
		return initialSeqs
		
		

		




