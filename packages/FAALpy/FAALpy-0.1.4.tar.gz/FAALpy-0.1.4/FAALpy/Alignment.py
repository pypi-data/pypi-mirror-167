class Alignment :
    word1_WithDiacritics = None
    word2_WithDiacritics = None
    word1_WithoutDiacritics = None
    word2_WithoutDiacritics = None
    globalSimilarityScore = None
    correctedGlobalSimilarityScore = None
    phoneticPairs = None
    nrAttestationsPhoneticPairs = None
    # *
    # 	 * Stores the aligned word 1, with diacritics.
    # 	 *
    # 	 * @param alignmentWord1_WithDiacritics
    # 	 *            (String): aligned word 1, with diacritics.
    def word1_WithDiacritics(self, alignmentWord1_WithDiacritics) :
        self.word1_WithDiacritics = alignmentWord1_WithDiacritics
    # *
    # 	 * Stores the aligned word 2, with diacritics.
    # 	 *
    # 	 * @param alignmentWord2_WithDiacritics
    # 	 *            (String): aligned word 2, with diacritics.
    def word2_WithDiacritics(self, alignmentWord2_WithDiacritics) :
        self.word2_WithDiacritics = alignmentWord2_WithDiacritics
    # *
    # 	 * Stores the aligned word 1, without diacritics.
    # 	 *
    # 	 * @param alignmentWord1_WithoutDiacritics
    # 	 *            (String): aligned word 1, without diacritics.
    def word1_WithoutDiacritics(self, alignmentWord1_WithoutDiacritics) :
        self.word1_WithoutDiacritics = alignmentWord1_WithoutDiacritics
    # *
    # 	 * Stores the aligned word 2, without diacritics.
    # 	 *
    # 	 * @param alignmentWord2_WithoutDiacritics
    # 	 *            (String): aligned word 2, without diacritics.
    def word2_WithoutDiacritics(self, alignmentWord2_WithoutDiacritics) :
        self.word2_WithoutDiacritics = alignmentWord2_WithoutDiacritics
    # *
    # 	 * Stores the Global Similarity Score.
    # 	 *
    # 	 * @param alignmentGlobalSimilarityScore
    # 	 *            (Double): Global Similarity Score.
    def globalSimilarityScore(self, alignmentGlobalSimilarityScore) :
        self.globalSimilarityScore = alignmentGlobalSimilarityScore
    # *
    # 	 * Stores the Corrected Global Similarity Score.
    # 	 *
    # 	 * @param alignmentCorrectedGlobalSimilarityScore
    # 	 *            (Double): Corrected Global Similarity Score.
    def correctedGlobalSimilarityScore(self, alignmentCorrectedGlobalSimilarityScore) :
        self.correctedGlobalSimilarityScore = alignmentCorrectedGlobalSimilarityScore
    # *
    # 	 * Stores the list of phonetic pairs attested in the alignment.
    # 	 *
    # 	 * @param alignmentPhoneticPairs
    # 	 *            List<String>: Attested Phonetic Pairs.
    def phoneticPairs(self, alignmentPhoneticPairs) :
        self.phoneticPairs = alignmentPhoneticPairs
    # *
    # 	 * Stores the numbers of attestations of the phonetic pairs identified by the algorithm.
    # 	 *
    # 	 * @param alignmentNrAttestationsPhoneticPairs
    # 	 *            List<Integer>: numbers of attestations of the phonetic pairs.
    def nrAttestationsPhoneticPairs(self, alignmentNrAttestationsPhoneticPairs) :
        self.nrAttestationsPhoneticPairs = alignmentNrAttestationsPhoneticPairs
    # get
    # *
    # 	 * Returns the the aligned word 1, with diacritics.
    def  getWord1_WithDiacritics(self) :
        return self.word1_WithDiacritics
    # *
    # 	 * Returns the the aligned word 2, with diacritics.
    def  getWord2_WithDiacritics(self) :
        return self.word2_WithDiacritics
    # *
    # 	 * Returns the the aligned word 1, without diacritics.
    def  getWord1_WithoutDiacritics(self) :
        return self.word1_WithoutDiacritics
    # *
    # 	 * Returns the the aligned word 2, without diacritics.
    def  getWord2_WithoutDiacritics(self) :
        return self.word2_WithoutDiacritics
    # *
    # 	 * Returns the Global Similarity Score.
    def  getGlobalSimilarityScore(self) :
        return self.globalSimilarityScore
    # *
    # 	 * Returns the Corrected Global Similarity Score.
    def  getCorrectedGlobalSimilarityScore(self) :
        return self.correctedGlobalSimilarityScore
    # *
    # 	 * Returns the list of phonetic pairs attested within the alignment. Each item on the list corresponds to a phonetic pair, and it is stored as a string with the following syntax: "phoneme_A - phoneme_B"
    def  getPhoneticPairs(self) :
        return self.phoneticPairs
    # *
    # 	 * Returns the numbers of attestations for each phonetic pairs identified by the algorithm.
    def  getNrAttestationsPhoneticPairs(self) :
        return self.nrAttestationsPhoneticPairs