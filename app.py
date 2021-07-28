import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


st.title(
	"Gases Reales"
)

st.subheader("Cátedra de Introducción a la Química UNLP. FCE")




x=np.linspace(-1,1,100)
y =x**2

fig,ax=plt.subplots(2,1)
ax=ax.flatten()
ax[0].plot(x,y)
ax[1].scatter(x,y)
st.pyplot(fig)

