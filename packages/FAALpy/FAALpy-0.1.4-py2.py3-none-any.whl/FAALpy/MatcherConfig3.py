import os

class MatcherConfig3 :
    arrayMatcherConfig3 = [None] * (3)
    matcherConfig3 =  []
    # *
    # 	 * Stores the path of the file <i>phon_features.txt</i>.
    # 	 * 
    # 	 * @param pathPhonologicalFeatures (String).
    # 	 * <p>
    # 	 * <p>
    # 	 * Default: "config/phon_features.txt"
    def pathPhonologicalFeatures(self, pathPhonologicalFeatures) :
        self.arrayMatcherConfig3[0] = pathPhonologicalFeatures
    # *
    # 	 * Stores the path of the file <i>phon_categories.txt</i>.
    # 	 * 
    # 	 * @param pathPhoneClass (String).
    # 	 * <p>
    # 	 * <p>
    # 	 * Default: "config/phon_categories.txt"
    def pathPhoneClass(self, pathPhoneClass) :
        self.arrayMatcherConfig3[1] = pathPhoneClass
    # *
    # 	 * Stores the path of the file <i>phon_diacritics.txt</i>.
    # 	 * 
    # 	 * @param pathPhoneClass (String).
    # 	 * <p>
    # 	 * <p>
    # 	 * Default: "config/phon_diacritics.txt"
    def pathPhoneticDiacritics(self, pathPhoneticDiacritics) :
        self.arrayMatcherConfig3[2] = pathPhoneticDiacritics
    # *
    # 	 * Returns the a list with the parameters for the matcherConfig3 parameters.
    def  getmatcherConfig3(self) :
        if (self.arrayMatcherConfig3[0] == None) :
            # location of the config file with list of phonological features
            self.matcherConfig3.append(os.path.join(os.path.dirname(__file__), "config/phon_features.txt"))
        else :
            self.matcherConfig3.append(self.arrayMatcherConfig3[0])
        if (self.arrayMatcherConfig3[1] == None) :
            # location of the config file with phonological categories - only the first category is relevant
            self.matcherConfig3.append(os.path.join(os.path.dirname(__file__), "config/phon_categories.txt"))
        else :
            self.matcherConfig3.append(self.arrayMatcherConfig3[1])
        if (self.arrayMatcherConfig3[2] == None) :
            # location of the file with the diacritics;
            self.matcherConfig3.append(os.path.join(os.path.dirname(__file__), "config/phon_diacritics.txt"))
        else :
            self.matcherConfig3.append(self.arrayMatcherConfig3[2])
        return self.matcherConfig3