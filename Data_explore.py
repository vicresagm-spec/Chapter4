import  pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

penguin_df =pd.read_csv('penguins.csv')
print(penguin_df.head())

#Cleaning the data set
penguin_df.dropna(inplace=True)
#f=penguin_df.columns
#print(f)
output = penguin_df['species']
features =penguin_df[['island','bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g', 'sex']]

features =pd.get_dummies(features)

#print(f"Output Variable:{output.head()}")
#print(f"Feature Variable:{features.head()}")

output ,uniques =pd.factorize(output)
X_train ,X_test,y_train,y_test =train_test_split(features,output,test_size=.8)

rfc =RandomForestClassifier(random_state=15)
rfc.fit(X_train,y_train)
y_pred =rfc.predict(X_test)
score =accuracy_score(y_pred,y_test)
print(f"Our accuracy score fro this model is {score }")
# saving the file as pickle 

rf_pickle =open('random_forest_penguin.pickle' ,'wb')
pickle.dump(rfc,rf_pickle)
rf_pickle.close()

output_pickle =open('ouput_penguin.pickle', 'wb')
pickle.dump(uniques,output_pickle)
output_pickle.close()

fig ,ax =plt.subplots()
ax =sns.barplot(x=rfc.feature_importances_, y=features.columns)

plt.title('which feature are teh mos timportant for species prediction ?')
plt.xlabel('Importance')
plt.ylabel('Features')
plt.tight_layout()
fig.savefig('feature_importance.png')
