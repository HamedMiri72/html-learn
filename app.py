print("Hello world")


import pandas as pd
from sqlalchemy import create_engine


xlxs_file = "file.xlsx"
df = pd.read_excel(xlxs_file)

engine = create_engine
df.to.sql("tabke_name", con = engine, if_exists = "replace", index = false)

print("data write in to the data base")




