import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import mean_squared_error
from math import sqrt



def train(data, y):
    model = LinearRegression().fit(data, y)
    return model


def get_fitness(x, y, n_splits=None, random_state=42):
    if n_splits and n_splits > 1:  # run K-Fold cross validation
        predictions_lst = []
        kf = KFold(n_splits=n_splits)
        for train_index, test_index in kf.split(x):
            x_train, x_test = x[train_index], x[test_index]
            y_train, y_test = y[train_index], y[test_index]
            model = train(x_train, y_train)
            predictions = model.predict(x_test)
            predictions_lst.append(mean_squared_error(predictions, y_test))
        return np.mean(predictions_lst) 

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=random_state)
    model = train(x_train, y_train)
    predictions = model.predict(x_test)
    return mean_squared_error(predictions, y_test)


def get_columns(x, bitstring):
    # Function to filter data based on a bitstring
    indexes = []
    for i, s in enumerate(bitstring):
        if s == '0':
            indexes.append(i)
    arr = np.asarray(x)
    arr = np.delete(arr, indexes, axis=1)
    return arr
