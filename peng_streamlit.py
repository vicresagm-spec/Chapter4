import streamlit as st
import pickle
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd 
st.title("Penguin Classifier")


password_guess =st.text_input("enter the password",type ='password')
if password_guess!= st.secrets["app_password"]:
    st.warning('incorrect password')
    st.stop()
st.write("This app uses 6 input to predict the species of penguin using"
         " a model built on the Plamer's Penguins data set ")
penguin_df =pd.read_csv('penguins.csv')
rf_pickle =open('random_forest_penguin.pickle','rb')

map_pickle= open('ouput_penguin.pickle','rb')
rfc =pickle.load(rf_pickle)
unique_penguin_mapping =pickle.load(map_pickle)

rf_pickle.close()
map_pickle.close()
# Wrap all inputs in a form -prevetns rerun on every single change 
with st.form('User_inputs'):
    island =st.selectbox('Penguin Island',options =['Biscoe','Dream','Torgerson'])
    sex= st.selectbox('Sex',options=['Female','Male'])
    bill_length =st.number_input('Bill Lenght (mm)',min_value =0)
    bill_depth= st.number_input('Bill Depth (mm)',min_value=0)
    flipper_length= st.number_input('Flipper Length(mm)',min_value=0)
    body_mass =st.number_input('Body_mass(g)',min_value=0)
    st.form_submit_button()
#st.write(f'The User inputs are {island,sex,bill_length,bill_depth,flipper_length,body_mass}')

# Add prediction Logic
island_biscoe,island_dream ,island_torgerson =0,0,0
if island =='Biscoe':
    island_biscoe=1
elif island =='Dream':
    island_dream =1
elif island == 'Torgerson':
    island_torgerson=1


# one hot encode sex

sex_female,sex_male =0,0
if sex=='Female':
    sex_female= 1
elif sex =='Male':
    sex_male =1


# predict
new_prediction =rfc.predict([[bill_length, bill_depth, flipper_length,
                                body_mass, island_biscoe, island_dream,
                                island_torgerson, sex_female, sex_male]])

predcition_species =unique_penguin_mapping[new_prediction][0]
st.write(f'We predict your penguin is of the {predcition_species} species')
st.write('Feature rnaked by importnace below')
st.image('feature_importance.png')

# histogram with user inout as vertical line
st.write('Histogram of each variable seoerated by species.'
         'Vertical line =your input')
fig ,ax =plt.subplots()
ax = sns.displot(x=penguin_df['bill_length_mm'],hue =penguin_df['species'])
plt.axvline(bill_length)
plt.title('Bill Depth by Species')
st.pyplot(ax)


fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['bill_depth_mm'], hue=penguin_df['species'])
plt.axvline(bill_depth)
plt.title('Bill Depth by Species')
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['flipper_length_mm'], hue=penguin_df['species'])
plt.axvline(flipper_length)
plt.title('Flipper Length by Species')
st.pyplot(ax)