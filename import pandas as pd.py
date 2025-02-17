import pandas as pd
df = pd.read_excel("C:\\Users\\bleed\\OneDrive\\Bureau\\Mme KANE.xlsx")
#print(df)
dff = pd.read_csv("C:\\Users\\bleed\\OneDrive\\Bureau\\annual-survey-2023-csv.csv", header = None)
#print(dff.head())
#print(dff.tail())
#print(dff.dtypes)
#print(dff.describe(include="all"))
#print(dff.info())
#print(dff["Value"])
#df["Value"]+1
data = pd.read_excel("C:\\Users\\bleed\\OneDrive\\Bureau\\F-Somapep.xlsx")
#print(data["N° ORDRE"])
#print(data.dropna())
data.dropna(subset=["DESIGNATION"], axis=0, inplace=True)
#print(data["N° ORDRE"].replace("A", "23"))
#print(data.rename(columns={"N° ORDRE": "CLASSEMENT"}))
#print(data["N° ORDRE"].tail())
#print(data["N° ORDRE"].astype("int"))
#print(data["N° ORDRE"]/data["N° ORDRE"].max())     ->->->-> #SIMPLE FEATURE SCALING                                     
#print(data["N° ORDRE"]-data["N° ORDRE"].min()/data["N° ORDRE"].max()-data["N° ORDRE"].min()) ->-> #MIN-MAX METHOD
#print((data["N° ORDRE"]-data["N° ORDRE"].mean())/data["N° ORDRE"].std())   ->->->  #Z-SCORE

#                          ##BINNING (*Divides Continuous Variables into Discrete Intervals/Bins)
import numpy as np
#print(np.linspace(min(data["N° ORDRE"]), max(data["N° ORDRE"]),4))  
#bins=np.linspace(min(data["N° ORDRE"]), max(data["N° ORDRE"]),4)
#name = ["A","B","C"]
#print(pd.cut(data["N° ORDRE"], bins, labels=name, include_lowest=True)) ->-> #BINS SEGMENTATION / GROUPING
#print(pd.get_dummies(data["DESIGNATION"]))                ->->-> #CATEGORICAL -> QUANTITATIVE VARIABLE
#                                      ##DESCRIPTIVE STATISTIQUES
#print(data.describe())                               
#print(data["DESIGNATION"].value_counts().to_frame())
import matplotlib as plt
x=data["DESIGNATION"]
y=data["N° ORDRE"]
print(plt.scater(x,y))