from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

#interesting = st.checkbox('Interesting')
#save = st.checkbox('Save')

data = {'Source': ['BBCM', 'Janes', 'Secret', 'Cardinal'],
        'Relevance':[0.6, 0.7, 0.98, 0.3]
        #'Interesting': [interesting, interesting, interesting, interesting],
        #'Saved': [save, save, save, save]
       }

df = pd.DataFrame(data)
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_selection(selection_mode='multiple', use_checkbox=True)
gridoptions = gd.build()

grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

st.write('## Selected')
selected_row = grid_table["selected_rows"]
st.dataframe(selected_row)

