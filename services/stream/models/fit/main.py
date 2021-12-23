import pandas as pd
from utils import preprocessor
from catboost import CatBoostClassifier

def fit_model():
    df = pd.read_json('/services/stream/data/train_data.json')
    clean_df = preprocessor.clean_df(df)

    cat_features = list(range(0, clean_df.shape[1]))

    clf = CatBoostClassifier(
        iterations=5, 
        learning_rate=0.1, 
        #loss_function='CrossEntropy'
    )


    clf.fit(X_train, y_train, 
            cat_features=cat_features, 
            eval_set=(clean_df), 
            verbose=False
    )

    clf.save_model('services/stream/models/weights/catboost',
           format="cbm",
           export_parameters=None,
           pool=None)

    return True
    

if __name__ == '__main__':
    fit_model()