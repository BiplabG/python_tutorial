"""Problem 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
Shipping costs $3 for the first copy and 75 cents for each additional copy. 
What is the total wholesale cost for 60 copies?"""

cover_price = 24.95
discount = 0.4
shipping_cost_first = 3
shipping_cost_additional = 0.75

wholesale_cost = (cover_price * (1-discount) * 60) + shipping_cost_first + (shipping_cost_additional * 59)
print("Total Wholesale cost:", wholesale_cost)
