import pandas as pd
country = pd.read_csv("C:\Users\Administrator\Desktop\Nz.csv",index_col=0)
country.to_html('edu.html')