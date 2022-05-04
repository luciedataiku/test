# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
import pandas as pd, numpy as np
import socket

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
ecommerce_transactions = dataiku.Dataset("ecommerce_transactions__1_")
df = ecommerce_transactions.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# DNS lookup to retrieve IP addresses of merchant URLs
df_merchants = pd.DataFrame(data = {"MerchantURL" : df["MerchantURL"].unique()})

df_merchants["MerchantIP"] = df_merchants["MerchantURL"].apply(socket.gethostbyname)

df = df.merge(df_merchants, on=["MerchantURL"])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
ecommerce_transactions_with_ip = dataiku.Dataset("ecommerce_transactions_with_ip")
ecommerce_transactions_with_ip.write_with_schema(df)
