import pandas as pd
tables = pd.read_html("https://ko.wikipedia.org/wiki/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
len(tables)