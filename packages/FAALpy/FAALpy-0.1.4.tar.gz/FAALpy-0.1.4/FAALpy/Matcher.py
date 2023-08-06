#/*
# * Copyright 2018 Marwan Kilani
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *    http:#//www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# */

from threading import Thread

import os

from multiprocessing.pool import ThreadPool

from .MatcherConfig1 import *
from .MatcherConfig2 import *
from .MatcherConfig3 import *
from .MatcherConfig4 import *

from .Reader import *

from .Alignment import *

import copy

from .ThreadAfterMax import *
from .ThreadBeforeMax import *
from .ThreadInitialSeq import *
from .ThreadTailSeq import *

import numexpr

from pathlib import Path


def calculateFeaturesInCommon(option, sumFeaturesInCommon, valuePairFromComparisonMatrix):
	if option == 0:
		empty = 0
	# // nothing
	elif (option == 1):
		sumFeaturesInCommon = sumFeaturesInCommon + valuePairFromComparisonMatrix
	elif (option == 2):
		sumFeaturesInCommon = sumFeaturesInCommon - 1

	return sumFeaturesInCommon


def findTypeOfMatch(i, n, matchWord1, matchWord2, word1, word2):
	typeLetterWord1 = ""
	typeLetterWord2 = ""
	typeCombined = ""

	# // ----

	if (matchWord1[i][n] <= -1):

		typeLetterWord1 = "0"

	elif (matchWord1[i][n] > -1):

		if ((word1[matchWord1[i][n]]) == ("￤")):

			typeLetterWord1 = "￤"

		elif (not (word1[matchWord1[i][n]]) == ("￤")):

			typeLetterWord1 = "x"

	# // -----

	if (matchWord2[i][n] <= -1):

		typeLetterWord2 = "0"

	elif (matchWord2[i][n] > -1):

		if ((word2[matchWord2[i][n]]) == ("￤")):

			typeLetterWord2 = "￤"

		elif (not (word2[matchWord2[i][n]]) == ("￤")):

			typeLetterWord2 = "x"

	typeCombined = typeLetterWord1 + typeLetterWord2

	return typeCombined


def countMorphemicBoundaries(a, b, c, word1, word2):  # // b limite
	# // conto non
	# // incluso,
	# // ultimo è
	# // b-1 #// b
	# // per
	# // parola 1,
	# // c per
	# // parola 2

	nrMorphemicBoundariesWord1 = 0
	nrMorphemicBoundariesWord2 = 0
	highestNrMorphemicBoundaries = 0

	for i in range(a, b):

		if ((word1[i]) == ("￤")):
			nrMorphemicBoundariesWord1 += 1

	for i in range(a, c):
		if ((word2[i]) == ("￤")):
			nrMorphemicBoundariesWord2 += 1

	if (nrMorphemicBoundariesWord1 >= nrMorphemicBoundariesWord2):

		highestNrMorphemicBoundaries = nrMorphemicBoundariesWord1
	else:

		highestNrMorphemicBoundaries = nrMorphemicBoundariesWord2

	resultsNrsMorphemicBoundaries = []

	resultsNrsMorphemicBoundaries.append(copy.deepcopy(highestNrMorphemicBoundaries))
	resultsNrsMorphemicBoundaries.append(copy.deepcopy(nrMorphemicBoundariesWord1))
	resultsNrsMorphemicBoundaries.append(copy.deepcopy(nrMorphemicBoundariesWord2))

	return resultsNrsMorphemicBoundaries


def buildWord(word, unparsedWord, locationFilePhoneticDiacritics):
	# // read diacritics

	filePhoneticDiacriticsLines = []

	filePhoneticDiacriticsRead = Reader.readFile(locationFilePhoneticDiacritics)

	filePhoneticDiacriticsLinesProvisional = filePhoneticDiacriticsRead.split("\n")

	for i in range(0, len(filePhoneticDiacriticsLinesProvisional)):

		if (filePhoneticDiacriticsLinesProvisional[i].find("%") < 0):
			filePhoneticDiacriticsLines.append(copy.deepcopy(filePhoneticDiacriticsLinesProvisional[i]))

	filePhoneticDiacriticsLines.append(
		copy.deepcopy("̯	2	0;1"))  # // marked with 2 to distinguish it from normal diacritics
	filePhoneticDiacriticsLines.append(
		copy.deepcopy("͜	3	0;2"))  # // marked with 3 to distinguish it from normal diacritics

	valuesPhoneticDiacritics = []
	classPhoneticDiacritics = []

	phoneticDiacritics_FeaturesChanged = []
	phoneticDiacritics_FeaturesChangedValue = []

	for i in range(0, len(filePhoneticDiacriticsLines)):
		diacrititics_Split1 = []
		diacrititics_Split2 = []
		diacrititics_Split3 = []

		featuresChanged = []
		featuresChangedValue = []

		diacrititics_Split1 = filePhoneticDiacriticsLines[i].split("	")
		diacrititics_Split2 = diacrititics_Split1[2].split(" ")

		valuesPhoneticDiacritics.append(copy.deepcopy(diacrititics_Split1[0]))
		classPhoneticDiacritics.append(copy.deepcopy(diacrititics_Split1[1]))

		for n in range(0, len(diacrititics_Split2)):
			diacrititics_Split3 = diacrititics_Split2[n].split(";")
			featuresChanged.append(copy.deepcopy(diacrititics_Split3[0]))
			featuresChangedValue.append(copy.deepcopy(diacrititics_Split3[1]))

		phoneticDiacritics_FeaturesChanged.append(copy.deepcopy(featuresChanged))
		phoneticDiacritics_FeaturesChangedValue.append(copy.deepcopy(featuresChangedValue))

	segment = ""
	splittedWord = list(word)
	splittedUnparsedWord = list(unparsedWord)

	for r in range(0, len(splittedUnparsedWord)):

		if (splittedUnparsedWord[r] == ("͜")):
			letter_A = splittedUnparsedWord[r - 1]
			splittedUnparsedWord[r - 1] = splittedUnparsedWord[r + 1]
			splittedUnparsedWord[r + 1] = letter_A

	result = ""
	sequenceInitialDiacritics = ""

	for z in range(0, len(unparsedWord)):
		initialDiacritic = False
		for m in range(0, len(classPhoneticDiacritics)):

			if (classPhoneticDiacritics[m] == ("1")):

				if ((unparsedWord[z]) == (valuesPhoneticDiacritics[m])):
					initialDiacritic = True
					sequenceInitialDiacritics = sequenceInitialDiacritics + valuesPhoneticDiacritics[m]

		if (initialDiacritic == False):
			break

	g = len(splittedUnparsedWord) - 1

	for i in range(len(splittedWord)-1, -1, -1):
		if (splittedWord[i] == ("0")):
			segment = "	0" + segment

		elif (splittedWord[i] == ("┊")):
			segment = "┊" + segment

		elif (splittedWord[i] == ("·")):
			segment = "·" + segment

		elif (splittedWord[i] == (";")):
			segment = ";" + segment

		elif not (splittedWord[i] == (":")):

			for n in range(g, -1, -1):
				segment = splittedUnparsedWord[n] + segment
				if (splittedWord[i] == (splittedUnparsedWord[n])):
					if (i > 0):
						result = "	" + segment + result
					else:
						result = segment + result

					segment = ""
					g = n - 1
					break

	result = segment + result
	result = result.replace("	", "", 1)

	result = sequenceInitialDiacritics + result

	result = result.replace(sequenceInitialDiacritics + "┊", "┊" + sequenceInitialDiacritics)
	result = result.replace(sequenceInitialDiacritics + "0", "0" + sequenceInitialDiacritics)

	for m in range(0, len(classPhoneticDiacritics)):
		precedingDiacritic = ""

		if (classPhoneticDiacritics[m] == ("1")):

			for z in range(0, len(result)):
				precedingDiacritic = valuesPhoneticDiacritics[m]

				result = result.replace(precedingDiacritic + "	0", "	0" + precedingDiacritic)

				result = result.replace(precedingDiacritic + "┊	0", "┊	0" + precedingDiacritic)

	for i in range(0, len(result)):

		if (result[i:i + 1] == ("͜")):
			letter_A = result[i - 1:i]
			result = result[0:i - 1] + result[i + 1:i + 2] + "͜" + letter_A + result[i + 2:len(result)]
			i = i + 1

	for z in range(0, len(result)):

		for i in range(0, len(classPhoneticDiacritics)):
			if (classPhoneticDiacritics[i] == ("1")):
				result = result.replace(valuesPhoneticDiacritics[i] + "	", "	" + valuesPhoneticDiacritics[i])
				result = result.replace(valuesPhoneticDiacritics[i] + "┊	", "┊	" + valuesPhoneticDiacritics[i])

	return result


class Matcher :








#	/**
#	 * Method corresponding to the Matcher module. It parses one pair of words at a
#	 * time, using default values (see online documentation for their values). It
#	 * returns an array list of possible alignments organized according to their
#	 * Global Similarity Score.
#	 *
#	 * @param word1Parsed
#	 *            (String): parsed (i.e. without diacritics etc) transcription of
#	 *            word A (returned by IPA_parser.IPA_parser_new - output 0).
#	 * @param word2Parsed
#	 *            (String): parsed (i.e. without diacritics etc) transcription of
#	 *            word B (returned by IPA_parser.IPA_parser_new - output 1).
#	 * @param matrixResultComparison
#	 *            (int[][]): matching features matrix corrected according to the
#	 *            salience settings (returned by IPA_parser.IPA_parser_new - output
#	 *            2).
#	 * @param matrixResultComparisonOriginal
#	 *            (int[][]): basic matching features matrix with- out any salience
#	 *            corrections (returned by IPA_parser.IPA_parser_new - output 3).
#	 * @param word1Unparsed
#	 *            (String): IPA transcription of the first word to be aligned.
#	 * @param word2Unparsed
#	 *            (String): IPA transcription of the second word to be aligned.
#	 * @return Result output: Listandlt;Alignmentandgt;
#	 *         <p>
#	 *         <p>
#	 *         Each <i>Alignment</i > item within the List corresponds to an
#	 *         alignment obtained. They are organized according to their Global or Corrected
#	 *         Global Similarity score (see documentation online).
#	 *         The items stored in the <i>Alignment</i > class can be called as follow:
#	 *         <p>
#	 *         <p>
#	 *         0. .getWord1_WithDiacritics() - String: Returns the aligned word 1, with diacritics.
#	 *         <p>
#	 *         1. .getWord2_WithDiacritics() - String: Returns the aligned word 2, with diacritics.
#	 *         <p>
#	 *         2. .getWord1_WithoutDiacritics() - String: Returns the aligned word 1, without diacritics.
#	 *         <p>
#	 *         3. .getWord2_WithoutDiacritics() - String: Returns the aligned word 2, without diacritics.
#	 *         <p>
#	 *         4. .getGlobalSimilarityScore() - Double: Returns the Global Similarity Score.
#	 *         <p>
#	 *         5. .getCorrectedGlobalSimilarityScore() - Double: Returns the Corrected Global Similarity Score.
#	 *         <p>
#	 *         6. .getPhoneticPairs() - Listandlt;Stringandgt;: Returns the list of phonetic pairs attested within the
#	 *         alignment. Each item on the list corresponds to a phonetic pair, and
#	 *         it is stored as a with the following syntax: "phoneme_A -
#	 *         phoneme_B"
#	 *         <p>
#	 *         7. .getNrAttestationsPhoneticPairs() - Listandlt;Integerandgt;: Returns the number of attestations within the alignment
#	 *         for each phonetic pair of po6. here above.
#	 *         <p>
#	 * @throws ExecutionException
#	 * @throws InterruptedException
#	 */


	def match(*args):

		if len(args) == 6:
			word1Parsed = args[0]
			word2Parsed = args[1]
			matrixResultComparison = args[2]
			matrixResultComparisonOriginal = args[3]
			word1Unparsed = args[4]
			word2Unparsed = args[5]


			results = []
			matcherConfig1 = []
			matcherConfig2 = []
			matcherConfig3 = []
			matcherConfig4 = []

			settingsMatcherConfig1 = MatcherConfig1()
			settingsMatcherConfig2 = MatcherConfig2()
			settingsMatcherConfig3 = MatcherConfig3()
			settingsMatcherConfig4 = MatcherConfig4()

			#// Configs files:

			matcherConfig1 = settingsMatcherConfig1.getmatcherConfig1()
			matcherConfig2 = settingsMatcherConfig2.getmatcherConfig2()
			matcherConfig3 = settingsMatcherConfig3.getmatcherConfig3()
			matcherConfig4 = settingsMatcherConfig4.getmatcherConfig4()

			#// Parameters concerning the use of an external Corrected Global Similarity
			#// Score function

			#// use of an external function: 0 = use the default function/do not use any
			#// external function; 1 = use function from config file; 2 = use function from
			#// argument
			optionFunction = 0

			#// Since no function is passed as argument, the parameter externalFunction is
			#// "".
			#externalFunction = ""

			#results = match(word1Parsed, word2Parsed, matrixResultComparison, matrixResultComparisonOriginal, word1Unparsed,
			#		word2Unparsed, matcherConfig1, matcherConfig2, matcherConfig3, matcherConfig4, optionFunction,
			#		externalFunction)




		#// =========================
		#// =========================
		#// =========================

		#/**
	#	 * Method corresponding to the Matcher module. It parses one pair of words at a
	#	 * time, using personalized values (see online documentation for detailed
	#	 * description). It returns an array list of possible alignments organized
	#	 * according to their Global or Corrected Global Similarity Score, or according
	#	 * to an external function.
	#	 *
	#	 * @param word1Parsed
	#	 *            (String): parsed (i.e. without diacritics etc) transcription of
	#	 *            word A (returned by IPA_parser.IPA_parser_new - output 0).
	#	 * @param word2Parsed
	#	 *            (String): parsed (i.e. without diacritics etc) transcription of
	#	 *            word B (returned by IPA_parser.IPA_parser_new - output 1).
	#	 * @param matrixResultComparison
	#	 *            (int[][]): matching features matrix corrected according to the
	#	 *            salience settings (returned by IPA_parser.IPA_parser_new - output
	#	 *            2).
	#	 * @param matrixResultComparisonOriginal
	#	 *            (int[][]): basic matching features matrix with- out any salience
	#	 *            corrections (returned by IPA_parser.IPA_parser_new - output 3).
	#	 * @param word1Unparsed
	#	 *            (String): IPA transcription of the first word to be aligned.
	#	 * @param word2Unparsed
	#	 *            (String): IPA transcription of the second word to be aligned.
	#	 * @param matcherConfig1
	#	 *            (Listandlt;Booleanandgt;): array list with variables for the
	#	 *            configuration of the FAAL.faal and Matcher.Matcher_new modules.
	#	 *            Instances of this list can be initialized through the
	#	 *            <i>MatcherConfig1</i> class - see the corresponding JavaDoc, and
	#	 *            the documentation and examples online.
	#	 * @param matcherConfig2
	#	 *            (Listandlt;Integerandgt;): array list with variables for the
	#	 *            configuration of the FAAL.faal and Matcher.Matcher_new modules.
	#	 *            Instances of this list can be initialized through the
	#	 *            <i>MatcherConfig2</i> class - see the corresponding JavaDoc, and
	#	 *            the documentation and examples online.
	#	 * @param matcherConfig3
	#	 *            (Listandlt;Stringandgt;): array list with variables for the
	#	 *            configuration of the FAAL.faal and Matcher.Matcher_new modules.
	#	 *            Instances of this list can be initialized through the
	#	 *            <i>MatcherConfig3</i> class - see the corresponding JavaDoc, and
	#	 *            the documentation and examples online.
	#	 * @param matcherConfig4
	#	 *            (Listandlt;Doubleandgt;): array list storing the factors used
	#	 *            in the calculation of the Corrected Global Similarity score. It is
	#	 *            used in the configuration of the FAAL.faal and Matcher.Matcher_new
	#	 *            modules. Instances of this list can be initialized through the
	#	 *            <i>MatcherConfig4</i> class - see the corresponding JavaDoc, and
	#	 *            the documentation and examples online.
	#	 * @param optionFunction
	#	 *            (Integer): select if using or not an external function - 0 = do
	#	 *            not use external function; 1 = use external function from config.
	#	 *            folder; 2 = use function provided as next argument
	#	 * @param externalFunction
	#	 *            (String): alternative function to use for the calculation of the
	#	 *            Corrected Global Similarity Score. See readme.md and
	#	 *            config/external_corr_glob_sim_score_function.txt for details about
	#	 *            the options and syntax of the formula.
	#	 *
	#	 * @return Result output: Listandlt;Alignmentandgt;
	#	 *         <p>
	#	 *         <p>
	#	 *         Each <i>Alignment</i > item within the List corresponds to an
	#	 *         alignment obtained. They are organized according to their Global or Corrected
	#	 *         Global Similarity score (see documentation online).
	#	 *         The items stored in the <i>Alignment</i > class can be called as follow:
	#	 *         <p>
	#	 *         <p>
	#	 *         0. .getWord1_WithDiacritics() - String: Returns the aligned word 1, with diacritics.
	#	 *         <p>
	#	 *         1. .getWord2_WithDiacritics() - String: Returns the aligned word 2, with diacritics.
	#	 *         <p>
	#	 *         2. .getWord1_WithoutDiacritics() - String: Returns the aligned word 1, without diacritics.
	#	 *         <p>
	#	 *         3. .getWord2_WithoutDiacritics() - String: Returns the aligned word 2, without diacritics.
	#	 *         <p>
	#	 *         4. .getGlobalSimilarityScore() - Double: Returns the Global Similarity Score.
	#	 *         <p>
	#	 *         5. .getCorrectedGlobalSimilarityScore() - Double: Returns the Corrected Global Similarity Score.
	#	 *         <p>
	#	 *         6. .getPhoneticPairs() - Listandlt;Stringandgt;: Returns the list of phonetic pairs attested within the
	#	 *         alignment. Each item on the list corresponds to a phonetic pair, and
	#	 *         it is stored as a with the following syntax: "phoneme_A -
	#	 *         phoneme_B"
	#	 *         <p>
	#	 *         7. .getNrAttestationsPhoneticPairs() - Listandlt;Integerandgt;: Returns the number of attestations within the alignment
	#	 *         for each phonetic pair of po6. here above.
	#	 *         <p>
	#	 * @throws ExecutionException
	#	 * @throws InterruptedException
	#	 */
		
		if len(args) == 12:
			word1Parsed = args[0]
			word2Parsed = args[1]
			matrixResultComparison = args[2]
			matrixResultComparisonOriginal = args[3]
			word1Unparsed = args[4]
			word2Unparsed = args[5]

			matcherConfig1 = args[6]
			matcherConfig2 = args[7]
			matcherConfig3 = args[8]
			matcherConfig4 = args[9]

			optionFunction = args[10]
			externalFunction = args[11]

		indexPhoneticPairs = []
		indexPhoneticPairsValue = []

		attestedPhoneticPairs = []
		nrAttestationsPhoneticPairs = []

		word1 = word1Parsed
		word2 = word2Parsed


		#// read config 1

		printResults = matcherConfig1[0]
		limitMinimumFeaturesConsonants = matcherConfig1[1]
		limitMinimumFeaturesVowels = matcherConfig1[1]
		autodetectMorphologicalBoundaries = matcherConfig1[2]
		ignoreSemiconsonantMismatches = matcherConfig1[3]
		ignoreVowelsMismatches = matcherConfig1[4]
		ignoreVowelsMismatchesExceptFirst = matcherConfig1[5]
		displayAutomaticallyRecognizedMorphologicalBoundaries = matcherConfig1[6]
		matchesOnlyPhonesSameCategory = matcherConfig1[7]

		#// read config 2

		selectSimilarityScore = matcherConfig2[0] #// if 0 = use globalSimilaryScore, if 1 = use
															#// correctedGlobalSimilaryScore
		limitSignificanceConsonants = matcherConfig2[1]
		limitSignificanceVowels = matcherConfig2[2]
		nrTrialsWithMorphemicBoundaries = matcherConfig2[3]
		nrTrialsWithoutMorphemicBoundaries = matcherConfig2[4]

		#// read config 3

		locationFileFeatures = matcherConfig3[0]#// phon_features.txt
		locationFileCategoriesPhones = matcherConfig3[1]#// "cons_vows_semi.txt";
		locationFilePhoneticDiacritics = matcherConfig3[2]#// "phon_diacritics.txt";

		#// read config 4

		factors = []

		for z in range(0, len(matcherConfig4)):

			factors.append(copy.deepcopy(matcherConfig4[0]))




		#// ----------

		#// settings - varia

		if (ignoreVowelsMismatchesExceptFirst == True) :
			ignoreVowelsMismatches = False


		line1 = ""
		line2 = ""

		nrFeatures = 0

		indexesMatchingSequence = []
		indexesMatchingSequenceOriginal = []

		indexesMorphemicBoundaries = []
		indexesMorphemicBoundariesOriginal = []

		nrOfTrials = nrTrialsWithoutMorphemicBoundaries

		#// autodetect morphemic boundaries

		if (autodetectMorphologicalBoundaries == True) :

			if ((word1[0:-1].find("￤") > -1)
					or (word2[0:-1].find("￤") > -1)) :
				selectSimilarityScore = 0
				nrOfTrials = nrTrialsWithMorphemicBoundaries
			else :
				selectSimilarityScore = 1



		#// prSimilarity Score used

		if (printResults == True) :
			print("Similarity Score used: " )
			if (optionFunction == 3) :
				print("Basic Global Similarity Score used")
			elif (optionFunction == 4) :
				print("Corrected Global Similarity Score used")
			elif (selectSimilarityScore == 0) :
				print(str(selectSimilarityScore) + " - morphemic boundary detected -> Basic Global Similarity Score used")
			elif (selectSimilarityScore == 1) :
				print(str(selectSimilarityScore) + " - no morphemic boundary detected -> Corrected Global Similarity Score used")



		#// Alignment - Variables 1

		newItem = True

		nextCharacter = 0
		nextCharacter_Tail = 0

		lengthWord1 = len(word1)
		lengthWord2 = len(word2)

		sequenceCount = 0

		index = 0
		previousIndex = -1

		sequenceCount_Tail = 0

		index_Tail = 0

		results = []

		#// store number of feautres used

		fileFeatures = ""
		linesFeaturesProvisional = []
		itemsFeaturesProvisional = []

		fileFeatures = Reader.readFile(locationFileFeatures)

		linesFeaturesProvisional = fileFeatures.split("\n")

		for i in range(0, len(linesFeaturesProvisional)):

			if (linesFeaturesProvisional[i].find("%") < 0) :

				itemsFeaturesProvisional = linesFeaturesProvisional[i].split("	")

				nrFeatures = len(itemsFeaturesProvisional) - 1 #// nr of feature - slot for the character

				break


		#// retrieve consonants-semiconsonant-vowels

		fileCategoriesPhones = ""
		fileCategoriesPhonesLines = []
		fileCategoriesPhonesItems = []
		classCategoriesPhonesCharacter = []
		classCategoriesPhonesValue = []

		fileCategoriesPhones = Reader.readFile(locationFileCategoriesPhones)

		fileCategoriesPhonesLines = fileCategoriesPhones.split("\n")

		for i in range(0, len(fileCategoriesPhonesLines)):

			if (fileCategoriesPhonesLines[i].find("%") < 0) :

				fileCategoriesPhonesItems = fileCategoriesPhonesLines[i].split("	")
				classCategoriesPhonesCharacter.append(copy.deepcopy(fileCategoriesPhonesItems[0]))
				classCategoriesPhonesValue.append(copy.deepcopy(fileCategoriesPhonesItems[1]))


		#// count morphem boundaries

		highestNrMorphemicBoundaries = 0

		listNrsMorphemicBoundaries = countMorphemicBoundaries(0, lengthWord1, lengthWord2, word1, word2)

		#// Variables 2

		bestPairs = [0] * nrOfTrials

		sumFeaturesInCommon = 0.0
		globalSimilaryScore = 0.0
		correctedGlobalSimilaryScore = 0.0

		for n in range(0, len(bestPairs)):
			bestPairs[n] = 0



		similarityScoreMatches = []
		similarityScoreMatchesOriginal = []

		sequence = []
		sequence_Tail = []


		listWord1Pre = []
		listWord2Pre = []

		listWord1Post = []
		listWord2Post = []

		matchWord1 = []
		matchWord2 = []
		matchWord1Original = []
		matchWord2Original = []

		#// Check words' length
		#// -- if 1-letter long

		if (lengthWord1 == 1 or lengthWord2 == 1) :

			if (lengthWord1 == 1) :

				for i in range(0, lengthWord2) :

					matchWord1Provisional1 = []
					matchWord2Provisional1 = []

					for n in range(0, lengthWord2) :
						matchWord2Provisional1.append(copy.deepcopy(n))
						matchWord1Provisional1.append(copy.deepcopy(-1))


					matchWord1Provisional1[i] = 0

					matchWord1.append(copy.deepcopy(matchWord1Provisional1))
					matchWord2.append(copy.deepcopy(matchWord2Provisional1))


			else:

				for i in range(0, lengthWord1) :

					matchWord1Provisional1 = []
					matchWord2Provisional1 = []

					for n in range(0, lengthWord1) :
						matchWord1Provisional1.append(copy.deepcopy(n))
						matchWord2Provisional1.append(copy.deepcopy(-1))


					matchWord2Provisional1[i] = 0

					matchWord2.append(copy.deepcopy(matchWord2Provisional1))
					matchWord1.append(copy.deepcopy(matchWord1Provisional1))




		else: #// if more than 1 letter long

			#// search for max values
			for i in range(0, lengthWord1) :
				for n in range(0, lengthWord2) :

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







			#// store max values
			try:
				for x in range(0, len(bestPairs)):
					for i in range(0, lengthWord1):
						for n in range(0, lengthWord2):

							#//
							if (x == 1 and len(sequence) > nrOfTrials + 1) :#// the +1 is to compensate the addition of a
																			#// morphological boundary at the end

								for f in range(1, len(bestPairs)):
									bestPairs[f] = 0


								raise StopIteration


							if (matrixResultComparison[i][n] == bestPairs[x]) :

								sequenceData = [sequenceCount, i, n, matrixResultComparison[i][n], index, previousIndex, 0 ]
								sequence.append(copy.deepcopy(sequenceData))
								sequence_Tail.append(copy.deepcopy(sequenceData))
								sequenceCount += 1
								sequenceCount_Tail += 1
								index += 1
								index_Tail += 1








			except StopIteration:
				xyz = ""

			##ThreadBeforeMax -> return sequence
			##ThreadAfterMax -> return sequence_Tail

			pool = ThreadPool(processes=2)

			async_sequence = pool.apply_async(ThreadBeforeMax, (bestPairs, sequence, matrixResultComparison, sequenceCount, index))
			async_sequence_Tail = pool.apply_async(ThreadAfterMax, (lengthWord1, lengthWord2, bestPairs, sequence_Tail, matrixResultComparison, sequenceCount_Tail, index_Tail))

			# do some other stuff in the main process

			sequence = async_sequence.get()  # get the return value from your function.
			sequence_Tail = async_sequence_Tail.get()
			#-----

			#ExecutorService pool = Executors.newFixedThreadPool(2);
			#// Wait until One finishes it's task.
			#pool.submit(new ThreadBeforeMax (bestPairs, sequence, matrixResultComparison, sequenceCount, index)).get();
			#// Wait until Two finishes it's task.
			#pool.submit(new ThreadAfterMax (lengthWord1, lengthWord2, bestPairs, sequence_Tail, matrixResultComparison, sequenceCount_Tail, index_Tail)).get();

			#pool.shutdown();

			#----


			#// ==========
			#// Build alignments

			#// ---------
			#// Build initial sequence


			initialSeqs = []
			tailSeqs = []


			pool1 = ThreadPool(processes=2)

			async_initialSeqs = pool1.apply_async(ThreadInitialSeq, (initialSeqs, sequence, line1, word1, line2, word2, nextCharacter))

			line1 = ""
			line2 = ""

			async_tailSeqs = pool1.apply_async(ThreadTailSeq, (lengthWord1, lengthWord2, tailSeqs, sequence_Tail, line1, word1, line2, word2, nextCharacter_Tail))

			initialSeqs = async_initialSeqs.get()  # get the return value from your function.
			tailSeqs = async_tailSeqs.get()

			#-------

			#ExecutorService pool1 = Executors.newFixedThreadPool(2);
			  #// Wait until One finishes it's task.
			#  pool1.submit(new ThreadInitialSeq (initialSeqs, sequence, line1, word1, line2, word2, nextCharacter)).get();

			#  line1 = "";
			#  line2 = "";

			  #// Wait until Two finishes it's task.
			#  pool1.submit(new ThreadTailSeq (lengthWord1, lengthWord2, tailSeqs, sequence_Tail, line1, word1, line2, word2, nextCharacter_Tail)).get();

			  #pool1.shutdown();


			 #//-----

			#//======


			listWord1Pre += copy.deepcopy(initialSeqs[0])
			listWord2Pre += copy.deepcopy(initialSeqs[1])

			listWord1Post += copy.deepcopy(tailSeqs[0])
			listWord2Post += copy.deepcopy(tailSeqs[1])


			line1 = ""
			line2 = ""





			#// join initial and final sequences



			#//this part is conceived if one wants to split the joining of the sequences into batches - this approach may speed up he algorithm, but it is not implemented here
			batches = []

			batches.append(copy.deepcopy(0))

			for w in range(1, 100000):

				if (w*10 > len(listWord1Pre)) :
					batches.append(copy.deepcopy(len(listWord1Pre)))
					break
				else:
					batches.append(copy.deepcopy(w*10))



			listMatchedSeqTemp = []


			#/*
			#[
			# [IN, [A], [B]]*/

			listMatchedSeqTempBatchThreads = []

			listMatchedSeqTempBatch = []

			listMatchedSeqTempCleaned = []







			for i in range(0, len(listWord1Pre)):
				for n in range(0, len(listWord1Post)):

					match1_Pre_Post = []
					match2_Pre_Post = []
					indexes = []
					indexes.append(copy.deepcopy(i))
					indexes.append(copy.deepcopy(n))

					entry = []

					if (listWord1Pre[i][len(listWord1Pre[i]) - 1] == listWord1Post[n][0]
							and listWord2Pre[i][len(listWord2Pre[i]) - 1] == listWord2Post[n][0]) :

						for a in range(0, len(listWord1Pre[i])):
							match1_Pre_Post.append(copy.deepcopy(listWord1Pre[i][a]))
							match2_Pre_Post.append(copy.deepcopy(listWord2Pre[i][a]))


						for a in range(1, len(listWord1Post[n])):
							match1_Pre_Post.append(copy.deepcopy(listWord1Post[n][a]))
							match2_Pre_Post.append(copy.deepcopy(listWord2Post[n][a]))


						for a in range(0, len(match1_Pre_Post)):
							line1 = line1 + ":" + str(match1_Pre_Post[a])
							line2 = line2 + ":" + str(match2_Pre_Post[a])


						line1 = ""
						line2 = ""

						#//entry.append(copy.deepcopy(indexes);
						entry.append(copy.deepcopy(match1_Pre_Post))
						entry.append(copy.deepcopy(match2_Pre_Post))

						listMatchedSeqTemp.append(copy.deepcopy(entry))

						newItem = True
						#/*
						#if (len(matchWord1) < 1) :
						#	matchWord1.append(copy.deepcopy(match1_Pre_Post))
						#	matchWord2.append(copy.deepcopy(match2_Pre_Post))
						#else:
						#	for m in range(0, len(matchWord1)):
						#		if (matchWord1[m] == (match1_Pre_Post) and matchWord2[m] == (match2_Pre_Post)) :
						#			newItem = False


						#	if (newItem == True) :
						#		matchWord1.append(copy.deepcopy(match1_Pre_Post))
						#		matchWord2.append(copy.deepcopy(match2_Pre_Post))


						#*/




			#//=============

			#//combine batches of sequences all together into a single list

			listMatchedSeqTempBatchThreads.append(copy.deepcopy(listMatchedSeqTemp))

			for i in range(0, len(listMatchedSeqTempBatchThreads)):
				for n in range(0, len(listMatchedSeqTempBatchThreads[i])):

					listMatchedSeqTempBatch.append(copy.deepcopy(listMatchedSeqTempBatchThreads[i][n]))




			#// delete matches

			set = copy.deepcopy(listMatchedSeqTempBatch)
			listMatchedSeqTempBatch = []
			listMatchedSeqTempBatch = set
			#/*
			#matchWord1_Temp = []
			#matchWord2_Temp = []
			#*/

			for i in range(0, len(listMatchedSeqTempBatch)):
				matchWord1.append(copy.deepcopy(listMatchedSeqTempBatch[i][0]))
				matchWord2.append(copy.deepcopy(listMatchedSeqTempBatch[i][1]))



			#/*
			#if (newItem == True) {
			#	matchWord1.append(copy.deepcopy(match1_Pre_Post);
			#	matchWord2.append(copy.deepcopy(match2_Pre_Post);
			#}

			#newItem = False;*/



		#// ====================
		#// calculate similarity of various pairs
		#// distinguish between Global or Corrected Global Similarity Scores



		for i in range(0, len(matchWord1)):

			#// varables - 3

			indexPhonPairsItem = []
			indexPhonPairsValueItem = []

			matchingSequence_Start_End = [-1, -1]

			#// possible pairs -> letter word 1 (= A) - letter word 2 (= B), morphemic
			#// boundary = MB, letter = x, gap = 0

			MB0 = False #// morphemic boundary - 0
			x0_MB0 = False #// match letter-0 before morphemic boundary - 0
			x0A_MB0 = False #// match letter-0 before morphemic boundary - 0
			x0B_MB0 = False #// match letter-0 before morphemic boundary - 0
			x0A_MB0B = False #// match letter-0 before morphemic boundary - 0
			x0B_MB0A = False #// match letter-0 before morphemic boundary - 0
			xx_MB0 = False #// match letter-letter before morphemic boundary - 0

			semiconsonant = 0
			vowel = 0

			typeOfMatch = None
			valuePairFromComparisonMatrix = None
			valuePairFromComparisonMatrixOriginal = 0

			coefNeg = 0 #// the coefNeg is used to identify those alignments that are wrong on the basis
								#// of the morpheme boundaries, i.e. matching a morph. bound. and a letter

			#// ----------
			#// define type of pair

			for n in range(0, len(matchWord1[i]) ):

				typeOfMatch = findTypeOfMatch(i, n, matchWord1, matchWord2, word1, word2)

				if typeOfMatch == ("x0") or typeOfMatch == ("0x") or typeOfMatch == ("0￤") or typeOfMatch == ("￤0"):

					valuePairFromComparisonMatrix = 0
				else:

					valuePairFromComparisonMatrix = matrixResultComparison[matchWord1[i][n]][matchWord2[i][n]]
					valuePairFromComparisonMatrixOriginal = matrixResultComparisonOriginal[matchWord1[i][n]][matchWord2[i][n]]



				#/// ----------
				#// -CASE 1-

				if (typeOfMatch == ("xx")) :

					valuePair_1 = -1
					valuePair_2 = -1

					for f in range(0, len(classCategoriesPhonesValue)):
						if (matchWord1[i][n] > -1) :
							if ((word1[matchWord1[i][n]]) == (classCategoriesPhonesCharacter[f]) and classCategoriesPhonesValue[f] == ("-")) :
								valuePair_1 = 0 #// cons
							elif ((word1[matchWord1[i][n]]) == (classCategoriesPhonesCharacter[f]) and classCategoriesPhonesValue[f] == ("±")) :
								valuePair_1 = 1 #// semicons
							elif ((word1[matchWord1[i][n]]) == (classCategoriesPhonesCharacter[f]) and classCategoriesPhonesValue[f] == ("+")) :
								valuePair_1 = 2 #// vows


							if ((word2[matchWord2[i][n]]) == (classCategoriesPhonesCharacter[f]) and classCategoriesPhonesValue[f] == ("-")) :
								valuePair_2 = 0 #// cons
							elif ((word2[matchWord2[i][n]]) == (classCategoriesPhonesCharacter[f]) and classCategoriesPhonesValue[f] == ("±")) :
								valuePair_2 = 1 #// semicons
							elif ((word2[matchWord2[i][n]]) == (classCategoriesPhonesCharacter[f]) and classCategoriesPhonesValue[f] == ("+")) :
								valuePair_2 = 2 #// vows




					limitSignificanceUsed = -1

					if (limitSignificanceConsonants <= limitSignificanceVowels
							and (valuePair_1 == 0 or valuePair_2 == 0 or valuePair_1 == 1 or valuePair_2 == 1)) : #// if
																												#// one
																												#// of
																												#// the
																												#// two
																												#// is a
																												#// cons
																												#// or a
																												#// semicons

						limitSignificanceUsed = 0 #// -> use limitSignificanceConsonants
					elif (limitSignificanceConsonants <= limitSignificanceVowels and (valuePair_1 == 2 and valuePair_2 == 2)) : #// if both are vows

						limitSignificanceUsed = 1 #// -> use limitSignificanceVowels


					elif (limitSignificanceConsonants > limitSignificanceVowels and (valuePair_1 == 2 or valuePair_2 == 2)) : #// if one of the two is a cons or a semicons

						limitSignificanceUsed = 1 #// -> use limitSignificanceVowels
					elif (limitSignificanceConsonants > limitSignificanceVowels and ((valuePair_1 == 0 or valuePair_1 == 1) and (valuePair_2 == 0 or valuePair_2 == 1))) : #// if
																													#// both
																													#// are
																													#// cons

						limitSignificanceUsed = 0 #// -> use limitSignificanceConsonants


					if (limitSignificanceUsed == 0) :
						if (limitMinimumFeaturesConsonants == True
								and valuePairFromComparisonMatrixOriginal <= limitSignificanceConsonants) : #// if the
																											#// feature
																											#// index of
																											#// the match
																											#// is below
																											#// the
																											#// feature
																											#// limit,
																											#// its value
																											#// is
																											#// reduced
																											#// to 0 and
																											#// not
																											#// counted
							matchWord1[i][n] = matchWord1[i][n] - 2000
							matchWord2[i][n] = matchWord2[i][n] - 2000
							valuePairFromComparisonMatrix = 0

					elif (limitSignificanceUsed == 1) :
						if (limitMinimumFeaturesVowels == True and valuePairFromComparisonMatrixOriginal <= limitSignificanceVowels) : #// if the feature
																										#// index of the
																										#// match is
																										#// below the
																										#// feature
																										#// limit, its
																										#// value is
																										#// reduced to 0
																										#// and not
																										#// counted
							matchWord1[i][n] =  matchWord1[i][n] - 2000
							matchWord2[i][n] =  matchWord2[i][n] - 2000
							valuePairFromComparisonMatrix = 0



					#// match only same class of phonemes

					if (matchesOnlyPhonesSameCategory == True) :
						if ((valuePair_1 == 2 or valuePair_2 == 2) and (valuePair_1 != valuePair_2) and ( not (i == 0 or n == 0 or n == len(matchWord1[i]) - 2 or i == len(matchWord1) - 2))) :
							coefNeg = 1000

						if ((valuePair_1 == 2 or valuePair_2 == 2) and (valuePair_1 != valuePair_2) and (i == 0 or n == 0) and not (n == len(matchWord1[i]) - 2) or (i == len(matchWord1) - 2)) :

							matrixResultComparisonOriginal[matchWord1[i][n]][matchWord2[i][n]] = 0
							matrixResultComparison[matchWord1[i][n]][matchWord2[i][n]] = 0



					if ((valuePair_1 == 2 and valuePair_2 == 2) or ((valuePair_1 < 2 and valuePair_2 < 2))) :#// or
																											#// valuePair_1
																											#// == 1) and
																											#// (valuePair_2
																											#// == 0 or
																											#// valuePair_2
																											#// == 1))){
						if (matchWord1[i][n] > -1) :

							alreadyListed = False
							lettersOfThePair = ""

							word1DividedSegments = ""
							word2DividedSegments = ""

							for h in range(0, len(word1)):
								if not (word1[h] == ("￤")):
									word1DividedSegments = word1DividedSegments + ":" + (word1[h])



							for h in range(0, len(word2)):
								if not (word2[h] == ("￤")):
									word2DividedSegments = word2DividedSegments + ":" + (word2[h])




							segmentsWord1WithDiacritics = buildWord(word1DividedSegments, word1Unparsed, locationFilePhoneticDiacritics)
							segmentsWord2WithDiacritics = buildWord(word2DividedSegments, word2Unparsed, locationFilePhoneticDiacritics)

							segmentsWord1WithDiacritics = segmentsWord1WithDiacritics.replace("￤", "	￤")
							segmentsWord2WithDiacritics = segmentsWord2WithDiacritics.replace("￤", "	￤")

							segmentsWord1 = segmentsWord1WithDiacritics.split("	")
							segmentsWord2 = segmentsWord2WithDiacritics.split("	")

							if (matchWord1[i][n] < -1) :
								lettersOfThePair = segmentsWord1[(matchWord1[i][n]) + 2000] + " - " + segmentsWord2[(matchWord2[i][n]) + 2000]
							else:
								lettersOfThePair = segmentsWord1[(matchWord1[i][n])] + " - " + segmentsWord2[(matchWord2[i][n])]

							for f in range(0, len(indexPhonPairsItem)):

								if (lettersOfThePair == (indexPhonPairsItem[f])) :
									alreadyListed = True
									indexPhonPairsValueItem[f] = indexPhonPairsValueItem[f] + 1



							if (alreadyListed == False) :

								indexPhonPairsItem.append(copy.deepcopy(lettersOfThePair))
								indexPhonPairsValueItem.append(copy.deepcopy(1))



						if (valuePairFromComparisonMatrix > 0) :
							if (matchingSequence_Start_End[0] < 0) :
								matchingSequence_Start_End[0] = n

							matchingSequence_Start_End[1] = n


						if (MB0 == False) :

							sumFeaturesInCommon = calculateFeaturesInCommon(1, sumFeaturesInCommon, valuePairFromComparisonMatrix)
							xx_MB0 = True

						elif (MB0 == True and (xx_MB0 == False or x0_MB0 == False)) :

							sumFeaturesInCommon = calculateFeaturesInCommon(1, sumFeaturesInCommon, valuePairFromComparisonMatrix)
							xx_MB0 = True

							if (x0A_MB0B == True or x0B_MB0A == True) :

								coefNeg = 1000


						elif (MB0 == True and (xx_MB0 == True or x0_MB0 == True)) :

							sumFeaturesInCommon = calculateFeaturesInCommon(1, sumFeaturesInCommon, valuePairFromComparisonMatrix)




					#// -CASE 2-

				elif (typeOfMatch == ("x0") or typeOfMatch == ("0x")) :

					if (ignoreSemiconsonantMismatches == True) :
						if (typeOfMatch == ("x0")) :
							for f in range(0, len(classCategoriesPhonesValue)):
								if (matchWord1[i][n] > -1) :
									if ((word1[matchWord1[i][n]]) == (classCategoriesPhonesCharacter[f]) and classCategoriesPhonesValue[f] == ("±")) :
										matchWord1[i][n] =  matchWord1[i][n] - 1000
										valuePairFromComparisonMatrix = 0
										semiconsonant = semiconsonant + 1




						if (typeOfMatch == ("0x")) :
							for f in range(0, len(classCategoriesPhonesValue)):
								if (matchWord2[i][n] > -1) :
									if ((word2[matchWord2[i][n]])
											 == (classCategoriesPhonesCharacter[f])
											and classCategoriesPhonesValue[f] == ("±")) :
										matchWord2[i][n] =  matchWord2[i][n] - 1000
										valuePairFromComparisonMatrix = 0
										semiconsonant = semiconsonant + 1






					if ((ignoreVowelsMismatches == True or (ignoreVowelsMismatchesExceptFirst == True and n > 0))
							and matchWord1[i][n] > -2 and matchWord2[i][n] > -2) :
						if (typeOfMatch == ("x0")) :
							for f in range(0, len(classCategoriesPhonesValue)):
								if (matchWord1[i][n] > -1) :
									if ((word1[matchWord1[i][n]])
											 == (classCategoriesPhonesCharacter[f])
											and classCategoriesPhonesValue[f] == ("+")) :
										matchWord1[i][n] =  matchWord1[i][n] - 1000
										valuePairFromComparisonMatrix = 0
										vowel = vowel + 1




						if (typeOfMatch == ("0x")) :
							for f in range(0, len(classCategoriesPhonesValue)):
								if (matchWord2[i][n] > -1) :
									if ((word2[matchWord2[i][n]])
											 == (classCategoriesPhonesCharacter[f])
											and classCategoriesPhonesValue[f] == ("+")) :
										matchWord2[i][n] =  matchWord2[i][n] - 1000
										valuePairFromComparisonMatrix = 0
										vowel = vowel + 1






					if (MB0 == False) :

						sumFeaturesInCommon = calculateFeaturesInCommon(0, sumFeaturesInCommon, valuePairFromComparisonMatrix)
						x0_MB0 = True
						if (typeOfMatch == ("x0")) :
							x0A_MB0 = True


						if (typeOfMatch == ("0x")) :
							x0B_MB0 = True


					elif (MB0 == True and (xx_MB0 == False or x0_MB0 == False)) :

						sumFeaturesInCommon = calculateFeaturesInCommon(0, sumFeaturesInCommon, valuePairFromComparisonMatrix)
						x0_MB0 = True

						if (typeOfMatch == ("x0")) :
							x0A_MB0 = True


						if (typeOfMatch == ("0x")) :
							x0B_MB0 = True


					elif (MB0 == True and (xx_MB0 == True or x0_MB0 == True)) :

						sumFeaturesInCommon = calculateFeaturesInCommon(1, sumFeaturesInCommon, valuePairFromComparisonMatrix)



					#// -CASE 3-

				elif (typeOfMatch == ("x￤") or typeOfMatch == ("￤x")) :

					sumFeaturesInCommon = calculateFeaturesInCommon(2, sumFeaturesInCommon, valuePairFromComparisonMatrix)
					coefNeg = 1000
					MB0 = True

					#// -CASE 4-

				elif (typeOfMatch == ("￤0") or typeOfMatch == ("0￤")) :

					sumFeaturesInCommon = calculateFeaturesInCommon(0, sumFeaturesInCommon, valuePairFromComparisonMatrix)
					if (xx_MB0 == True and typeOfMatch == ("0￤")) :
						coefNeg = 1000

					if (xx_MB0 == True and typeOfMatch == ("￤0")) :
						coefNeg = 1000

					if (x0A_MB0 == True and typeOfMatch == ("0￤")) :
						x0A_MB0B = True

					if (x0B_MB0 == True and typeOfMatch == ("￤0")) :
						x0B_MB0A = True

					MB0 = True

					#// -CASE 5-

				elif (typeOfMatch == ("￤￤")) :

					sumFeaturesInCommon = calculateFeaturesInCommon(0, sumFeaturesInCommon, valuePairFromComparisonMatrix)

					MB0 = False
					x0_MB0 = False
					xx_MB0 = False
					x0A_MB0 = False
					x0B_MB0 = False
					x0A_MB0B = False
					x0B_MB0A = False



			#// Calculate length of the match

			indexesMatchingSequence.append(copy.deepcopy(matchingSequence_Start_End))

			indexesMorphemicBoundaries.append(copy.deepcopy(matchingSequence_Start_End))

			lengthMatchingSequence = 0

			nrMorphemicBoundariesWord1 = 0
			nrMorphemicBoundariesWord2 = 0

			for m in range(indexesMatchingSequence[i][0], indexesMatchingSequence[i][1] + 1):

				if (m < 0) :
					m = 0
				#// to deal with cases in which there is no match

				if (matchWord1[i][m] > -1) :
					if ((word1[matchWord1[i][m]]) == ("￤")) :
						nrMorphemicBoundariesWord1 = nrMorphemicBoundariesWord1 + 1



				if (matchWord2[i][m] > -1) :
					if ((word2[matchWord2[i][m]]) == ("￤")) :
						nrMorphemicBoundariesWord2 = nrMorphemicBoundariesWord2 + 1





			if (nrMorphemicBoundariesWord1 >= nrMorphemicBoundariesWord2) :
				highestNrMorphemicBoundaries = nrMorphemicBoundariesWord1
			else:
				highestNrMorphemicBoundaries = nrMorphemicBoundariesWord2


			#// ----count vowels in the Corrected Global matching
			#// string-------------------------------------

			nrVowelsMatchingSequenceWord1 = 0
			nrVowelsMatchingSequenceWord2 = 0
			nrVowelsMatchingSequence = 0

			for m in range(indexesMatchingSequence[i][0], indexesMatchingSequence[i][1] + 1):

				if (m < 0) :
					m = 0
				 #// to deal with cases in which there is no match

				if (matchWord1[i][m] < -100 and matchWord1[i][m] > -1500) :
					for f in range(0, len(classCategoriesPhonesValue)):
						if ((word1.charAt(matchWord1[i][m] + 1000)) == (classCategoriesPhonesCharacter[f]) and classCategoriesPhonesValue[f] == ("+")) :

							nrVowelsMatchingSequenceWord1 = nrVowelsMatchingSequenceWord1 + 1





				if (matchWord2[i][m] < -100 and matchWord2[i][m] > -1500) :
					for f in range(0, len(classCategoriesPhonesValue)):
						if ((word2.charAt(matchWord2[i][m] + 1000)) == (classCategoriesPhonesCharacter[f]) and classCategoriesPhonesValue[f] == ("+")) :

							nrVowelsMatchingSequenceWord2 = nrVowelsMatchingSequenceWord2 + 1






			if (nrVowelsMatchingSequenceWord1 >= nrVowelsMatchingSequenceWord2) :
				nrVowelsMatchingSequence = nrVowelsMatchingSequenceWord1
			else:
				nrVowelsMatchingSequence = nrVowelsMatchingSequenceWord2

			#// -------------------------
			#// ----count semivowels in the Corrected Global matching
			#// string-------------------------------------

			nrSemiconsonantsMatchingSequenceWord1 = 0;
			nrSemiconsonantsMatchingSequenceWord2 = 0;
			nrSemiconsonantsMatchingSequence = 0;

			for m in range(indexesMatchingSequence[i][0], indexesMatchingSequence[i][1]):

				if (m < 0) :
					m = 0
				#// to deal with cases in which there is no match

				if (matchWord1[i][m] < -100 and matchWord1[i][m] > -1500) :

					for j in range(0, len(classCategoriesPhonesCharacter)) :
						if ((word1.charAt(matchWord1[i][m] + 1000)) == (classCategoriesPhonesCharacter[j]) and classCategoriesPhonesValue[j] == ("±")) : #// if
																														#// the
																														#// feature
																														#// index
																														#// of
																														#// the
																														#// match
																														#// is
																														#// below
																														#// the
																														#// feature
																														#// limit,
																														#// its
																														#// value
																														#// is
																														#// reduced
																														#// to
																														#// 0
																														#// and
																														#// not
																														#// counted

							nrSemiconsonantsMatchingSequenceWord1 = nrSemiconsonantsMatchingSequenceWord1 + 1




				if (matchWord2[i][m] < -100 and matchWord2[i][m] > -1500) :

					for j in range(0, len(classCategoriesPhonesCharacter)):
						if ((word2.charAt(matchWord2[i][m] + 1000)) == (classCategoriesPhonesCharacter[j]) and classCategoriesPhonesValue[j] == ("±")) : #// if
																														#// the
																														#// feature
																														#// index
																														#// of
																														#// the
																														#// match
																														#// is
																														#// below
																														#// the
																														#// feature
																														#// limit,
																														#// its
																														#// value
																														#// is
																														#// reduced
																														#// to
																														#// 0
																														#// and
																														#// not
																														#// counted
							nrSemiconsonantsMatchingSequenceWord2 = nrSemiconsonantsMatchingSequenceWord2 + 1






			if (nrSemiconsonantsMatchingSequenceWord1 >= nrSemiconsonantsMatchingSequenceWord2) :
				nrSemiconsonantsMatchingSequence = nrSemiconsonantsMatchingSequenceWord1
			else:
				nrSemiconsonantsMatchingSequence = nrSemiconsonantsMatchingSequenceWord2

			#// -------------------------

			lengthMatchingSequence = indexesMatchingSequence[i][1] + 1 - indexesMatchingSequence[i][0] - highestNrMorphemicBoundaries - nrSemiconsonantsMatchingSequence - nrVowelsMatchingSequence

			listNrsMorphemicBoundaries = countMorphemicBoundaries(0, lengthWord1, lengthWord2, word1, word2)

			highestNrMorphemicBoundaries = listNrsMorphemicBoundaries[0]

			lengthWord1MinusMorphemicBoundaries = lengthWord1 - listNrsMorphemicBoundaries[1]
			lengthWord2MinusMorphemicBoundaries = lengthWord2 - listNrsMorphemicBoundaries[2]

			#//find longest and shortest word
			longestWord = 0.0
			shortestWord = 0.0

			if (lengthWord1MinusMorphemicBoundaries >= lengthWord2MinusMorphemicBoundaries) :
				longestWord = lengthWord1MinusMorphemicBoundaries
				shortestWord = lengthWord2MinusMorphemicBoundaries
			else:
				longestWord = lengthWord2MinusMorphemicBoundaries
				shortestWord = lengthWord1MinusMorphemicBoundaries


			#//find length of the whole match
			lenghtAlignmentMinusMorphemicBoundaries = 0.0
			lenghtAlignmentMinusMorphemicBoundaries = len(matchWord1[i])-highestNrMorphemicBoundaries

			#//cast nrFeatures into double
			nrFeaturesDouble = nrFeatures

			#// calculate global similarity score according to default function

			SumFeat = float(sumFeaturesInCommon)
			NrFeat = float(nrFeaturesDouble)
			LongestWord = float(longestWord)
			ShortestWord = float(shortestWord)
			LenSeq = float(lengthMatchingSequence)
			LenWord1 = float(lengthWord1MinusMorphemicBoundaries)
			LenWord2 = float(lengthWord2MinusMorphemicBoundaries)
			LenAlign = float(lenghtAlignmentMinusMorphemicBoundaries)


			defaultFunctionGlobal = "((SumFeat) / (NrFeat * 7.71))"

			globalSimilaryScore = numexpr.evaluate(defaultFunctionGlobal)

			#Expression gf = new ExpressionBuilder(defaultFunctionGlobal)
			#		.variables("SumFeat", "NrFeat", "LongestWord", "ShortestWord", "LenSeq", "LenWord1", "LenWord2", "LenAlign").build()
			#		.setVariable("SumFeat", sumFeaturesInCommon).setVariable("NrFeat", nrFeaturesDouble)
			#		.setVariable("LongestWord", longestWord)
			#		.setVariable("ShortestWord", shortestWord)
			#		.setVariable("LenSeq", (double) lengthMatchingSequence)
			#		.setVariable("LenWord1", lengthWord1MinusMorphemicBoundaries)
			#		.setVariable("LenWord2", lengthWord2MinusMorphemicBoundaries)
			#		.setVariable("LenAlign",lenghtAlignmentMinusMorphemicBoundaries);
			#globalSimilaryScore = gf.evaluate();

			#// calculate corrected global similarity score:

			if (optionFunction == 0 or optionFunction == 3 or optionFunction == 4) :

				#// according to default function

				defaultFunctionCorrectedGlobal = "((SumFeat) / (NrFeat * 7.71)) - ((LenSeq - ShortestWord)/1.04 + ((LenAlign - LenSeq)/LenSeq)) * (1-(ShortestWord/LongestWord))";


				correctedGlobalSimilaryScore = numexpr.evaluate(defaultFunctionCorrectedGlobal)


				#Expression e = new ExpressionBuilder(defaultFunctionCorrectedGlobal)
				#		.variables("SumFeat", "NrFeat", "LongestWord", "ShortestWord", "LenSeq", "LenWord1", "LenWord2", "LenAlign").build()
				#		.setVariable("SumFeat", sumFeaturesInCommon).setVariable("NrFeat", nrFeaturesDouble)
				#		.setVariable("LongestWord", longestWord)
				#		.setVariable("ShortestWord", shortestWord)
				#		.setVariable("LenSeq", (double) lengthMatchingSequence)
				#		.setVariable("LenWord1", lengthWord1MinusMorphemicBoundaries)
				#		.setVariable("LenWord2", lengthWord2MinusMorphemicBoundaries)
				#		.setVariable("LenAlign",lenghtAlignmentMinusMorphemicBoundaries);
				#correctedGlobalSimilaryScore = e.evaluate();


			elif optionFunction == 1:

				#// read external function - as config file

				fileExternalFunction = Path(os.path.join(os.path.dirname(__file__), "config/external_corr_glob_sim_score_function.txt"))

				fileExternalFunctionRead = Reader.readFile(fileExternalFunction)

				linesExternalFunction = fileExternalFunctionRead.split("\n")

				for a in range(0, len(linesExternalFunction)):

					if (linesExternalFunction[a].find("%") < 0) :


						correctedGlobalSimilaryScore = numexpr.evaluate(linesExternalFunction[a])



						#Expression e = new ExpressionBuilder(linesExternalFunction[a])
						#		.variables("SumFeat", "NrFeat", "LongestWord", "ShortestWord", "LenSeq", "LenWord1", "LenWord2", "LenAlign").build()
						#		.setVariable("SumFeat", sumFeaturesInCommon).setVariable("NrFeat", nrFeaturesDouble)
						#		.setVariable("LongestWord", longestWord)
						#		.setVariable("ShortestWord", shortestWord)
						#		.setVariable("LenSeq", (double) lengthMatchingSequence)
						#		.setVariable("LenWord1", lengthWord1MinusMorphemicBoundaries)
						#		.setVariable("LenWord2", lengthWord2MinusMorphemicBoundaries)
						#		.setVariable("LenAlign",lenghtAlignmentMinusMorphemicBoundaries);
						#correctedGlobalSimilaryScore = e.evaluate();




			elif (optionFunction == 2) :

					#// external function - as argument

				correctedGlobalSimilaryScore = numexpr.evaluate(externalFunction)

					#Expression e = new ExpressionBuilder(externalFunction)
					#		.variables("SumFeat", "NrFeat", "LongestWord", "ShortestWord", "LenSeq", "LenWord1", "LenWord2", "LenAlign").build()
					#		.setVariable("SumFeat", sumFeaturesInCommon).setVariable("NrFeat", nrFeaturesDouble)
					#		.setVariable("LongestWord", longestWord)
					#		.setVariable("ShortestWord", shortestWord)
					#		.setVariable("LenSeq", (double) lengthMatchingSequence)
					#		.setVariable("LenWord1", lengthWord1MinusMorphemicBoundaries)
					#		.setVariable("LenWord2", lengthWord2MinusMorphemicBoundaries)
					#		.setVariable("LenAlign",lenghtAlignmentMinusMorphemicBoundaries);
					#correctedGlobalSimilaryScore = e.evaluate();



			#// Mark wrong alignments
			if (globalSimilaryScore < 0) :

				globalSimilaryScore = 0
				correctedGlobalSimilaryScore = 0 - correctedGlobalSimilaryScore



			globalSimilaryScore = globalSimilaryScore - coefNeg
			correctedGlobalSimilaryScore = correctedGlobalSimilaryScore - coefNeg

			#// build results without diacritics

			similarityScores = []

			similarityScores.append(copy.deepcopy(globalSimilaryScore))
			similarityScores.append(copy.deepcopy(correctedGlobalSimilaryScore))

			similarityScoreMatches.append(copy.deepcopy(similarityScores))

			sumFeaturesInCommon = 0.0

			line1 = ""
			line2 = ""

			indexPhoneticPairs.append(copy.deepcopy(indexPhonPairsItem))
			indexPhoneticPairsValue.append(copy.deepcopy(indexPhonPairsValueItem))


		#// =================
		#// organize alignments by most similar to less similar

		similarityScoreMatchesOriginal.append(copy.deepcopy(similarityScoreMatches[0]))
		matchWord1Original.append(copy.deepcopy(matchWord1[0]))
		matchWord2Original.append(copy.deepcopy(matchWord2[0]))
		indexesMatchingSequenceOriginal.append(copy.deepcopy(indexesMatchingSequence[0]))
		indexesMorphemicBoundariesOriginal.append(copy.deepcopy(indexesMorphemicBoundaries[0]))
		attestedPhoneticPairs.append(copy.deepcopy(indexPhoneticPairs[0]))
		nrAttestationsPhoneticPairs.append(copy.deepcopy(indexPhoneticPairsValue[0]))

		for i in range(1, len(similarityScoreMatches)):
			for n in range(0, len(similarityScoreMatchesOriginal)):



				if (similarityScoreMatches[i][selectSimilarityScore] < similarityScoreMatchesOriginal[-1][selectSimilarityScore]) :
					similarityScoreMatchesOriginal.append(copy.deepcopy(similarityScoreMatches[i]))
					matchWord1Original.append(copy.deepcopy(matchWord1[i]))
					matchWord2Original.append(copy.deepcopy(matchWord2[i]))
					attestedPhoneticPairs.append(copy.deepcopy(indexPhoneticPairs[i]))
					nrAttestationsPhoneticPairs.append(copy.deepcopy(indexPhoneticPairsValue[i]))
					indexesMatchingSequenceOriginal.append(copy.deepcopy(indexesMatchingSequence[i]))
					indexesMorphemicBoundariesOriginal.append(copy.deepcopy(indexesMorphemicBoundaries[i]))
					break
				elif (similarityScoreMatches[i][selectSimilarityScore] == (similarityScoreMatchesOriginal[n][selectSimilarityScore])) :

					sameGlobal = False #this bit is different from the Java version, because insert seems to work differently from .add() ?
					sameModified = False

					if similarityScoreMatches[i][0] == similarityScoreMatchesOriginal[n][0]:
						sameGlobal =True
					if similarityScoreMatches[i][1] == similarityScoreMatchesOriginal[n][1]:
						sameModified = True
					if sameGlobal == True and sameModified == True:
						break
					else:
						if (selectSimilarityScore == 0) :
							a = 0

							if (similarityScoreMatchesOriginal[n][1] < similarityScoreMatches[i][1]) :
								a = n
							else:
								a = n + 1


							similarityScoreMatchesOriginal.insert(a, copy.deepcopy(similarityScoreMatches[i]))
							matchWord1Original.insert(a, copy.deepcopy(matchWord1[i]))
							matchWord2Original.insert(a, copy.deepcopy(matchWord2[i]))
							attestedPhoneticPairs.insert(a, copy.deepcopy(indexPhoneticPairs[i]))
							nrAttestationsPhoneticPairs.insert(a, copy.deepcopy(indexPhoneticPairsValue[i]))
							indexesMatchingSequenceOriginal.insert(a, copy.deepcopy(indexesMatchingSequence[i]))
							indexesMorphemicBoundariesOriginal.insert(a, copy.deepcopy(indexesMorphemicBoundaries[i]))
							break

						else:

							similarityScoreMatchesOriginal.insert(n, copy.deepcopy(similarityScoreMatches[i]))
							matchWord1Original.insert(n, copy.deepcopy(matchWord1[i]))
							matchWord2Original.insert(n, copy.deepcopy(matchWord2[i]))
							attestedPhoneticPairs.insert(n, copy.deepcopy(indexPhoneticPairs[i]))
							nrAttestationsPhoneticPairs.insert(n, copy.deepcopy(indexPhoneticPairsValue[i]))
							indexesMatchingSequenceOriginal.insert(n, copy.deepcopy(indexesMatchingSequence[i]))
							indexesMorphemicBoundariesOriginal.insert(n, copy.deepcopy(indexesMorphemicBoundaries[i]))
							break

				elif (similarityScoreMatches[i][selectSimilarityScore] > similarityScoreMatchesOriginal[n][selectSimilarityScore]) :

					similarityScoreMatchesOriginal.insert(n, copy.deepcopy(similarityScoreMatches[i]))
					matchWord1Original.insert(n, copy.deepcopy(matchWord1[i]))
					matchWord2Original.insert(n, copy.deepcopy(matchWord2[i]))
					attestedPhoneticPairs.insert(n, copy.deepcopy(indexPhoneticPairs[i]))
					nrAttestationsPhoneticPairs.insert(n, copy.deepcopy(indexPhoneticPairsValue[i]))
					indexesMatchingSequenceOriginal.insert(n, copy.deepcopy(indexesMatchingSequence[i]))
					indexesMorphemicBoundariesOriginal.insert(n, copy.deepcopy(indexesMorphemicBoundaries[i]))
					break





		#// build and prresults in the console

		for i in range(0, len(similarityScoreMatchesOriginal)):

			if (i == 0 or (similarityScoreMatchesOriginal[i][0] > 0)) :

				for n in range(0, len(matchWord1Original[i])) :

					if (displayAutomaticallyRecognizedMorphologicalBoundaries == True) :
						if (n == indexesMorphemicBoundariesOriginal[i][0]) :
							line1 = line1 + "┊"
							line2 = line2 + "┊"




					if (matchWord1Original[i][n] == -1) :
						line1 = line1 + ":0"
					elif (matchWord1Original[i][n] < -1 and matchWord1Original[i][n] > -1500) :
						line1 = line1 + ";" + word1.charAt((matchWord1Original[i][n]) + 1000)
					elif (matchWord1Original[i][n] < -1500) :
						line1 = line1 + "·" + word1.charAt((matchWord1Original[i][n]) + 2000)
					else:
						line1 = line1 + ":" + word1[matchWord1Original[i][n]]

					if (matchWord2Original[i][n] == -1) :
						line2 = line2 + ":0"
					elif (matchWord2Original[i][n] < -1 and matchWord2Original[i][n] > -1500) :
						line2 = line2 + ";" + word2.charAt((matchWord2Original[i][n]) + 1000)
					elif (matchWord2Original[i][n] < -1500) :
						line2 = line2 + "·" + word2.charAt((matchWord2Original[i][n]) + 2000)###
					else:
						line2 = line2 + ":" + word2[matchWord2Original[i][n]]


					if (displayAutomaticallyRecognizedMorphologicalBoundaries == True) :
						if (n == indexesMorphemicBoundariesOriginal[i][1]) :
							line1 = line1 + "┊"
							line2 = line2 + "┊"





				#// ============
				#// organize and return results

				#// if there is no alignment

				if (similarityScoreMatchesOriginal[0][0] < 0) :

					line1 = ""
					line2 = ""

					line1 = line1 + word1.charAt(0)

					for a in range(1, lengthWord1):
						line1 = line1 + ":" + word1.charAt(a)

					for a in range(0, (lengthWord2)):
						line1 = line1 + ":" + "0"


					line2 = "0"
					for a in range(1, (lengthWord1)):
						line2 = line2 + ":" + "0"

					for a in range(0, (lengthWord2)):
						line2 = line2 + ":" + word2.charAt(a)


					similarityScoreMatchesOriginal[i][0] = 0.0
					similarityScoreMatchesOriginal[i][1] = 0.0

					indexPhonPairsItem = []
					indexPhonPairsValueItem = []

					indexPhonPairsItem.append(copy.deepcopy("0 - 0"))
					indexPhonPairsValueItem.append(copy.deepcopy(0))

					attestedPhoneticPairs[i] = indexPhonPairsItem
					nrAttestationsPhoneticPairs[i] = indexPhonPairsValueItem


				if (printResults == True) :
					print("========")


				#// build alignments with diacritics

				word1WithDiacritics = ""
				word2WithDiacritics = ""

				if not (word1Unparsed[-1] == ("￤")) :
					word1Unparsed = word1Unparsed + "￤"


				if not (word2Unparsed[-1] == ("￤")) :
					word2Unparsed = word2Unparsed + "￤"


				word1WithDiacritics = buildWord(line1, word1Unparsed, locationFilePhoneticDiacritics)
				word2WithDiacritics = buildWord(line2, word2Unparsed, locationFilePhoneticDiacritics)

				#//

				firstWord1 = 0
				firstWord2 = 0

				#// vows = 2
				#// vows = 0

				foundWord1 = False
				foundWord2 = False

				for f in range(0, len(classCategoriesPhonesValue)):

					if (line1[1:2] == (classCategoriesPhonesCharacter[f])) :
						firstWord1 = (classCategoriesPhonesValue[f].replace("-", "0").replace("±", "1").replace("\+", "2")) ###
						foundWord1 = True


					if (line2[1:2] == (classCategoriesPhonesCharacter[f])) :
						firstWord2 = (classCategoriesPhonesValue[f].replace("-", "0").replace("±", "1").replace("\+", "2"))
						foundWord2 = True




				if (foundWord1 == False) :
					firstWord1 = -1


				if (foundWord2 == False) :
					firstWord2 = -1



				if ((firstWord1 == 2 and firstWord2 != 2 and firstWord2 > -1)) :

					lettersWord1 = line1.split(":")
					line1 = ":" + lettersWord1[1][0:1] + ":0┊"

					for t in range(2, len(lettersWord1)):
						line1 = line1 + ":" + lettersWord1[t]


					lettersWord1WithDiacritics = word1WithDiacritics.split("	")
					word1WithDiacritics = lettersWord1WithDiacritics[0][0:1] + "	0┊"

					for t in range(1, len(lettersWord1WithDiacritics)):
						word1WithDiacritics = word1WithDiacritics + "	" + lettersWord1WithDiacritics[t]


					line2 = ":0" + line2
					word2WithDiacritics = "0	" + word2WithDiacritics



				if ((firstWord2 == 2 and firstWord1 != 2 and firstWord1 > -1)) :

					lettersWord2 = line2.split(":")
					line2 = ":" + lettersWord2[1][0:1] + ":0┊"

					for t in range(2, len(lettersWord2)):
						line2 = line2 + ":" + lettersWord2[t]


					lettersWord2WithDiacritics = word2WithDiacritics.split("	")
					word2WithDiacritics = lettersWord2WithDiacritics[0][0:1] + "	0┊"

					for t in range(1, len(lettersWord2WithDiacritics)):
						word2WithDiacritics = word2WithDiacritics + "	" + lettersWord2WithDiacritics[t]


					line1 = ":0" + line1
					word1WithDiacritics = "0	" + word1WithDiacritics



				#// --- last

				#// vows = 2
				#// vows = 0

				lastWord1 = 0
				lastWord2 = 0

				foundWord1_1 = False
				foundWord2_1 = False

				for f in range(0, len(classCategoriesPhonesValue)):

					if (line1[len(line1)-3:len(line1)-2] == (classCategoriesPhonesCharacter[f])) :
						lastWord1 = classCategoriesPhonesValue[f].replace("-", "0").replace("±", "1").replace("\+", "2")
						foundWord1_1 = True


					if (line2[len(line2)-3:len(line2)-2] == (classCategoriesPhonesCharacter[f])) :
						lastWord2 = (classCategoriesPhonesValue[f].replace("-", "0").replace("±", "1").replace("\+", "2"))
						foundWord2_1 = True




				if (foundWord1_1 == False) :
					lastWord1 = -1


				if (foundWord2_1 == False) :
					lastWord2 = -1





				#//===

				if ((lastWord1 == 2 and lastWord2 != 2 and lastWord2 > -1)) :

					lettersWord1 = line1.split(":")
					lettersWord1WithDiacritics = word1WithDiacritics.split("	")

					lettersWord2 = line2.split(":")
					lettersWord2WithDiacritics = word2WithDiacritics.split("	")

					line1 = ""
					for t in range(1, len(lettersWord1)):
						line1 = line1 + ":" + lettersWord1[t]


					line1 = line1.replace(":┊:", "┊:")

					line1 = line1 + ":" + lettersWord1[len(lettersWord1) - 2][0:1] + ":0:￤"#// .substring(letters_word.length-1,
																											#// letters_word.length)
																											#// +
																											#// "┊:0:￤";

					word1WithDiacritics = lettersWord1WithDiacritics[0]
					for t in range(1, len(lettersWord1WithDiacritics) - 2):
						word1WithDiacritics = word1WithDiacritics + "	" + lettersWord1WithDiacritics[t]


					word1WithDiacritics = word1WithDiacritics + "	" + lettersWord1WithDiacritics[len(lettersWord1WithDiacritics) - 2][0:1] + "	0	￤"

					line2 = ""

					for t in range(1, len(lettersWord2)-2) :
						line2 = line2 + ":" + lettersWord2[t]

					line2 = line2.replace(":┊:", "┊:")

					line2 = line2 + ":0:" + lettersWord2[len(lettersWord2) - 2]+ ":￤" #//.substring(0, 1) + ":￤";

					#// ----
					word2WithDiacritics = lettersWord2WithDiacritics[0]

					for t in range(1, len(lettersWord2WithDiacritics)):
						word2WithDiacritics = word2WithDiacritics + "	" + lettersWord2WithDiacritics[t]


					word2WithDiacritics = word2WithDiacritics + "	0	" + lettersWord2WithDiacritics[len(lettersWord2WithDiacritics) - 2] + "	￤" #//.substring(0, 1) + "	￤";





				#// ---------

				if ((lastWord2 == 2 and lastWord1 != 2 and lastWord1 > -1)) :

					lettersWord1 = line1.split(":")
					lettersWord1WithDiacritics = word2WithDiacritics.split("	")

					lettersWord2 = line2.split(":")
					lettersWord2WithDiacritics = word1WithDiacritics.split("	")

					line1 = ""
					for t in range(1, len(lettersWord1 - 2)) :
						line1 = line1 + ":" + lettersWord1[t]


					line1 = line1.replace(":┊:", "┊:")

					line1 = line1 + ":" + lettersWord1[len(lettersWord1) - 2][0:1] + ":0:￤"#// .substring(letters_word.length-1,
																											#// letters_word.length)
																											#// +
																											#// "┊:0:￤";

					word1WithDiacritics = lettersWord2WithDiacritics[0]
					for t in range(1, len(lettersWord2WithDiacritics) - 2):
						word1WithDiacritics = word1WithDiacritics + "	" + lettersWord2WithDiacritics[t]


					word1WithDiacritics = word1WithDiacritics + "	" + lettersWord2WithDiacritics[lettersWord2WithDiacritics.length - 2][0:1] + "	0	￤"

					line2 = ""

					for t in range(1, len(lettersWord2) - 2):
						line2 = line2 + ":" + lettersWord2[t]

					line2 = line2.replace(":┊:", "┊:")

					line2 = line2 + ":0:" + lettersWord2[len(lettersWord2) - 2][0:1] + ":￤"

					#// ----
					word2WithDiacritics = lettersWord1WithDiacritics[0]

					for t in range(1, len(lettersWord1WithDiacritics) - 2) :
						word2WithDiacritics = word2WithDiacritics + "	" + lettersWord1WithDiacritics[t]


					word2WithDiacritics = word2WithDiacritics + "	0	" + lettersWord1WithDiacritics[len(lettersWord1WithDiacritics) - 2] + "	￤" #//.substring(0, 1) + "	￤";



				if (printResults == True) :
					print(word1WithDiacritics)
					print(word2WithDiacritics)
					print(line1)
					print(line2)
					print("Global Similarity Score:")
					print(similarityScoreMatchesOriginal[i][0])
					print("Corrected Global Similarity Score:")
					print(similarityScoreMatchesOriginal[i][1])
					print("Attested Pairs:")
					print(attestedPhoneticPairs[i])
					print("Number of Attestations of the Attested Pairs:")
					print(nrAttestationsPhoneticPairs[i])
					print("----")


				newAlignment = Alignment()

				newAlignment.word1_WithDiacritics(word1WithDiacritics)
				newAlignment.word2_WithDiacritics(word2WithDiacritics)
				newAlignment.word1_WithoutDiacritics(line1)
				newAlignment.word2_WithoutDiacritics(line2)
				newAlignment.globalSimilarityScore(similarityScoreMatchesOriginal[i][0])
				newAlignment.correctedGlobalSimilarityScore(similarityScoreMatchesOriginal[i][1])
				newAlignment.phoneticPairs(attestedPhoneticPairs[i])
				newAlignment.nrAttestationsPhoneticPairs(nrAttestationsPhoneticPairs[i])


				results.append(copy.deepcopy(newAlignment))


				line1 = ""
				line2 = ""



		return results

