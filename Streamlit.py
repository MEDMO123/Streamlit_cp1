import streamlit as st
st.title('Bonjour les gignols')
st.header("This is a header")
st.text("Hello Gomycode!!!")
st.markdown("### Ceci est un markdown")

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero" )
st.exception(exp)

from PIL import Image
img = Image.open("streamlit.png")

st.image(img, width=200)