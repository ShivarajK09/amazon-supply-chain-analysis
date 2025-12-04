import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="amazon_supply_chain"
)
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
