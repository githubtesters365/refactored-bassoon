import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
import plotly.figure_factory as ff



option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
''')



video_file = open('thesun.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)




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
    st.image("Earth.jpg")

with col2:
    st.header("Our Moon")
    st.image("Moon.jpg")

with col3:
    st.header("Mars")
    st.image("Mars.jpg")



st.image(image, caption='The Moon')


# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


video_file = open('lol.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)