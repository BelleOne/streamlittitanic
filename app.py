import streamlit as st
from joblib import load


model = load('titanic_df.joblib')

st.title('Titanic Predictions')

st.sidebar.title('Menu')

menu = ['Home', 'Predictions']

st.sidebar.selectbox('', menu)

# input with sideder
age = st.slider('age',0.42,80.0,30.0)
sibsp = st.slider('Sibsp',0,8,0)
parch = st.slider('Parch',0,8,0)
fare = st.slider('Fare',0.0,512.32,7.83)

#add predictions button
predic_btn = st.button('Predictions')

if predic_btn :
    input_data = [[age, sibsp, parch,fare]]

    predicton = model.predict(input_data)

    predict_proba = model.predict_proba(input_data)
# display predictions and show them
    st.subheader('predicton') 
    if predicton[0]== 1:
    
            st.write('survived')
    else :
            st.write('not survived')

    st.subheader('Predictions probability')
    st.write(f'survived : {predict_proba[0][1]:.2f}')
    st.write(f'not survived : {predict_proba[0][0]:.2f}')

    #predic_btn = st.button('Predictions')







