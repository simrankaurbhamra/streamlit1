import streamlit as st
import plotly.express as px
import pandas as pd
st.title("Student Info")
st.text_input("Enter your Name")
st.text_input("Enter your age")
st.date_input("Enter your DOB")
st.radio("Pick your gender",["Male","Female"])
st.text_input("Enter your Email")
st.file_uploader("upload your picture")
st.multiselect("choose your Subjects",["English","Hindi","Maths","Punjabi","Science","Social Science"])
st.slider("Rate your Communication skills",0,5)
st.select_slider("How are you as a Leader",["Outstanding","Excellent","Very Good","Good","Average","Poor"])
st.write("Do you like your College")
st.checkbox("yes")
st.checkbox("no")
df = pd.read_csv('sales.csv')
col1, col2 = st.columns([2,1])
with col1:
    sunburst_fig = px.sunburst( df,
        path=['Category', 'SubCategory','Discount'],
        values='Discount',
        title='Discount Breakdown'
       )
    st.plotly_chart(sunburst_fig,use_container_width=True)
with col2:
     bar_fig = px.bar(df.groupby('SubCategory')['Sales'].sum().reset_index(),
        x='SubCategory',
        y='Sales',
        title='Sales by SubCategory',
        labels={'Sales': 'Total Sales'}
        )
     st.plotly_chart(bar_fig,use_container_width=True)

st.button("Submit")

