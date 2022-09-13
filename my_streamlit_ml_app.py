import streamlit as st
st.title("this is a title")
st.header("this is a header")
st.latex(2+2)
st.write("hello friend")
st.code("x=22")
st.caption("this is a caption")
st.subheader("hello friend")


import altair as alt
import numpy as np
import pandas as pd

# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2

# Convert this grid to columnar data expected by Altair
source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

c1 = alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q'
)

st.altair_chart(c1, use_container_width=True)

import streamlit as st
sentences1 = st.text_input("hej med dig")
sentences2 = st.text_input("det er nr 2")
st.write("sentences1 is:, sentences1")
st.write("sentences2 is:, sentences2")
if st.button("Skriv her") :
    st.write("sentences1 is:, sentences1")
    st.write("sentences2 is:, sentences2")