class ParsedWord :
    # *
    # 	 * Stores the parsed word 1.
    # 	 *
    # 	 * @param word1
    # 	 *            (String): parsed word 1.
    #def parsedWord1(word1) :
    def __init__(self):
        self.parsedWord1_var = ""
    # *
    # 	 * Stores the parsed word 2.
    # 	 *
    # 	 * @param word2
    # 	 *            (String): parsed word 2.

        self.parsedWord2_var = ""
    # *
    # 	 * Stores matrix with the numbers of features in common, modified according to
    # 	 * the saliences.
    # 	 *
    # 	 * @param matrixResultComparisonWithSaliences
    # 	 *            (int[][]): matrix with the numbers of features in common, modified
    # 	 *            according to the saliences.
        self.matrixResultComparison_WithSaliences_var = [[]]
    # *
    # 	 * Stores matrix with the numbers of features in common, without modifications.
    # 	 *
    # 	 * @param matrixResultComparisonWithoutSaliences
    # 	 *            (int[][]): matrix with the numbers of features in common, without
    # 	 *            modifications.
        self.matrixResultComparison_WithoutSaliences_var = [[]]
    # =====

    def parsedWord1(self, word1):
        self.parsedWord1_var = word1

    def parsedWord2(self, word2):
        self.parsedWord2_var = word2

    def matrixResultComparison_WithSaliences(self, matrix_saliences):
        self.matrixResultComparison_WithSaliences_var = matrix_saliences

    def matrixResultComparison_WithoutSaliences(self, matrix_withoutSaliences):
        self.matrixResultComparison_WithoutSaliences_var = matrix_withoutSaliences

    def getParsedWord1(self):
        return self.parsedWord1_var

    def getParsedWord2(self):
        return self.parsedWord2_var

    def getMatrixResultComparison_WithSaliences(self):
        return self.matrixResultComparison_WithSaliences_var

    def getMatrixResultComparison_WithoutSaliences(self):
        return self.matrixResultComparison_WithoutSaliences_var

