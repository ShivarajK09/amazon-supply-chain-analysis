import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",                         # your working password
    database="amazon_supply_chain"
)

print("Connected to database!")

# 2. Example query: total rows in orders
df = pd.read_sql("SELECT COUNT(*) AS total FROM orders_data", conn)
print(df)

conn.close()

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="amazon_supply_chain"
)

# ---------- 1. City-wise delivery delay ----------
query_city_delay = """
SELECT city,
       COUNT(*) AS total_orders,
       AVG(DATEDIFF(delivery_date, order_date)) AS avg_delay_days
FROM orders_data
GROUP BY city
ORDER BY avg_delay_days DESC
LIMIT 20;
"""

df_city = pd.read_sql(query_city_delay, conn)
print("\nCity-wise delay:")
print(df_city)

# Plot
plt.figure(figsize=(12,6))
plt.bar(df_city["city"], df_city["avg_delay_days"])
plt.xticks(rotation=90)
plt.xlabel("City")
plt.ylabel("Average Delay (days)")
plt.title("Average Delivery Delay by City")
plt.tight_layout()
plt.show()

conn.close()

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="amazon_supply_chain"
)

# ---------- 1. City-wise delivery delay ----------
query_city_delay = """
SELECT city,
       COUNT(*) AS total_orders,
       AVG(DATEDIFF(delivery_date, order_date)) AS avg_delay_days
FROM orders_data
GROUP BY city
ORDER BY avg_delay_days DESC
LIMIT 20;
"""

df_city = pd.read_sql(query_city_delay, conn)
print("\nCity-wise delay:")
print(df_city)

# Plot
plt.figure(figsize=(12,6))
plt.bar(df_city["city"], df_city["avg_delay_days"])
plt.xticks(rotation=90)
plt.xlabel("City")
plt.ylabel("Average Delay (days)")
plt.title("Average Delivery Delay by City")
plt.tight_layout()
plt.show()

conn.close()

# ---------- 2. Courier performance ----------
query_courier = """
SELECT courier_partner,
       COUNT(*) AS total_orders,
       AVG(DATEDIFF(delivery_date, order_date)) AS avg_delay_days
FROM orders_data
GROUP BY courier_partner
ORDER BY avg_delay_days;
"""

df_courier = pd.read_sql(query_courier, conn)
print("\nCourier performance:")
print(df_courier)

plt.figure(figsize=(10,5))
plt.bar(df_courier["courier_partner"], df_courier["avg_delay_days"])
plt.xticks(rotation=45)
plt.xlabel("Courier Partner")
plt.ylabel("Average Delay (days)")
plt.title("Courier Performance")
plt.tight_layout()
plt.show()

# ---------- 3. Ratings vs delay ----------
query_rating_delay = """
SELECT 
    r.rating,
    COUNT(*) AS total_reviews,
    AVG(DATEDIFF(o.delivery_date, o.order_date)) AS avg_delay_days
FROM customer_reviews r
JOIN orders_data o
  ON r.order_id = o.order_id
GROUP BY r.rating
ORDER BY r.rating;
"""

df_rating = pd.read_sql(query_rating_delay, conn)
print("\nRating vs delay:")
print(df_rating)

plt.figure(figsize=(8,5))
plt.plot(df_rating["rating"], df_rating["avg_delay_days"], marker='o')
plt.xlabel("Rating")
plt.ylabel("Average Delay (days)")
plt.title("Delivery Delay vs Rating")
plt.grid(True)
plt.tight_layout()
plt.show()


