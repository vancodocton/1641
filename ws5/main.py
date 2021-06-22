# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# import lib
import pandas
import numpy


# %%
# read input file
input_file = './Gold_price.xlsx'
df = pandas.read_excel(input_file)
df.info()


# %%
# rename columns
df.rename(columns={'Price (USD)' : 'price', 'Date' : 'date'}, inplace=True)
df.info()
df.head()


# %%
# calculate average forecast
step = 5
df['average_forecast'] = [0 for i in range(step)] +     [numpy.average(df['price'].loc[i - step : i - 1])         for i in df.index[step:]]
# calculate average forecast loss
df['average_loss'] = df['price'] - df['average_forecast']
df.tail()


# %%
df.loc[0:10]


# %%
def deviations(arr):
    mean = numpy.mean(arr)
    return numpy.array([x - mean for x in arr])

def linear(x, known_ys, known_xs):
    if (len(known_ys) != len(known_xs)): 
        return numpy.nan
    
    x_deviations = deviations(known_xs)
    y_deviations = deviations(known_ys)

    b = sum(x_deviations * y_deviations) / sum(x_deviations * x_deviations)
    
    a = numpy.mean(known_ys) - b * numpy.mean(known_xs)

    return a + b * x


# %%
step = 17

df['linear_forecast'] = [0 for i in range(step)] +     [linear(i + step,         df['price'].loc[i: i + step - 1].to_numpy(),             df.index[i:i+step].to_numpy()) for i in range(len(df.index) - step)]
df['linear_loss'] = df['price'] - df['linear_forecast']

df.tail()


# %%
# export line plot for average forecast 
df.plot(x='date', y=['price','average_forecast','average_loss'],     kind='line', xlabel ='DateTime',ylabel='Gold Price',         title='Moving Average', figsize=(30,10))


# %%
df.plot(x='date', y=['price','linear_forecast','linear_loss'],     kind='line', xlabel ='DateTime',ylabel='Gold Price',         title='Moving Average', figsize=(30,10))


# %%
# compare the loss of two methods
print('average_loss')
print('\tMAX     \t', df['average_loss'].max())
print('\tMIN     \t', df['average_loss'].min())
print('\tAVERAGE \t', df['average_loss'].mean())

print('linear_loss')
print('\tMAX      \t', df['linear_loss'].max())
print('\tMIN      \t', df['linear_loss'].min())
print('\tAVERAGE  \t', df['linear_loss'].mean())


