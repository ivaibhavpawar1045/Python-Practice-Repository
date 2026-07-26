"""
Problem:   Already given a monthly_orders=[] , so perform following actions:

          1) Print total orders.
          2) Print average monthly orders.
          3) Print highest orders.
          4) Print lowest orders.
          5) Add July orders (1950).
          6) Print the updated list.
          7) Print only the first three months.
          8) Print only the last three months.

Sample Input : Pre-defined

Platform: ChatGPT

Difficulty: Easy 

"""

monthly_orders = [
    1200,
    1450,
    1320,
    1680,
    1740,
    1820
]

print("Total Orders : " , sum(monthly_orders))

print("Average Monthly Orders : " , sum(monthly_orders)/len(monthly_orders))

highest_orders = max(monthly_orders)
print("Highest Orders :", highest_orders)

print("Lowest Orders : ", min(monthly_orders))

monthly_orders.append(1950)
print("Updated Monthly Orders :", monthly_orders)

print("First three months : " , monthly_orders[:3])

print("Last three months : " , monthly_orders[-3:])