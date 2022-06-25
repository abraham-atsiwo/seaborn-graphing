import pandas as pd

file_extensions = ['csv']
func = [pd.read_csv]

file_extensions_func = {file_extensions[j]:func[j] for j in range(len(func))}
