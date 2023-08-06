class MatcherConfig4 :
    arrayMatcherConfig4 = [None] * (1)
    matcherConfig4 =  []
    # *
    # 	 * Set the factor A (see article) to be used in the default Corrected Global Similarity Score.
    # 	 * 
    # 	 * @param factorA (Double).
    # 	 * <p>
    # 	 * <p>
    # 	 * Default: 7.71
    def factorA(self, factorA) :
        self.arrayMatcherConfig4[0] = factorA
    # *
    # 	 * Returns the a list with the parameters for the matcherConfig4 parameters.
    def  getmatcherConfig4(self) :
        if (self.arrayMatcherConfig4[0] == None) :
            # Set the factor A (see article) to be used in the default Corrected Global Similarity Score:
            self.matcherConfig4.append(7.71)
        else :
            self.matcherConfig4.append(self.arrayMatcherConfig4[0])
        return self.matcherConfig4