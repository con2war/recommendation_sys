import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("Phone Recommendatation system")
phone_df=pickle.load(open("meta_data.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
list_phone=np.array(phone_df["model"])
option = st.selectbox(
"Select Phone ",
(list_phone))

def phone_recommend(phone):
     index = phone_df[phone_df['model'] == phone].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     l=[]
     for i in distances[1:6]:
          l.append("{}".format(phone_df.iloc[i[0]].model))
          # return("{} {}".format(movie_df.iloc[i[0]].title, movie_df.iloc[i[0]].urls))
     return(l)
if st.button('Recommend Me'):
     st.write('Phones Recomended for you are:')
     # st.write(movie_recommend(option),show_url(option))
     df = pd.DataFrame({
          'Phone Recommended': phone_recommend(option),
     })

     st.table(df)