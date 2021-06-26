# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
A = [[1, 2, 3], 
    [4, 5, 6], 
    [7, 8 ,9]]


# %%
diag = []
for i in [0, 1, 2]:
    diag.append(A[i][i])

print(diag)


# %%
diagLC = [A[i][i] for i in range(0,3)]
print(diagLC)


# %%
slicedInColums = [A[i][0] for i in range(0,3)]
print(slicedInColums)


# %%
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 1
powerList = []
while True:
    powerList.append(i * i)
    i += 2
    if (i > 10): break
print(powerList)


# %%



