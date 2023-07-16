import streamlit as st
import joblib
import sklearn
from time import sleep

def main():
    url = 'https://www.kaggle.com/code/muditgupta1086/churn-modelling'
    st.markdown("🔗[Source Code](%s)" % url)

    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:#232323;text-align:center">Bank Customer Churn Prediction</h2>
    </div>
    <img src="https://img.freepik.com/free-vector/bank-building-with-cityscape_1284-52265.jpg?w=2000" 
    style="width:100%; height: 30rem"></img>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    model = joblib.load('rf_churn')
    st.divider()
    
    credit_score = st.slider('Credit Score', 300, 900)
    
    age = st.slider('Age', 18, 100)
    
    tenure = st.slider('Tenure', 0, 10)
    
    balance = st.number_input('Enter Balance')
    
    NumOfProducts = st.number_input('Number of Product',0,10)
    
    HasCrCard = st.selectbox('Credit Card issued',
                      ('Yes', 'No'))
    
    boolSwitcher = {
        'Yes': 1,
        'No': 0
    }
    HasCrCard = boolSwitcher.get(HasCrCard)
    
    IsActiveMember = st.selectbox('Active Member Status',
                      ('Yes', 'No'))
    
    IsActiveMember = boolSwitcher.get(IsActiveMember)
    
    # st.write(IsActiveMember)
    
    EstimatedSalary = st.number_input('Estimated Salary')
    
    gender = st.selectbox('Gender',
                      ('Male', 'Female'))
    
    genderSwitcher = {
        'Male': 1,
        'Female':0
    }
    
    gender = genderSwitcher.get(gender)
    
    area = [0,0]
    
    geography = st.selectbox('Geography',
                      ('France', 'Spain','Germany'))
    
    geographySwitcher = {
        'France': [0,0],
        'Spain':[0,1],
        'Germany':[1,0]
    }
    
    geography = geographySwitcher.get(geography)
    
    if st.button('Predict Now'):
        
        with st.spinner('💬Model is predicting...'):
            sleep(5)
        
        prediction = model.predict(
            [[credit_score,age,tenure,balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,geography[0],geography[1],gender]])
        print(prediction[0])
        
        if(prediction[0]==0):
            st.success(f"📈 Customer did not leave the bank")
        else:
            st.warning(f'📉 Customer left the bank')
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    main()