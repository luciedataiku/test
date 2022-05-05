# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

from to_xlsx import dataframe_to_xlsx

# Read recipe inputs
ecommerce_transactions_with_ip_prepared = dataiku.Dataset("ecommerce_transactions_with_ip_prepared")
ecommerce_transactions_with_ip_prepared_df = ecommerce_transactions_with_ip_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_df = ecommerce_transactions_with_ip_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
test = dataiku.Dataset("test")


