from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
interesting = st.checkbox('Interesting)

st.write(pd.DataFrame({'Source': ['BBCM', 'Janes', 'Secret', 'Cardinal'],
                   'Relevance':[0.6, 0.7, 0.98, 0.3],
                      'User input': [interesting, interesting, interesting, interesting]}))
                          
