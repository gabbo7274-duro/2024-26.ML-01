import pandas as pd
import os
from sklearn.model_selection import train_test_split, RandomizedSearchCV, KFold
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, make_scorer, r2_score, mean_squared_error
from joblib import dump
import os
import joblib




df = pd.read_csv('Salary Data.csv')
df[df.isnull().any(axis=1)]
df.dropna(inplace=True)
from sklearn.model_selection import train_test_split
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
from sklearn.linear_model import LinearRegression
X_train = df_train[["Years of Experience"]]
y_train = df_train["Salary"]

X_test = df_test[["Years of Experience"]]
y_test = df_test["Salary"]
linreg = LinearRegression()
linregfit = linreg.fit(X_train, y_train)
linreg.get_params()
linreg.set_params(positive=True)
y_test_pred = linreg.predict(X_test)
y_test_pred

os.makedirs('treminio', exist_ok=True)
dump(linreg, 'treminio/artifact.joblib')
print("Model saved to treminio/artifact.joblib")
print("sddyt")

joblib.dump(linregfit, 'treminio/grid_search.joblib')
