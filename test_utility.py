import pytest
import pandas as pd
import numpy as np
from prediction_demo import data_preparation, data_split, train_model, eval_model
from utility import data_split  # ✅ Assumes utility.py is in the same folder

@pytest.fixture
def housing_data_sample():
    return pd.DataFrame(
        data={
            'price': [13300000, 12250000],
            'area': [7420, 8960],
            'bedrooms': [4, 4],
            'bathrooms': [2, 4],
            'stories': [3, 4],
            'mainroad': ["yes", "yes"],
            'guestroom': ["no", "no"],
            'basement': ["no", "no"],
            'hotwaterheating': ["no", "no"],
            'airconditioning': ["yes", "yes"],
            'parking': [2, 3],
            'prefarea': ["yes", "no"],
            'furnishingstatus': ["furnished", "unfurnished"]
        }
    )

def test_data_preparation(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)

    # Target and datapoints have same length
    assert feature_df.shape[0] == len(target_series)

    # Feature only has numerical values
    assert feature_df.shape[1] == feature_df.select_dtypes(include=(np.number, np.bool_)).shape[1]

@pytest.fixture
def feature_target_sample(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    return (feature_df, target_series)

def test_data_split(housing_data_sample):
    df = housing_data_sample

    X_train, X_test, y_train, y_test = data_split(df)

    assert len(X_train) == 1
    assert len(X_test) == 1
    assert len(y_train) == 1
    assert len(y_test) == 1

    expected_features = [
        'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad',
        'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
        'parking', 'prefarea', 'furnishingstatus'
    ]
    assert all(col in X_train.columns for col in expected_features)