import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df_madre = pd.read_excel('ruta_del_archivo/roca_madre.xlsx')  # Cambia la ruta del archivo
df_reservorio = pd.read_excel('ruta_del_archivo/roca_reservorio.xlsx')  # Cambia la ruta del archivo
df_sello = pd.read_excel('ruta_del_archivo/roca_sello.xlsx')  # Cambia la ruta del archivo

# Limpiar los datos
df_madre_clean = df_madre[['Propiedades', 'Permeabilidad (md)', 'Densidad (g/cm^3)', 'Arcilla (%)', 'Materia Organica (%)']]
df_madre_clean = df_madre_clean.dropna()

df_reservorio_clean = df_reservorio[['Propiedades', 'Porosidad (%)', 'Permeabilidad (md)', 'Mojabilidad (°)', 'Densidad (g/cm³)']]
df_reservorio_clean = df_reservorio_clean.dropna()

df_sello_clean = df_sello[['Roca Sello', 'Permeabilidad (Md)', 'Porosidad', 'Espesor (m)']]
df_sello_clean = df_sello_clean.dropna()

# Graficar las propiedades físicas de las Rocas Madre
properties_madre = ['Permeabilidad (md)', 'Densidad (g/cm³)', 'Arcilla (%)', 'Materia Organica (%)']
values_madre = [df_madre_clean['Permeabilidad (md)'], df_madre_clean['Densidad (g/cm^3)'], df_madre_clean['Arcilla (%)'], df_madre_clean['Materia Organica (%)']]

# Graficar las propiedades físicas de las Rocas Reservorio
properties_reservorio = ['Porosidad (%)', 'Permeabilidad (md)', 'Mojabilidad (°)', 'Densidad (g/cm³)']
values_reservorio = [df_reservorio_clean['Porosidad (%)'], df_reservorio_clean['Permeabilidad (md)'], df_reservorio_clean['Mojabilidad (°)'], df_reservorio_clean['Densidad (g/cm³)']]

# Graficar las propiedades físicas de las Rocas Sello
properties_sello = ['Permeabilidad (Md)', 'Porosidad', 'Espesor (m)']
values_sello = [df_sello_clean['Permeabilidad (Md)'], df_sello_clean['Porosidad'], df_sello_clean['Espesor (m)']]

# Crear la aplicación Streamlit
st.title('Propiedades Físicas de Rocas Madre, Reservorio y Sello')

# Mostrar las gráficas de Rocas Madre
st.subheader('Propiedades de Rocas Madre')
for i, prop in enumerate(properties_madre):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(df_madre_clean['Propiedades'], values_madre[i], color='skyblue')
    ax.set_xlabel('Propiedades de Rocas Madre')
    ax.set_ylabel(prop)
    ax.set_title(f'{prop} en Rocas Madre')
    plt.xticks(rotation=90)
    st.pyplot(fig)

# Mostrar las gráficas de Rocas Reservorio
st.subheader('Propiedades de Rocas Reservorio')
for i, prop in enumerate(properties_reservorio):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(df_reservorio_clean['Propiedades'], values_reservorio[i], color='lightcoral')
    ax.set_xlabel('Propiedades de Rocas Reservorio')
    ax.set_ylabel(prop)
    ax.set_title(f'{prop} en Rocas Reservorio')
    plt.xticks(rotation=90)
    st.pyplot(fig)

# Mostrar las gráficas de Rocas Sello
st.subheader('Propiedades de Rocas Sello')
for i, prop in enumerate(properties_sello):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(df_sello_clean['Roca Sello'], values_sello[i], color='lightgreen')
    ax.set_xlabel('Propiedades de Rocas Sello')
    ax.set_ylabel(prop)
    ax.set_title(f'{prop} en Rocas Sello')
    plt.xticks(rotation=90)
    st.pyplot(fig)
