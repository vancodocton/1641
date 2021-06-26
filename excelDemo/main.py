# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas
import numpy
from matplotlib import pyplot


# %%
excelFileName = './Sample - Superstore.xls'
df = pandas.read_excel(excelFileName)
df.info()


# %%
categorydf = df[['Category','Quantity']].groupby('Category').sum()


# %%
categorydf


# %%
df.loc[df['Category']=='Furniture'] ["Quantity"].sum()


# %%
# Object Oriented plot
categoryList = df['Category'].unique().tolist()
categoryQuantity = df.groupby('Category')['Quantity'].sum().tolist()
fig, ax = pyplot.subplots()
y_pos = numpy.arange(len(categoryList))
ax.barh(y_pos, categoryQuantity)
ax.set_yticks(y_pos)
ax.set_yticklabels(categoryList)
ax.set_ylabel('Category')
ax.set_xlabel('Quantity')
ax.set_title('Quantity base on Category')


# %%
df1 = df[['Category','Quantity']].groupby('Category').sum()


# %%
df2 = df.groupby('Category')['Quantity'].sum()


# %%
df2.tolist()


# %%
df2.keys().tolist()


# %%
def sum_on_attribute(num_col, attrib_col, dataframe):
    df = dataframe.groupby(num_col)[attrib_col].sum()
    return df.keys().tolist(), df.tolist()
cat_list, cat_quan = sum_on_attribute('Category', 'Quantity', df)


# %%
def bar_plot(num_list, attrib_list, xlabel, ylabel, title="", color_list=['r', 'g', 'b', 'g', 'c', 'm']):
    fig, ax = pyplot.subplots()
    y_pos = numpy.arange(len(num_list))
    ax.barh(y_pos, attrib_list)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categoryList)
    ax.set_ylabel(xlabel)
    ax.set_xlabel(ylabel)
    ax.set_title('Quantity base on Category')
bar_plot(cat_list, cat_quan, "", "")


