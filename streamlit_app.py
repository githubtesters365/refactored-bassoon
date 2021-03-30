import streamlit as st
import numpy as np
import streamlit.components.v1 as components


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
''')




from PIL import Image
image = Image.open('solarsystem.jpg')





st.image(image, caption='1,2,3')






from PIL import Image
image = Image.open('sun.jpg')





st.image(image, caption='The Sun')



col1, col2, col3 = st.beta_columns(3)

with col1:
    st.header("mercury")
    st.image("mercury.jpg")

with col2:
    st.header("Venus")
    st.image("venus.jpg")

with col3:
    st.header("The Earth")
    st.image("earth.jpg")



from PIL import Image
image = Image.open('moon.jpg')




col1, col2, col3 = st.beta_columns(3)

with col1:
    st.header("The Earth")
    st.image("earth.jpg")

with col2:
    st.header("Our Moon")
    st.image("moon.jpg")

with col3:
    st.header("Mars")
    st.image("mars.jpg")



st.image(image, caption='The Moon')


video_file = open('lol.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
