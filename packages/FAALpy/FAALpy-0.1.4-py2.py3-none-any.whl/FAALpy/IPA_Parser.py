#/*
# * Copyright 2018 Marwan Kilani
# *
# * Licensed under the Apache License, Version 2.0 (the "License")
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *    http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# */


#// =========================
#	// =========================
#	// =========================
#
#	/**
#	 * Method corresponding to the IPA_parser module. It parses one pair of words at
#	 * a time, using default values (see online documentation for their values).
#	 *
#	 * @param word1Base
#	 *            (String): IPA transcription of the first word to be aligned.
#	 * @param word2Base
#	 *            (String): IPA transcription of the second word to be aligned.
#	 * @param configIPA
#	 *            (List&ltString&gt): String array list with variables for the
#	 *            configuration of the IPA_parser.IPA_parser_new module. Instances
#	 *            of this list can be initialized through the <i>ConfigIPA</i> class
#	 *            - see the corresponding JavaDoc, and the documentation and
#	 *            examples online.
#	 *
#	 * @return Result output: ParsedWord
#	 *         <p>
#	 *         The <i>ParsedWord</i > object contains the results of the parsing of
#	 *         a word. The items stored in the <i>ParsedWord</i > class can be
#	 *         called as follow:
#	 *         <p>
#	 *         0. .getParsedWord1() - String: Parsed (without diacritics etc.) IPA
#	 *         transcription of word 1
#	 *         <p>
#	 *         1. .getParsedWord2() - String: Parsed (without diacritics etc.) IPA
#	 *         transcription of word 2
#	 *         <p>
#	 *         2. .getMatrixResultComparison_WithSaliences() - int[][]: feature
#	 *         matrix corrected according to the salience settings. The dimensions
#	 *         of the matrix correspond to the length of the parsed (i.e. without
#	 *         diacritics etc.) transcription of word 1 × the length of the parsed
#	 *         (i.e. without diacritics etc.) transcription of word 2.
#	 *         <p>
#	 *         3. .getMatrixResultComparison_WithoutSaliences() - int[][]: basic
#	 *         feature matrix without any salience correction. Dimension as previous
#	 *         one.
#	 *         <p>
#	 *         <p>
#	 */

from .Reader import *
from .ConfigIPA import *
from .ParsedWord import *

import os

import copy

class IPA_Parser :
	@staticmethod

#/**
#	#* Method corresponding to the IPA_parser module. It parses one pair of words at
#	# * a time, using default values (see online documentation for their values).
#	# *
#	# * @param word1Base
#	# *            (String): IPA transcription of the first word to be aligned.
#	# * @param word2Base
#	# *            (String): IPA transcription of the second word to be aligned.
#	# *
#	# * @return Result output: ParsedWord
#	# *         <p>
#	# *         The <i>ParsedWord</i > object contains the results of the parsing of
#	# *         a word. The items stored in the <i>ParsedWord</i > class can be
#	# *         called as follow:
#	# *         <p>
#	# *         0. .getParsedWord1() - String: Parsed (without diacritics etc.) IPA
#	# *         transcription of word 1
#	# *         <p>
#	# *         1. .getParsedWord2() - String: Parsed (without diacritics etc.) IPA
#	# *         transcription of word 2
#	# *         <p>
#	# *         2. .getMatrixResultComparison_WithSaliences() - int[][]: feature
#	# *         matrix corrected according to the salience settings. The dimensions
#	# *         of the matrix correspond to the length of the parsed (i.e. without
#	# *         diacritics etc.) transcription of word 1 × the length of the parsed
#	# *         (i.e. without diacritics etc.) transcription of word 2.
#	# *         <p>
#	# *         3. .getMatrixResultComparison_WithoutSaliences() - int[][]: basic
#	# *         feature matrix without any salience correction. Dimension as previous
#	# *         one.
#	# *         <p>
#	# *         <p>
#	# */

	def parseIPA(*args) :
		
		word1Base = ""
		word2Base = ""

		configIPA = []

		settingsConfigIPA = ConfigIPA()

		# // Configs files:

		configIPA = settingsConfigIPA.getConfigIPA()

		if len(args) == 2:
			word1Base = args[0]
			word2Base = args[1]

		elif len(args) == 3:
			word1Base = args[0]
			word2Base = args[1]
			configIPA = args[2]


#		// ￤ (U+FFE4) -> morphemic boundary
#		// ┊(U+250A) -> limits alignments
#
#		// variables & read config file
#
#		// diphthongs are coded as 0 if nothing, + if rising, - if falling -> columns 0,
#		// after the name



		locationFilePhoneticFeatures = configIPA[0]
		locationFilePhoneticDiacritics = configIPA[1]

		locationFileFeaturesDiphthongs = configIPA[2]
		locationFileFeaturesCoarticulation = configIPA[3]

		locationPhonCategories = configIPA[4]
		locationSaliencesMatchesPhonCategories = configIPA[5]

		word1 = ""
		word2 = ""

		tablePhoneticFeatures = ""
		tableFeaturesDiphthongs = ""
		tableFeaturesCoarticulation = ""
		diacriticsPhoneticFeatures = ""
		saliencesFeaturesPhonCategoriesFile = ""

		linesPhoneticFeatures = []
		linesFeaturesDiphthongs = []
		linesFeaturesCoarticulation = []
		linesPhoneticFeaturesProvisional = []

		linesDiacriticsPhoneticFeatures = []

		valuesPhoneticFeatures  = []
		valuesFeaturesDiphthongs  = []
		valuesFeaturesCoarticulation = []

		word1PhonCategory_FeatureA = []
		word1PhonCategory_FeatureB = []

		word2PhonCategory_FeatureA = []
		word2PhonCategory_FeatureB = []

		lengthWord1 = len(word1)
		lengthWord2 = len(word2)

		featuresWord1 = []
		featuresWord2 = []

		phonesWord1 = []
		phonesWord2 = []

		#// check if there is any morphemic boundary, if one has and the other not, add
		#// one at the end of the other
		#// as if one has at least one morhemic boundary, both need at least one

		if (word1Base.find("￤") > -1 and word2Base.find("￤") < 0):
			word2Base = word2Base + "￤"
		elif (word1Base.find("￤") < 0 and word2Base.find("￤") > -1):
			word1Base = word1Base + "￤"

		#// check if there is a morphemic boundary at the end, if not add one
		if word2Base[-1] != "￤":
			word2Base = word2Base + "￤"

		if word1Base[-1] != "￤":
			word1Base = word1Base + "￤"


		phonesWord1 = list(word1Base)
		phonesWord2 = list(word2Base)





		#// retrieve Phonological categories

		filePhonCategories = ""
		filePhonCategoriesLines = []
		filePhonCategoriesItems = []
		phonologicalCategoriesCharacter = []
		phonologicalCategoriesFirstFeature = []
		phonologicalCategoriesSecondFeature = []

		filePhonCategories = Reader.readFile(locationPhonCategories)



		filePhonCategoriesLines = filePhonCategories.split("\n")

		for i in range(0, len(filePhonCategoriesLines)):

			if (filePhonCategoriesLines[i].find("%") < 0):



				filePhonCategoriesItems = filePhonCategoriesLines[i].split("	")
				phonologicalCategoriesCharacter.append(copy.deepcopy(filePhonCategoriesItems[0]))
				phonologicalCategoriesFirstFeature.append(copy.deepcopy(filePhonCategoriesItems[1]))
				phonologicalCategoriesSecondFeature.append(copy.deepcopy(filePhonCategoriesItems[2]))




		#// retrieve saliences to use for matches for Phonological categories


		fileSaliencesMatchesPhonCategories = ""
		fileSaliencesMatchesPhonCategoriesLines = []
		fileSaliencesMatchesPhonCategoriesItems = []
		phonologicalCategoriesFeature_A1 = []
		phonologicalCategoriesFeature_B1 = []
		phonologicalCategoriesFeature_A2 = []
		phonologicalCategoriesFeature_B2 = []
		phonologicalCategoriesLocationSaliences = []

		fileSaliencesMatchesPhonCategories = Reader.readFile(locationSaliencesMatchesPhonCategories)

		fileSaliencesMatchesPhonCategoriesLines = fileSaliencesMatchesPhonCategories.split("\n")

		for i in range(0, len(fileSaliencesMatchesPhonCategoriesLines)):

			if fileSaliencesMatchesPhonCategoriesLines[i][0] != "%" :

				fileSaliencesMatchesPhonCategoriesItems = fileSaliencesMatchesPhonCategoriesLines[i].split("	")

				phonologicalCategoriesFeature_A1.append(copy.deepcopy(fileSaliencesMatchesPhonCategoriesItems[0]))
				phonologicalCategoriesFeature_A2.append(copy.deepcopy(fileSaliencesMatchesPhonCategoriesItems[1]))
				phonologicalCategoriesFeature_B1.append(copy.deepcopy(fileSaliencesMatchesPhonCategoriesItems[3]))
				phonologicalCategoriesFeature_B2.append(copy.deepcopy(fileSaliencesMatchesPhonCategoriesItems[4]))

				phonologicalCategoriesLocationSaliences.append(os.path.join(os.path.dirname(__file__), copy.deepcopy(fileSaliencesMatchesPhonCategoriesItems[6])))





		#// ========================
		#// read phonetic features

		tablePhoneticFeatures = Reader.readFile(locationFilePhoneticFeatures)

		linesPhoneticFeatures = tablePhoneticFeatures.split("\n")

		for i in range(0, len(linesPhoneticFeatures)) :

			if (linesPhoneticFeatures[i].find("%") < 0) :
				dataPhoneticFeatures = linesPhoneticFeatures[i].split("	")

				valuesPhoneticFeatures.append(copy.deepcopy(dataPhoneticFeatures))


		#// read features modified by secondary elements of diphthongs

		tableFeaturesDiphthongs = Reader.readFile(locationFileFeaturesDiphthongs)

		linesFeaturesDiphthongs = tableFeaturesDiphthongs.split("\n")

		for i in range(0, len(linesFeaturesDiphthongs)) :

			if linesFeaturesDiphthongs[i].find("%") < 0:
				valuesFeaturesDiphthongs.append(copy.deepcopy(linesFeaturesDiphthongs[i]))
			
		

		#// read features modified by secondary elements of coarticulated sequences

		tableFeaturesCoarticulation = Reader.readFile(locationFileFeaturesCoarticulation)

		linesFeaturesCoarticulation = tableFeaturesCoarticulation.split("\n")

		for i in range(0, len(linesFeaturesCoarticulation)):

			if (linesFeaturesCoarticulation[i].find("%") < 0) :
				valuesFeaturesCoarticulation.append(copy.deepcopy(linesFeaturesCoarticulation[i]))
			
		

		#// read diacritics

		diacriticsPhoneticFeatures = Reader.readFile(locationFilePhoneticDiacritics)

		linesPhoneticFeaturesProvisional = diacriticsPhoneticFeatures.split("\n")

		for i in range(0, len(linesPhoneticFeaturesProvisional)) :

			if (linesPhoneticFeaturesProvisional[i].find("%") < 0):
				linesDiacriticsPhoneticFeatures.append(copy.deepcopy(linesPhoneticFeaturesProvisional[i]))
			
		

		linesDiacriticsPhoneticFeatures.append("̯	2	01") #// marked with 2 to distinguish it from normal diacritics
		linesDiacriticsPhoneticFeatures.append("͜	3	02") #// marked with 3 to distinguish it from normal diacritics

		valuesDiacriticsPhoneticFeatures = []
		classDiacriticsPhoneticFeatures = []

		diacriticsPhoneticFeaturesChanged = []
		diacriticsPhoneticFeaturesChangedValue = []

		for i in range(0, len(linesDiacriticsPhoneticFeatures)):
			diacriticsSplit1 = []
			diacriticsSplit2 = []
			diacriticsSplit3 = []

			featuresChanged = []
			featuresChangedValue = []

			diacriticsSplit1 = linesDiacriticsPhoneticFeatures[i].split("	")
			diacriticsSplit2 = diacriticsSplit1[2].split(" ")

			valuesDiacriticsPhoneticFeatures.append(copy.deepcopy(diacriticsSplit1[0]))
			classDiacriticsPhoneticFeatures.append(copy.deepcopy(diacriticsSplit1[1]))

			for n in range(0, len(diacriticsSplit2)):

				diacriticsSplit3 = list(diacriticsSplit2[n])
				featuresChanged.append(copy.deepcopy(diacriticsSplit3[0]))
				featuresChangedValue.append(copy.deepcopy(diacriticsSplit3[1]))



			diacriticsPhoneticFeaturesChanged.append(copy.deepcopy(featuresChanged))
			diacriticsPhoneticFeaturesChangedValue.append(copy.deepcopy(featuresChangedValue))



		#// preliminary parsing -> diphthongs coarticulation diacritics that precede
		#// the letter they refer to

		#// diphthongs

		for i in range(0, len(phonesWord1)):
			if (phonesWord1[i] == "͜") :
				phonesWord1[i] = phonesWord1[i + 1]
				phonesWord1[i + 1] = "͜"
				i += 1



		for i in range(0, len(phonesWord2)):

			if (phonesWord2[i] == ("͜")) :
				phonesWord2[i] = phonesWord2[i + 1]
				phonesWord2[i + 1] = "͜"
				i+= 1




		#// coarticulation

		for i in range(0, len(phonesWord1)):
			if (phonesWord1[i] == ("͡")) :
				phonesWord1[i] = phonesWord1[i + 1]
				phonesWord1[i + 1] = "͡"
				i+= 1



		for i in range(0, len(phonesWord2)):

			if (phonesWord2[i] == ("͡")) :
				phonesWord2[i] = phonesWord2[i + 1]
				phonesWord2[i + 1] = "͡"
				i+= 1




		#// diacritics that precede the letter they refer to

		for i in range(0, len(phonesWord1)):
			for n in range(0, len(classDiacriticsPhoneticFeatures)):
				if (phonesWord1[i] == (valuesDiacriticsPhoneticFeatures[n]) and classDiacriticsPhoneticFeatures[n] == ("1")) :
					phonesWord1[i] = phonesWord1[i + 1]
					phonesWord1[i + 1] = valuesDiacriticsPhoneticFeatures[n]
					i += 1
				
			
		

		for i in range(0, len(phonesWord2)):
			for n in range(0, len(classDiacriticsPhoneticFeatures)):
				if (phonesWord2[i] == (valuesDiacriticsPhoneticFeatures[n]) \
						and classDiacriticsPhoneticFeatures[n] == ("1")) :
					phonesWord2[i] = phonesWord2[i + 1]
					phonesWord2[i + 1] = valuesDiacriticsPhoneticFeatures[n]
					i += 1





		#// read salience features phonological categories


		listSaliencesFeaturesCategories = []
		listSaliencesFeaturesCategoriesValue = []


		for y in range(0, len(phonologicalCategoriesLocationSaliences)):

			linesSaliencesFeaturesPhonCategoriesProvisional = []
			linesSaliencesFeaturesPhonCategories = []
			locationFileSaliences = phonologicalCategoriesLocationSaliences[y]

			#//----
	
			saliencesFeaturesPhonCategoriesFile = Reader.readFile(locationFileSaliences)
	
			linesSaliencesFeaturesPhonCategoriesProvisional = saliencesFeaturesPhonCategoriesFile.split("\n")
	
			for i in range(0, len(linesSaliencesFeaturesPhonCategoriesProvisional)):
	
				if (linesSaliencesFeaturesPhonCategoriesProvisional[i].find("%") < 0) :
					linesSaliencesFeaturesPhonCategories.append(copy.deepcopy(linesSaliencesFeaturesPhonCategoriesProvisional[i]))
				
			
	
			saliencesFeaturesPhonCategories = []
			saliencesFeaturesPhonCategoriesValue = []
	
			for i in range(0, len(linesSaliencesFeaturesPhonCategories)):
	
				saliencePhonCategoriesSplit = []
	
				saliencePhonCategoriesSplit = linesSaliencesFeaturesPhonCategories[i].split("	")
	
				saliencesFeaturesPhonCategories.append(copy.deepcopy(saliencePhonCategoriesSplit[0]))
				saliencesFeaturesPhonCategoriesValue.append(copy.deepcopy(saliencePhonCategoriesSplit[1]))
	
			
	
			#//----
	
	
			listSaliencesFeaturesCategories.append(copy.deepcopy(saliencesFeaturesPhonCategories))
			listSaliencesFeaturesCategoriesValue.append(copy.deepcopy(saliencesFeaturesPhonCategoriesValue))


		


		#// read phonetic features

		#// ================
		#// parsing
		#// ------------



		#// parse word A
		#// compile feature list for word A


		for i in range(0, len(phonesWord1)):

			#// diphthongs - modify according to diacritics
			for n in range(0, len(valuesDiacriticsPhoneticFeatures)):

				if (phonesWord1[i] == (valuesDiacriticsPhoneticFeatures[n])) :

					if (phonesWord1[i] == ("͜")) :
						phonesWord1[i - 2] = "$"

						#//------
						for x in range(0, len(valuesFeaturesDiphthongs)):
							m = valuesFeaturesDiphthongs[x]

							if ((featuresWord1[-2][m] == "+" and featuresWord1[-1][m] == ("-"))
									or (featuresWord1[-2][m] == ("-") and featuresWord1[-1][m] == ("+"))) :
								featuresWord1[-1][m] = "±"
							elif ((featuresWord1[-2][m] == ("+") and featuresWord1[-1][m] == ("0"))
									or (featuresWord1[-2][m] == ("0") and featuresWord1[-1][m] == ("+"))) :
								featuresWord1[-1][m] = "⁰"
							elif ((featuresWord1[-2][m] == ("-") and featuresWord1[-1][m] == ("0"))
									or (featuresWord1[-2][m] == ("0") and featuresWord1[-1][m] == ("-"))) :
								featuresWord1[-1][m] = "₀"





						featuresWord1.pop(-2)
						word1 = word1[0:-2] + word1[-1]

						word1PhonCategory_FeatureA.pop(-2)
						word1PhonCategory_FeatureB.pop(-2)





					if (phonesWord1[i] == ("̯")) :
						phonesWord1[i - 1] = "$"

						#//------
						for x in range(0, len(valuesFeaturesDiphthongs)) :
							m = valuesFeaturesDiphthongs[x]

							if ((featuresWord1[-2][m] == ("+") and featuresWord1[-1][m] == ("-"))
									or (featuresWord1[-2][m] == ("-") and featuresWord1[-1][m] == ("+"))):
								featuresWord1[-2][m] = "±"
							elif ((featuresWord1[-2][m] == ("+") and featuresWord1[-1][m] == ("0"))
									or (featuresWord1[-2][m] == ("0") and featuresWord1[-1][m] == ("+"))):
								featuresWord1[-2][m] = "⁰"
							elif ((featuresWord1[-2][m] == ("-") and featuresWord1[-1][m] == ("0"))
									or (featuresWord1[-2][m] == ("0") and featuresWord1[-1][m] == ("-"))):
								featuresWord1[-2][m] = "₀"





						featuresWord1.pop(-1)
						word1 = word1[0:-1]

						word1PhonCategory_FeatureA.pop(-1)
						word1PhonCategory_FeatureB.pop(-1)





			#// process coarticualted phones

			if (phonesWord1[i] == ("͡")) :
				phonesWord1[i - 1] = "$"

				for x in range(0, len(valuesFeaturesCoarticulation)) :
					m = valuesFeaturesCoarticulation[x]

					if ((featuresWord1[-2][m] == ("+") and featuresWord1[-1][m] == ("-"))
						or (featuresWord1[-2][m] == ("-") and featuresWord1[-1][m] == ("+"))) :
						featuresWord1[-2][m] = "±"
					elif ((featuresWord1[-2][m] == ("+") and featuresWord1[-1][m] == ("0"))
						  or (featuresWord1[-2][m] == ("0") and featuresWord1[-1][m] == ("+"))) :
						featuresWord1[-2][m] = "⁰"
					elif ((featuresWord1[-2][m] == ("-") and featuresWord1[-1][m] == ("0"))
						  or (featuresWord1[-2][m] == ("0") and featuresWord1[-1][m] == ("-"))) :
						featuresWord1[-2][m] = "₀"




				featuresWord1.pop(-1)
				word1 = word1[0:-1]

				word1PhonCategory_FeatureA.pop(-1)
				word1PhonCategory_FeatureB.pop(-1)



			#// modify according to diacritics
			for n in range(0, len(valuesDiacriticsPhoneticFeatures)):

				if (phonesWord1[i] == (valuesDiacriticsPhoneticFeatures[n])) :
					for m in range(0, len(diacriticsPhoneticFeaturesChanged[n])):

						featuresWord1[-1][int(diacriticsPhoneticFeaturesChanged[n][m])] = diacriticsPhoneticFeaturesChangedValue[n][m]







			#// modify according to vowel-semiconsonant-consonant

			#// end modify according to vowel-semiconsonant-consonant



			if (phonesWord1[i] == ("￤")) :

				#// morpheme boundary

				word1 = word1 + "￤"



				featuresWord1.append(copy.deepcopy(valuesPhoneticFeatures[0]))
				featuresWord1[-1].pop(0)
				for m in range(0, len(featuresWord1[-1])) :

					featuresWord1[-1][m] = "9"


				word1PhonCategory_FeatureA.append("9")
				word1PhonCategory_FeatureB.append("9")



			#// IPA basic transcription - create new word without diacritics

			for n in range(0, len(valuesPhoneticFeatures)):

				if (phonesWord1[i] == (valuesPhoneticFeatures[n][0])) :





						word1PhonCategory_FeatureA.append(copy.deepcopy(phonologicalCategoriesFirstFeature[n]))
						word1PhonCategory_FeatureB.append(copy.deepcopy(phonologicalCategoriesSecondFeature[n]))


						word1 = word1 + valuesPhoneticFeatures[n][0]

						featuresWord1.append(copy.deepcopy(valuesPhoneticFeatures[n]))
						featuresWord1[-1].pop(0)











		#// word B
		#// compile feature list for word B
		for i in range(0, len(phonesWord2)):

			#// diphthongs - modify according to diacritics
			for n in range(0, len(valuesDiacriticsPhoneticFeatures)):

				if (phonesWord2[i] == (valuesDiacriticsPhoneticFeatures[n])) :

					if (phonesWord2[i] == ("͜")) :
						phonesWord2[i - 2] = "$"

						#//------
						for x  in range(0, len(valuesFeaturesDiphthongs)):
							m = valuesFeaturesDiphthongs[x]

							if ((featuresWord2[-2][m] == ("+")
									and featuresWord2[-1][m] == ("-"))
									or (featuresWord2[-2][m] == ("-")
											and featuresWord2[-1][m] == ("+"))) :
								featuresWord2[-1][m] = "±"
							elif ((featuresWord2[-2][m] == ("+")
									and featuresWord2[-1][m] == ("0"))
									or (featuresWord2[-2][m] == ("0")
											and featuresWord2[-1][m] == ("+"))) :
								featuresWord2[-1][m] = "⁰"
							elif ((featuresWord2[-2][m] == ("-")
									and featuresWord2[-1][m] == ("0"))
									or (featuresWord2[-2][m] == ("0")
											and featuresWord2[-1][m] == ("-"))) :
								featuresWord2[-1][m] =  "₀"





						featuresWord2.pop(-2)
						word2 = word2[0:-2] + word2[-1]

						word2PhonCategory_FeatureA.pop(-2)
						word2PhonCategory_FeatureB.pop(-2)


					if (phonesWord2[i] == ("̯")) :
						phonesWord2[i - 1] = "$"

						#//------
						for x in range(0, len(valuesFeaturesDiphthongs)):
							m = valuesFeaturesDiphthongs[x]

							if ((featuresWord2[-2][m] == ("+") and featuresWord2[-1][m] == ("-"))
									or (featuresWord2[-2][m] == ("-") and featuresWord2[-1][m] == ("+"))) :
								featuresWord2[-2][m] = "±"
							elif ((featuresWord2[-2][m] == ("+") and featuresWord2[-1][m] == ("0"))
									or (featuresWord2[-2][m] == ("0") and featuresWord2[-1][m] == ("+"))) :
								featuresWord2[-2][m] = "⁰"
							elif ((featuresWord2[-2][m] == ("-") and featuresWord2[-1][m] == ("0"))
									or (featuresWord2[-2][m] == ("0") and featuresWord2[-1][m] == ("-"))) :
								featuresWord2[-2][m] = "₀"





						featuresWord2.pop(-1)
						word2 = word2[0:-1]

						word2PhonCategory_FeatureA.pop(-1)
						word2PhonCategory_FeatureB.pop(-1)





			#// process coarticualted phones

			if (phonesWord2[i] == ("͡")) :
				phonesWord2[i - 1] = "$"

				for x in range(0, len(valuesFeaturesCoarticulation)):
					m = valuesFeaturesCoarticulation[x]

					if ((featuresWord2[-2][m] == ("+")
							and featuresWord2[-1][m] == ("-"))
							or (featuresWord2[-2][m] == ("-")
									and featuresWord2[-1][m] == ("+"))) :
						featuresWord2[-2][m] = "±"
					elif ((featuresWord2[-2][m] == ("+") and featuresWord2[-1][m] == ("0"))
							or (featuresWord2[-2][m] == ("0") and featuresWord2[-1][m] == ("+"))) :
						featuresWord2[-2][m] = "⁰"
					elif ((featuresWord2[-2][m] == ("-")
							and featuresWord2[-1][m] == ("0"))
							or (featuresWord2[-2][m] == ("0") and featuresWord2[-1][m] == ("-"))):
						featuresWord2[-2][m] = "₀"




				featuresWord2.pop(-1)
				word2 = word2[0:-1]

				word2PhonCategory_FeatureA.pop(-1)
				word2PhonCategory_FeatureB.pop(-1)



			for n in range(0, len(valuesDiacriticsPhoneticFeatures)):

				if (phonesWord2[i] == (valuesDiacriticsPhoneticFeatures[n])) :

					for m in range (0, len(diacriticsPhoneticFeaturesChanged[n])) :

						featuresWord2[-1][int(diacriticsPhoneticFeaturesChanged[n][m])] = diacriticsPhoneticFeaturesChangedValue[n][m]







			#// end modify according to diacritics

			#// modify according to vowel-semiconsonant-consonant

			#// end modify according to vowel-semiconsonant-consonant

			if (phonesWord2[i] == ("￤")) :

				#// morpheme boundary

				word2 = word2 + "￤"



				featuresWord2.append(copy.deepcopy(valuesPhoneticFeatures[0]))
				featuresWord2[-1].pop(0)

				for m in range(0, len(featuresWord2[-1])) :

					featuresWord2[-1][m] = "9"
				

				word2PhonCategory_FeatureA.append("9")
				word2PhonCategory_FeatureB.append("9")

			

			for n in range(0, len(valuesPhoneticFeatures)):

				#// IPA basic transcription - create new word without diacritics
				if (phonesWord2[i] == (valuesPhoneticFeatures[n][0])) :




						word2PhonCategory_FeatureA.append(copy.deepcopy(phonologicalCategoriesFirstFeature[n]))
						word2PhonCategory_FeatureB.append(copy.deepcopy(phonologicalCategoriesSecondFeature[n]))

						word2 = word2 + valuesPhoneticFeatures[n][0]

						featuresWord2.append(copy.deepcopy(valuesPhoneticFeatures[n]))
						featuresWord2[-1].pop(0)




				
			
		

		#// count common features and make matrix

		lengthWord1 = len(word1)
		lengthWord2 = len(word2)

		matrixResultComparison_WithSaliences = [] #[[0] * lengthWord2] * lengthWord1
		matrixResultComparison_WithoutSaliences = [] #[[0] * lengthWord2] * lengthWord1

		for x in range(0, lengthWord1):
			temp_array_1 = []
			temp_array_2 = []
			for y in range(0, lengthWord2):
				temp_array_1.append(0)
				temp_array_2.append(0)

			matrixResultComparison_WithSaliences.append(temp_array_1)
			matrixResultComparison_WithoutSaliences.append(temp_array_2)


		for i in range(0, lengthWord1):
			for n in range(0, lengthWord2):

				matrixResultComparison_WithSaliences[i][n] = 0
				matrixResultComparison_WithoutSaliences[i][n] = 0

			
		


		#// create new matrix with values modified according to salience settings
		for i in range(0, lengthWord1):
			for n in range(0, lengthWord2):

				saliencesFeatures = []
				saliencesFeaturesValue = []


				for y in range(0, len(phonologicalCategoriesFeature_A1)):


					if(
							(
							(phonologicalCategoriesFeature_A1[y] == word1PhonCategory_FeatureA[i] and  phonologicalCategoriesFeature_A2[y] == word2PhonCategory_FeatureA[n])
							or
							(phonologicalCategoriesFeature_A1[y] == word2PhonCategory_FeatureA[n] and  phonologicalCategoriesFeature_A2[y] == word1PhonCategory_FeatureA[i])
							)
							and
							(
							(phonologicalCategoriesFeature_B1[y] == word1PhonCategory_FeatureB[i] and  phonologicalCategoriesFeature_B2[y] == word2PhonCategory_FeatureB[n])
							or
							(phonologicalCategoriesFeature_B1[y] == word2PhonCategory_FeatureB[n] and  phonologicalCategoriesFeature_B2[y] == word1PhonCategory_FeatureB[i])
							)
						) :

						saliencesFeatures = copy.deepcopy(listSaliencesFeaturesCategories[y])
						saliencesFeaturesValue = copy.deepcopy(listSaliencesFeaturesCategoriesValue[y])
						break





				#//------



				for o in range(0, len(featuresWord2[0])) :



					if (featuresWord1[i][o] == (featuresWord2[n][o])) :

						matrixResultComparison_WithoutSaliences[i][n] += 1

						for f in range(0, len(saliencesFeatures)) :
							if (str(o) == saliencesFeatures[f]) :

								for g in range(0, int(saliencesFeaturesValue[f])) :
									matrixResultComparison_WithSaliences[i][n] += 1




					elif ((featuresWord1[i][o] == ("±") and (featuresWord2[n][o] == ("-")
							or featuresWord2[n][o] == ("+") or featuresWord2[n][o] == ("±")))
							or (featuresWord1[i][o] == ("⁰") and (featuresWord2[n][o] == ("0")
									or featuresWord2[n][o] == ("+")
									or featuresWord1[i][o] == ("⁰")))
							or (featuresWord1[i][o] == ("₀") and (featuresWord2[n][o] == ("0")
									or featuresWord2[n][o] == ("-")
									or featuresWord1[i][o] == ("₀")))) : #// &
																		#			// featuresWord1[i].get(1) == ("+")
																		#			// &
																		#			// featuresWord1[i].get(1) == ("+")){
						matrixResultComparison_WithoutSaliences[i][n] += 1

						for f in range(0, len(saliencesFeatures)) :
							if (str(o) == saliencesFeatures[f]) :

								for g in range(0, int(saliencesFeaturesValue[f])) :
									matrixResultComparison_WithSaliences[i][n] += 1




					elif (((featuresWord1[i][o] == ("-") or featuresWord1[i][o] == ("+"))
							and featuresWord2[n][o] == ("±"))
							or ((featuresWord1[i][o] == ("0") or featuresWord1[i][o] == ("+"))
									and featuresWord2[n][o] == ("⁰"))
							or ((featuresWord1[i][o] == ("0") or featuresWord1[i][o] == ("-"))
									and featuresWord2[n][o] == ("₀"))) :
						matrixResultComparison_WithoutSaliences[i][n] += 1

						for f in range(0, len(saliencesFeatures)) :
							if (str(o) == saliencesFeatures[f]) :

								for g in range(0, int(saliencesFeaturesValue[f])) :
									matrixResultComparison_WithSaliences[i][n] += 1
								
							
						
					

				

				if (featuresWord1[i][0] == ("9") and featuresWord2[n][0] == ("9")) :

					for j in range(0, 30) :
						matrixResultComparison_WithSaliences[i][n] += 1


					matrixResultComparison_WithoutSaliences[i][n] += 1

					for f in range(0, len(saliencesFeaturesValue)) :
						for g in range(0, saliencesFeaturesValue[f]) :
							matrixResultComparison_WithSaliences[i][n] += 1





				if (featuresWord1[i][0] == ("9") and featuresWord2[n][0] != ("9")) : #// &
																					#						// featuresWord1[i].get(1) == ("+")
																					#						// &
																					#						// featuresWord1[i].get(1) == ("+")){

					matrixResultComparison_WithSaliences[i][n] = -1000
					matrixResultComparison_WithoutSaliences[i][n] = -1000



				if (featuresWord1[i][0] != ("9") and featuresWord2[n][0] == ("9")) :#// &
																											#// featuresWord1[i].get(1) == ("+")
																											#// &
																											#// featuresWord1[i].get(1) == ("+")){

					matrixResultComparison_WithSaliences[i][n] = -1000
					matrixResultComparison_WithoutSaliences[i][n] = -1000




		#// organize and return results

		resultParsing = ParsedWord()




		resultParsing.parsedWord1(word1)
		resultParsing.parsedWord2(word2)
		resultParsing.matrixResultComparison_WithSaliences(matrixResultComparison_WithSaliences)
		resultParsing.matrixResultComparison_WithoutSaliences(matrixResultComparison_WithoutSaliences)


		return resultParsing

