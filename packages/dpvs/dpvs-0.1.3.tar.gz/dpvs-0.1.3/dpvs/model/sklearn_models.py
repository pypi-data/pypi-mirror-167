from dpvs.logging import get_logger
from dpvs.utils import pickle_load
from sklearn.svm import SVC 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from xgboost import XGBClassifier

log = get_logger()


MODEL = {
    "svm": SVC(),
    "lda": LDA(),
    "rf":  RandomForestClassifier(),
    "gb":  GradientBoostingClassifier(),
    "knn": KNeighborsClassifier(),
    "adb": AdaBoostClassifier(),
    "log": LogisticRegression(),
    "dt": DecisionTreeClassifier(),
    "xgb": XGBClassifier()
}

def make_model(name, load_best, checkpoint):
    if load_best and checkpoint:
        try:
            log.info(f'Checkpoint set to {checkpoint}')
            return pickle_load(checkpoint)
        except OSError: pass # start training from scratch
    return MODEL.get(name)
    