
import pandas as pd
import sqlite3

# Cargar dataset final
df = pd.read_csv("telco_dataset_final.csv")

# Conexión a la base SQLite
conn = sqlite3.connect("telco_churn.db")
df.to_sql("telco_customer", conn, if_exists="replace", index=False)

print("Base de datos creada con éxito.")
