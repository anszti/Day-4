import streamlit as st

st.write('Hello SHRDC')
st.write('Hello again from SHRDC')
st.write('mlem')

st.write("Hello friends")
st.header("Hello friends")
st.subheader("Hello friends")
st.caption("Hello friends")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown(''' :red[Streamlit] :orange[is] :green[fun] ''')
st.markdown("Here's a bouquet &mdash;\:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">This is advanced font manipulation!</p>'
st.markdown(new_title, unsafe_allow_html=True)



select1 = st.selectbox("Kuala Lumpur is located at", ['Malaysia', 'Thailand', 'UK'])
st.write("You have selected:", select1)

st.multiselect("Select 2 states", ['Selangor','Johor','Kedah'])

c1 = st.button("Click Me")
if c1:
    st.write("You have clicked the button.")

st.slider("Select the length of stay", 1,10, value=3)


number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write("The current number is ", number)



from PIL import Image
im = Image.open('shrdc_logo.png')
st.image(im, width=500)



import pandas as pd
df = pd.read_excel('sampledata.xlsx')
st.dataframe(df)

st.bar_chart(df, x="Location", y="Income")
st.line_chart(df, x="Household", y="Income")
st.scatter_chart(df, x="Household", y="Income", color='Month Fees')



tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
 st.header("A cat")
 st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
 st.header("A dog")
 st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
 st.header("An owl")
 st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



col1, col2, col3 = st.columns(3)
with col1:
 st.header("A cat")
 st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
 st.header("A dog")
 st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
 st.header("An owl")
 st.image("https://static.streamlit.io/examples/owl.jpg")


#to centralize
col11, col22, col33 = st.columns(3)
with col11:
 st.write()
with col22:
 st.header("A dog")
 st.image("https://static.streamlit.io/examples/dog.jpg")
with col33:
 st.write()