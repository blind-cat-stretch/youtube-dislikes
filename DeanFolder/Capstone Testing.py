# import pandas as pd
# import numpy as np
# import pickle
# import os
# from pathlib import Path
# import joblib
# from time import perf_counter

# filepath = 'rfclf.joblib.pkl'

# try:
#     with open(filepath, 'rb') as file:
#         data = pickle.load(file)
#         print('try worked')
# except:
#     print('except')
#     pass

# obj = pd.read_pickle('rfclf.joblib.pkl')
# obj

# clf = joblib.load('rfclf.joblib.pkl')

import pandas as pd
import numpy as np
import pickle
import os
from pathlib import Path
import joblib
from time import perf_counter

# For local testing
X_cols = [
    "duration",
    "age_limit",
    "view_count",
    "like_count",
    "view_like_ratio_smoothed",
    "is_comments_enabled",
    "is_live_content",
    "cat_codes",
    "desc_neu",
    "desc_neg",
    "desc_pos",
    "desc_compound",
    "comment_neu",
    "comment_neg",
    "comment_pos",
    "comment_compound",
    "votes",
    "NoCommentsBinary"
]

# Some paths for testing the function on local data.
# ROOT_DIR = os.path.abspath(os.curdir)

# Path to load the model
# The model with no compression takes 1.5 seconds to load and is 945MB in size
# The model with 3 compression takes 3.6 seconds to load and is 188MB in size
# We are using the no compression for inference time but due to size limitations, we have the compressed version for github.

# model_pickle_path = os.path.join(ROOT_DIR,"models/rfclf.joblib.pkl")
# model_pickle_path = os.path.join(ROOT_DIR,"models/rfclf_nocompression.joblib.pkl")
model_pickle_path = 'rfclf.joblib.pkl'

# Test pred df
testing_df_pickle_path = 'testing_sample.pkl'
test_pred_df = pd.read_pickle(testing_df_pickle_path).iloc[0].to_frame().T
test_pred_row = test_pred_df[X_cols]
test_pred_actual = test_pred_df["ld_score_ohe"].values

def make_pred(pred_df,clf_path):
    print("Input data is:")
    print(pred_df)
    # print(pred_df.columns)
    print("Loading model...")
    start_load_time = perf_counter()
    rf_clf = joblib.load(clf_path)
    print(f"Time taken to load model: {(perf_counter() - start_load_time) }" )
    print("Making Prediction...")
    pred = rf_clf.predict(pred_df)
    print(f"Prediction is: {pred}")
    return pred

if __name__ == "__main__":
    # print("Testing predict model")
    for i in range(10):
        testing_df_pickle_path = 'testing_sample.pkl'
        test_pred_df = pd.read_pickle(testing_df_pickle_path).iloc[i].to_frame().T
        test_pred_row = test_pred_df[X_cols]
        test_pred_actual = test_pred_df["ld_score_ohe"].values
        print("Testing predict model")
        make_pred(test_pred_row,model_pickle_path)
        print(f"Actual label was {test_pred_actual}")
    # print(f"Actual label was {test_pred_actual}")