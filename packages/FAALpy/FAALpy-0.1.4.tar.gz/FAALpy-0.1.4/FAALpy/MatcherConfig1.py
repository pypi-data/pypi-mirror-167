class MatcherConfig1 :
    arrayMatcherConfig1 = [None] * (8)
    matcherConfig1 =  []
    # *
    # 	 * Print results.
    # 	 * 
    # 	 * @param printResults
    # 	 *            (Boolean).
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: true
    def printResults(self, printResults) :
        self.arrayMatcherConfig1[0] = printResults
    # *
    # 	 * Introduce a minimum limit of features that need to be attested in order to
    # 	 * count the match.
    # 	 * 
    # 	 * @param minimumLimitFeatures
    # 	 *            (Boolean).
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: false
    def minimumLimitFeatures(self, minimumLimitFeatures) :
        self.arrayMatcherConfig1[1] = minimumLimitFeatures
    # *
    # 	 * Automatically detect morphemic boundaries and automatically adapting
    # 	 * Global/Corrected Global Similarity Score used.
    # 	 * 
    # 	 * @param autoDetectMorphBound
    # 	 *            (Boolean).
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: true
    def autoDetectMorphBound(self, autoDetectMorphBound) :
        self.arrayMatcherConfig1[2] = autoDetectMorphBound
    # *
    # 	 * If semiconsonants do not match, they are not counted.
    # 	 * 
    # 	 * @param excludeSemicons
    # 	 *            (Boolean).
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: false
    def excludeSemiconsonants(self, excludeSemicons) :
        self.arrayMatcherConfig1[3] = excludeSemicons
    # *
    # 	 * If vowels do not match, they are not counted.
    # 	 * 
    # 	 * @param excludeVows
    # 	 *            (Boolean).
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: false
    def excludeVowels(self, excludeVows) :
        self.arrayMatcherConfig1[4] = excludeVows
    # *
    # 	 * If vowels do not match, they are not counted, except if they are at the
    # 	 * beginning of a word.
    # 	 * 
    # 	 * @param excludeNonInitialVows
    # 	 *            (Boolean).
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: false
    def excludeNonInitialVowels(self, excludeNonInitialVows) :
        self.arrayMatcherConfig1[5] = excludeNonInitialVows
    # *
    # 	 * Display automatically recognized boundaries.
    # 	 * 
    # 	 * @param displayBoundaries
    # 	 *            (Boolean).
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: true
    def displayBoundaries(self, displayBoundaries) :
        self.arrayMatcherConfig1[6] = displayBoundaries
    # *
    # 	 * Match only phonemes belonging to the same category (consonants, vowels,
    # 	 * semiconsonants).
    # 	 * 
    # 	 * @param matchOnlySameCategory
    # 	 *            (Boolean).
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: true
    def matchOnlySameCategory(self, matchOnlySameCategory) :
        self.arrayMatcherConfig1[7] = matchOnlySameCategory
    # *
    # 	 * Returns the a list with the parameters for the matcherConfig1 parameters.
    def  getmatcherConfig1(self) :
        if (self.arrayMatcherConfig1[0] == None) :
            # print results:
            self.matcherConfig1.append(True)
        else :
            self.matcherConfig1.append(self.arrayMatcherConfig1[0])
        if (self.arrayMatcherConfig1[1] == None) :
            # introducing a minimum limit of features that need to be attested in order to
            # count the match:
            self.matcherConfig1.append(False)
        else :
            self.matcherConfig1.append(self.arrayMatcherConfig1[1])
        if (self.arrayMatcherConfig1[2] == None) :
            # automatically detecting morphemic boundaries and automatically adapting
            # Global/Corrected Global Similarity Score used:
            self.matcherConfig1.append(True)
        else :
            self.matcherConfig1.append(self.arrayMatcherConfig1[2])
        if (self.arrayMatcherConfig1[3] == None) :
            # if semiconsonants do not match, they are not counted:
            self.matcherConfig1.append(False)
        else :
            self.matcherConfig1.append(self.arrayMatcherConfig1[3])
        if (self.arrayMatcherConfig1[4] == None) :
            # if vowels do not match, they are not counted:
            self.matcherConfig1.append(False)
        else :
            self.matcherConfig1.append(self.arrayMatcherConfig1[4])
        if (self.arrayMatcherConfig1[5] == None) :
            # if vowels do not match, they are not counted, except if they are at the
            # beginning of a word:
            self.matcherConfig1.append(False)
        else :
            self.matcherConfig1.append(self.arrayMatcherConfig1[5])
        if (self.arrayMatcherConfig1[6] == None) :
            # display automatically recognized boundaries:
            self.matcherConfig1.append(True)
        else :
            self.matcherConfig1.append(self.arrayMatcherConfig1[6])
        if (self.arrayMatcherConfig1[7] == None) :
            # Match only phonemes belonging to the same category (consonants, vowels,
            # semiconsonants):
            self.matcherConfig1.append(True)
        else :
            self.matcherConfig1.append(self.arrayMatcherConfig1[7])

        return self.matcherConfig1