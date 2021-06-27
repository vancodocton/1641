# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# import lib
import numpy
import pandas
from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error


# %%
csv_file = "./TESLA_STOCK_2010_2020.csv"
# Read the excel file to a dataframe
df = pandas.read_csv(csv_file)
# comment:
df.info()


# %%
# view dataframe
df


# %%
df['Date'] = pandas.to_datetime(df['Date'])
df.set_index('Date', inplace=True, verify_integrity=True)


# %%
# check if two columns Close and Adj Close is the same
(df['Close'] == df['Adj Close']).all()


# %%
# drop redudant column Adj Close
df.drop('Adj Close', axis=1, inplace=True)


# %%
df.info()


# %%
df


# %%
# X is data used to predict Y
# X_train , and Y_train is used to training model
# to predict, use X_test data to predict Y (Y_predict), Y_test is the real result

# by using historical price of stock, the tomorrow open price of stock will be predicted

X_col = ['Open', 'High', 'Low', 'Close', 'Volume'] 
# X is historical price
X = df[X_col]
# convert datetime[ns] to timestamp unit'D'
X['Timestamp'] = [x.value / 86400000000000 for x in df.index] # 10**9 * 60 * 60 *24
# pandas.to_datetime(14780, unit='D', origin='unix')
Y = df['Open'].iloc[1:]


# %%
# demo for predict

# step = 15
# model = LinearRegression()

# X_train = X.iloc[0: 15] (0, 1, 2, ..., 14)
# Y_train = Y.iloc[0: 15] (0, 1, 2, ..., 14)

# model.fit(X_train, Y_train)

# X_test = X.iloc[15].to_numpy().reshape(1, -1) (df.i = 15)
# Y_test = Y.iloc[15] = df.iloc[15, ]
# predict_demo = model.predict(X_test)


# %%
def predict_tomorrow_open_price(model, X_train, Y_train, X_test):
    model.fit(X_train, Y_train)
    Y_predict = model.predict(X_test)
    return Y_predict


# %%
step = 15

model = LinearRegression()

Open_Tomorrow_Predict = []

for i in range(step, len(df)):
    i_first = i - step
    X_train = X.iloc[i - step: i]
    Y_train = Y.iloc[i - step: i]
    
    # if (i_last == len(df)):
    #     i_last =- 1

    X_test = X.iloc[i].to_numpy().reshape(1, -1)

    Y_Predict = predict_tomorrow_open_price(        model, X_train, Y_train, X_test)[0]
    Open_Tomorrow_Predict.append(Y_Predict)


# %%
# Open_Predict = [0 for i in range(step + 1)] + Open_Tomorrow_Predict[:-1]
Open_Tomorrow_Predict = [None for i in range(step)] + Open_Tomorrow_Predict
Open_Predict = [None]+ Open_Tomorrow_Predict[:-1]


# %%
# Create new column Open_Tomorrow_Real
df['Open_Tomorrow_Predict'] = Open_Tomorrow_Predict
df['Open_Predict']  = Open_Predict
df['Open_Tomorrow_Real'] = df['Open'].shift(-1)
df['Loss'] = df['Open_Predict'] - df['Open']


# %%
# testing
df['NO'] = [i for i in range(len(df))]
df[:20]


# %%
df[-20:]


# %%
df.drop('NO', axis=1, inplace=True)


# %%
df.plot(y=['Open', 'Open_Predict', 'Loss'], figsize=(50,15))
# df.iloc[-200:].plot(y=['Open', 'Open_Predict', 'Loss'], figsize=(50,15))


# %%
evaluate_df = df[{'Open', 'Open_Predict', 'Loss'}].dropna()
evaluate_df.plot(y='Loss', figsize=(50,15))
evaluate_df.plot(y='Loss', kind='hist')


# %%
#cal mean squared error
mse = mean_squared_error(y_true=evaluate_df['Open'], y_pred=evaluate_df['Open_Predict'])
# show resluts
print('Mean Squared Error:          ', mse)
print('Root Mean Squared Error:     ', numpy.sqrt(mse))


# %%
evaluate_df['Loss'].describe()


# %%
df.to_csv('.\predicted.' + csv_file[2:])


