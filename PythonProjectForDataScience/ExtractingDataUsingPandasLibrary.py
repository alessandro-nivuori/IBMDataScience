import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
read_html_pandas_data = pd.read_html(url)
netflix_dataframe = read_html_pandas_data[0]
print(netflix_dataframe.head())