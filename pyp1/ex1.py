# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
arr = []
for i in range(20):
    arr.append(i + 1)
print(arr)


# %%
subArr1 = arr[:len(arr)//2]
subArr2 = arr[len(arr)//2:]
print(subArr1)
print(subArr2)


# %%
n = int(input("Enter n = "))
if (n < 0 or n > len(arr)//2):
    print("Invalid n")
else:
    subArr = arr[n : len(arr) - n]
    print(subArr)


# %%
n = int(input("Enter n = "))
newArr = arr[:n] + arr[len(arr) - n:]
print(newArr)


# %%
n = int(input("Enter n = "))
print(arr[n])


# %%
n = int(input("Enter n = "))
try:
    print(arr[n])
except Exception as message:   
    print(message)


# %%



