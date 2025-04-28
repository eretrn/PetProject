import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import seaborn as sns
import matplotlib.pyplot as plt
import ast
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

from sklearn.ensemble import GradientBoostingRegressor

pd.set_option('display.max_columns', None)
# Входные данные
sample_submit = pd.read_csv("sample_submit.csv")
train = pd.read_excel("train.xlsx")
test = pd.read_excel("test.xlsx")
# Предмет
train = pd.get_dummies(train, columns=['предмет'])
# Experience
train['experience'] = train['experience'].str.replace(r"[^\d\.]", "", regex=True)
train['experience'] = train['experience'].astype('float64')
# Categories
train['categories'] = train['categories'].apply(lambda s: list(ast.literal_eval(s)))
mlb = MultiLabelBinarizer()
genres_encoded = mlb.fit_transform(train['categories'])
genres_df = pd.DataFrame(genres_encoded, columns=mlb.classes_)
train = pd.concat([train, genres_df], axis=1)
del train['categories']
#Tags
train['tutor_head_tags'] = train['tutor_head_tags'].apply(lambda s: list(ast.literal_eval(s)))
mlb = MultiLabelBinarizer()
head_tags_encoded = mlb.fit_transform(train['tutor_head_tags'])
head_tags_df = pd.DataFrame(head_tags_encoded, columns = mlb.classes_)
train = pd.concat([train, head_tags_df], axis=1)
del train['tutor_head_tags']

# Расчёт
numeric_cols = train.select_dtypes(include='number').columns
train = train[numeric_cols]
train['experience'] = train['experience'].fillna(0)
train['tutor_rating'] = train['tutor_rating'].fillna(0)
train.drop(columns=['Unnamed: 0'], inplace=True)

# sns.set(rc = {'figure.figsize':(40,40)})
# sns.heatmap(train.corr(), annot = True, cmap="YlGnBu", linecolor='white',linewidths=1)
# plt.show()

X = train.drop(columns=['mean_price'])
Y = train['mean_price']
GBR = GradientBoostingRegressor()
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
# scores = cross_val_score(GBR, X, Y, cv=5, scoring='neg_mean_squared_error')
GBR.fit(X_train, y_train)
y_pred = GBR.predict(X_test)
# print(scores)
print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('R2 score:', r2_score(y_test, y_pred))