import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import mean_squared_error, mean_absolute_error
from math import sqrt



def train_lin_reg(data, y):
    model = LinearRegression().fit(data, y)
    return model


def train_log_reg(data, y):
    model = LogisticRegression(max_iter=10000).fit(data, y)
    return model


def get_fitness_lin_reg(x, y, n_splits=None, random_state=42, include_mae=False):
    if n_splits and n_splits > 1:  # run K-Fold cross validation
        predictions_mse_lst = []
        predictions_mae_lst = []
        kf = KFold(n_splits=n_splits)
        for train_index, test_index in kf.split(x):
            x_train, x_test = x[train_index], x[test_index]
            y_train, y_test = y[train_index], y[test_index]
            model = train_lin_reg(x_train, y_train)
            predictions = model.predict(x_test)
            predictions_mse_lst.append(mean_squared_error(predictions, y_test))
            if include_mae:
                predictions_mae_lst.append(mean_absolute_error(predictions, y_test))
        return (np.mean(predictions_mse_lst), np.mean(predictions_mae_lst)) if include_mae else np.mean(predictions_mse_lst)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=random_state)
    model = train_lin_reg(x_train, y_train)
    predictions = model.predict(x_test)
    return (mean_squared_error(predictions, y_test), mean_absolute_error(predictions, y_test)) if include_mae else mean_squared_error(predictions, y_test)


def get_fitness_log_reg(x, y, n_splits=None, random_state=42):
    if n_splits and n_splits > 1:  # run K-Fold cross validation
        score_lst = []
        kf = KFold(n_splits=n_splits)
        for train_index, test_index in kf.split(x):
            x_train, x_test = x[train_index], x[test_index]
            y_train, y_test = y[train_index], y[test_index]
            model = train_log_reg(x_train, y_train)
            score_lst.append(model.score(x_test, y_test))
        return np.mean(score_lst)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=random_state)
    model = train_log_reg(x_train, y_train)
    return model.score(x_test, y_test)


def get_columns(x, bitstring):
    # Function to filter data based on a bitstring
    indexes = []
    for i, s in enumerate(bitstring):
        if s == '0':
            indexes.append(i)
    arr = np.asarray(x)
    arr = np.delete(arr, indexes, axis=1)
    return arr
