class MatcherConfig2 :
    arrayMatcherConfig2 = [None] * (5)
    matcherConfig2 =  []
    # *
    # 	 * Select the Similarity Score to be used.
    # 	 * 
    # 	 * @param similarityScore (Integer):
    # 	 * 							0 = use globalSimilaryScore <p>
    # 	 * 							1 = use correctedGlobalSimilaryScore <p><p>
    # 	 * 							if morphemic boundaries are present, better 0 ; if no morphemic boundary is present, better 1.
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: 0
    def similarityScore(self, similarityScore) :
        self.arrayMatcherConfig2[0] = similarityScore
    # *
    # 	 * Set limit of features in common for consonants under which the features are not significant and not counted any more.
    # 	 * 
    # 	 * @param limitFeaturesCons (Integer)
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: 23
    def limitFeaturesConsonants(self, limitFeaturesCons) :
        self.arrayMatcherConfig2[1] = limitFeaturesCons
    # *
    # 	 * Set limit of features in common for vowels under which the features are not significant and not counted any more.
    # 	 * 
    # 	 * @param limitFeaturesVows (Integer)
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: 0
    def limitFeaturesVowels(self, limitFeaturesVows) :
        self.arrayMatcherConfig2[2] = limitFeaturesVows
    # *
    # 	 * Set number of trials when morphemic boundaries are present.
    # 	 * 
    # 	 * @param trialsWithMorphBound (Integer)
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: 6
    def trialsWithMorphemicBoundaries(self, trialsWithMorphBound) :
        self.arrayMatcherConfig2[3] = trialsWithMorphBound
    # *
    # 	 * Set number of trials when morphemic boundaries are not present.
    # 	 * 
    # 	 * @param trialsWithoutMorphBound (Integer)
    # 	 *            <p>
    # 	 *            <p>
    # 	 *            Default: 6
    def trialsWithoutMorphemicBoundaries(self, trialsWithoutMorphBound) :
        self.arrayMatcherConfig2[4] = trialsWithoutMorphBound
    # *
    # 	 * Returns the a list with the parameters for the matcherConfig2 parameters.
    def  getmatcherConfig2(self) :
        if (self.arrayMatcherConfig2[0] == None) :
            # Select the Similarity Score to be used: 0 = use
            # globalSimilaryScore, 1 = use correctedGlobalSimilaryScore (-> if morphemic
            # boundaries are present, better 0 ; if no morphemic boundary is present,
            # better 1)
            self.matcherConfig2.append(0)
        else :
            self.matcherConfig2.append(self.arrayMatcherConfig2[0])
        if (self.arrayMatcherConfig2[1] == None) :
            # Set limit of features in common for cons under which the features are not
            # significant and not counted any more
            self.matcherConfig2.append(23)
        else :
            self.matcherConfig2.append(self.arrayMatcherConfig2[1])
        if (self.arrayMatcherConfig2[2] == None) :
            # Set limit of features in common for vowels under which the features are not
            # significant and not counted any more
            self.matcherConfig2.append(0)
        else :
            self.matcherConfig2.append(self.arrayMatcherConfig2[2])
        if (self.arrayMatcherConfig2[3] == None) :
            # nr of trials with morphemic boundaries
            self.matcherConfig2.append(6)
        else :
            self.matcherConfig2.append(self.arrayMatcherConfig2[3])
        if (self.arrayMatcherConfig2[4] == None) :
            # nr of trials without morphemic boundary
            self.matcherConfig2.append(6)
        else :
            self.matcherConfig2.append(self.arrayMatcherConfig2[4])
        return self.matcherConfig2