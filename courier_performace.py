import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",   # your MySQL password
    database="amazon_supply_chain"
)

# 2️⃣ SQL query: average delay per courier
query = """
SELECT 
    courier_partner,
    AVG(DATEDIFF(delivery_date, order_date)) AS avg_delay_days
FROM orders_data
GROUP BY courier_partner
ORDER BY avg_delay_days;
"""

# 3️⃣ Read into DataFrame
df_courier = pd.read_sql(query, conn)

conn.close()

print(df_courier)

# 4️⃣ Plot
plt.figure(figsize=(10, 4))
plt.bar(df_courier["courier_partner"], df_courier["avg_delay_days"])
plt.xticks(rotation=45)
plt.xlabel("Courier Partner")
plt.ylabel("Average Delay (days)")
plt.title("Courier Performance")
plt.tight_layout()

# 5️⃣ Save as PNG
plt.savefig("courier_performance.png", dpi=300, bbox_inches="tight")

# 6️⃣ Show
plt.show()
