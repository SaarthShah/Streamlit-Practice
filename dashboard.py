import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", layout="centered",
page_icon='🤖')
# 

st.set_page_config(page_title="Marketing", layout="centered",
page_icon='https://i.imgur.com/7EdF8Rl.png')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

#### ADDING THE DASHBOARD MENU ####

st.markdown("""
<nav class="navbar fixed-top navbar-expand-md navbar-dark" style="background-color: #0E1117; top:45px">
  <div class="container ">
    <a class="navbar-brand" href="#">
      <img src="https://i.imgur.com/EvY4Eef.png" alt="" height="35">
    </a>
  </div>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">Business</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Marketing <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Data</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">UX</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
today = datetime.now()
lastweek = today - timedelta(days=7)
lastweek_range = pd.date_range(start=lastweek,end=today).to_pydatetime().tolist()

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)