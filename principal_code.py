import streamlit as st
import pandas as pd
import numpy 
import openpyxl

#--------------------Productos--------------------
# Esta parte del codigo sirve para la extracción de los precios de los productos.

productos=pd.read_excel('productos.xlsx')
df=pd.DataFrame(productos)

def obtprecio(artcl):
               # simboloq=df[df['nombre']==simb]['simbolo']
                dfSearchedElement = df['precio'].where(df['articulo']==artcl)
                dfSearchedElement.dropna(inplace=True)
                return dfSearchedElement.squeeze()
        
        
cols = st.columns([4,5,4])

cant = st.slider('Cantidad de productos', 0, 20)

while cant != 0:  
  with cols[0]:
    producto = st.text_input('Coloque el producto')
    st.text(producto)
    
  with cols[1]:
    st.text(obteprecio(producto))
    
  with cols[2]:
    st.text( )
    
    cant -= 1
    
    


