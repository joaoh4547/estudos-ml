import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px


data = pd.read_csv('data/credit_data.csv')

print(data.tail(8))
print()
print(data.describe())
