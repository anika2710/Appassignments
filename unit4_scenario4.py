import numpy as np
import pandas as pd

prices = np.array([250, 450, 600, 750, 900])

average_price = np.mean(prices)

books = pd.DataFrame({
    'Book Price (₹)': prices
})

print("Book Prices:")
print(books)

print("\nAverage Book Price:", average_price)

print("\nBooks costing more than ₹500:")
print(books[books['Book Price (₹)'] > 500])
