# %%
# import pandas, numpy, statsmodels, and matplotlib
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# import sklearn regression modules
from sklearn.linear_model import LinearRegression

# import a datatset of diamonds from statsmeodels rdatasets
diamonds = sm.datasets.get_rdataset("diamonds", "ggplot2").data


# %%
print(diamonds)
