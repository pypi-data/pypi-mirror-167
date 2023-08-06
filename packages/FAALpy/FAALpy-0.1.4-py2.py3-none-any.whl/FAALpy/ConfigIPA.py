
from pathlib import Path
import os


class ConfigIPA :

    def __init__(self):
        self.configIPA = [Path(os.path.join(os.path.dirname(__file__), "config/phon_features.txt")),
                          Path(os.path.join(os.path.dirname(__file__), "config/phon_diacritics.txt")),
                          Path(os.path.join(os.path.dirname(__file__), "config/features_diphthongs.txt")),
                          Path(os.path.join(os.path.dirname(__file__), "config/features_coarticulation.txt")),
                          Path(os.path.join(os.path.dirname(__file__), "config/phon_categories.txt")),
                          Path(os.path.join(os.path.dirname(__file__), "config/saliences_to_use_matches_phon_categories.txt"))]
    # *
    # 	 * Stores the path of the file <i>phon_features.txt</i>.
    # 	 *
    # 	 * @param pathPhonologicalFeatures (String).
    # 	 * <p>
    # 	 * <p>
    # 	 * Default: "config/phon_features.txt"

    def pathPhonologicalFeatures(self, path):
        self.configIPA[0] = Path(path)
    # *
    # 	 * Stores the path of the file <i>phon_diacritics.txt</i>.
    # 	 *
    # 	 * @param pathPhoneticDiacritics (String).
    # 	 * <p>
    # 	 * <p>
    # 	 * Default: "config/phon_diacritics.txt"
    def pathPhoneticDiacritics(self, path):
        self.configIPA[1] = Path(path)

    # *
    # 	 * Stores the path of the file <i>features_diphthongs.txt</i>.
    # 	 *
    # 	 * @param pathFeaturesDiphthongs (String).
    # 	 * <p>
    # 	 * <p>
    # 	 * Default: "config/features_diphthongs.txt"
    def pathFeaturesDiphthongs(self, path):
        self.configIPA[2] = Path(path)
    # *
    # 	 * Stores the path of the file <i>features_coarticulation.txt</i>.
    # 	 *
    # 	 * @param pathFeaturesCoarticulation (String).
    # 	 * <p>
    # 	 * <p>
    # 	 * Default: "config/features_coarticulation.txt"
    def pathFeaturesCoarticulation(self, path):
        self.configIPA[3] = Path(path)
    # *
    # 	 * Stores the path of the file <i>phon_categories.txt</i>.
    # 	 *
    # 	 * @param pathPhoneClass (String).
    # 	 * <p>
    # 	 * <p>
    # 	 * Default: "config/phon_categories.txt"
    def pathPhonCategories(self, path):
        self.configIPA[4] = Path(path)
    # *
    # 	 * Stores the path of the file <i>saliences_to_use_matches_phon_categories.txt</i>.
    # 	 *
    # 	 * @param pathPhoneClass (String).
    # 	 * <p>
    # 	 * <p>
    # 	 * Default: "config/saliences_to_use_matches_phon_categories.txt"
    def saliencesMatchesPhonCategories(self, path):
        self.configIPA[5] = Path(path)
    # *
    def getConfigIPA(self):
        return self.configIPA