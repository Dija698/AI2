import numpy as np

data = np.genfromtxt(
    "RealEstate-USA.csv",
    delimiter=",",
    skip_header=1,
    usecols=(2, 5, 10),
    dtype=float,
    encoding="utf-8",
    missing_values="",
    filling_values=np.nan
)

price = data[:, 0]
acre_lot = data[:, 1]
house_size = data[:, 2]

valid_rows = ~np.isnan(price) & ~np.isnan(acre_lot) & ~np.isnan(house_size)
price = price[valid_rows]
acre_lot = acre_lot[valid_rows]
house_size = house_size[valid_rows]

print("Price:", price[:5])
print("Acre Lot:", acre_lot[:5])
print("House Size:", house_size[:5])

print("Mean: ", np.mean(data))
print("Std: ", np.std(data))
print("Median: ", np.median(data))
print("25th Percentile: ", np.percentile(data, 25))
print("RealEstate-USA  - 75: " , np.percentile(data,75))
print("RealEstate-USA - 3: " , np.percentile(data,3))
print("RealEstate-USA : " , np.min(data))
print("RealEstate-USA : " , np.max(data))

print("\n---- Arithmetic Operations ----")
print("Addition (+):", price + house_size)
print("Subtraction (-):", price - house_size)
print("Multiplication (*):", price * house_size)

print("Addition (np.add):", np.add(price, house_size))
print("Subtraction (np.subtract):", np.subtract(price, house_size))
print("Multiplication (np.multiply):", np.multiply(price, house_size))

two_d_array = np.array([price, house_size])
print("\n---- 2D Array ----")
print(two_d_array)

three_d_array = np.array([house_size, price, acre_lot])
print("\n---- 3D Array ----")
print(three_d_array)

print("\n---- Iteration with np.nditer ----")
for val in np.nditer(price):
    print(val)

print("\n---- Iteration with np.ndenumerate ----")
for idx, val in np.ndenumerate(price):
    print(f"Index: {idx}, Value: {val}")

print("\n---- Array Properties of 'Price' ----")
print("ndim:", price.ndim)
print("shape:", price.shape)
print("size:", price.size)
print("dtype:", price.dtype)
print("itemsize:", price.itemsize)
print("nbytes:", price.nbytes)
print("type:", type(price))
