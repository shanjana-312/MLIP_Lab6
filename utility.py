from sklearn.model_selection import train_test_split

def data_split(data, test_size=0.2, random_state=42):
    X = data.drop(columns=['price'])  # ⬅️ fixed target column
    y = data['price']

    from sklearn.model_selection import train_test_split
    return train_test_split(X, y, test_size=test_size, random_state=random_state)