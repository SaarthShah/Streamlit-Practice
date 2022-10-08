import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", layout="centered",
page_icon='🤖')
# 

st.markdown("## KPI First Row")
kpi1, kpi2,kpi3 = st.columns(3)

with kpi1:
    st.markdown("**KPI 1**")
    kpi1_no =1
    st.markdown(f"##{kpi1_no}") 

with kpi2:
    st.markdown("**KPI 2**")
    kpi2_no =2
    st.markdown(f"##{kpi2_no}") 

with kpi3:
    st.markdown("**KPI 3**")
    kpi3_no =3
    st.markdown(f"##{kpi3_no}")

st.markdown("</hr>", unsafe_allow_html=True)

st.markdown("## KPI Second Row")

kpi01,kpi02, kpi03, kpi04, kpi05 = st.columns(5)

with kpi01:
    st.markdown("**KPI 01**")
    kpi01_no =1
    st.markdown(f"##{kpi01_no}")

with kpi02:
    st.markdown("**KPI 02**")
    kpi02_no =2
    st.markdown(f"##{kpi02_no}")

with kpi03:
    st.markdown("**KPI 03**")
    kpi03_no =3
    st.markdown(f"##{kpi03_no}")

with kpi04:
    st.markdown("**KPI 04**")
    kpi04_no =4
    st.markdown(f"##{kpi04_no}")

with kpi05:
    st.markdown("**KPI 05**")
    kpi05_no =5
    st.markdown(f"##{kpi05_no}")


st.markdown("</hr>", unsafe_allow_html=True)

st.markdown("## Chart Layout")

first_chart, second_chart = st.columns(2)
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))


with first_chart:
    st.markdown("### First Chart")
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(df.index, df['A'])
    st.pyplot(fig)

with second_chart:
    st.markdown("### Second Chart")
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(df.index, df['B'])
    st.pyplot(fig)
