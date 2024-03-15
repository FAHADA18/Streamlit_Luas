import streamlit as st
from streamlit_option_menu import  option_menu
import numpy as np



#navigasi sidebar
with st.sidebar:
    selected = option_menu("Menghitung Luas Bangun", 
        ['Menghitung Luas Segitiga', 
         'Menghitung Luas Lingkaran','Menghitung Luas Persegi Panjang'], 
        icons=['gear', 'gear','gear' ], menu_icon="cast", 
        
        default_index=0)
    

#halaman hitung segitiga
if (selected == 'Menghitung Luas Segitiga') :
    st.title('Menghitung Luas Segitiga')
    alas = st.number_input("Masukkan Nilai Alas", 0)
    Tinggi = st.number_input("Masukkan Nilai Tinggi", 0)
    hitung = st.button("Hitung Luas")

    if hitung :
        luas = (0.5*alas*Tinggi)
        st.write("Luas Segitiga adalah =  ",luas)

#halaman hitung lingkaran        
if (selected == 'Menghitung Luas Lingkaran') :
    st.title('Menghitung Luas Lingkaran')
    
    radius = st.slider("Masukkan Nilai Jari-Jari", 0,1000)
    hitung = st.button("Hitung Luas")

    if hitung :
        luas = (np.pi*radius*radius)
        st.write("Luas Lingkaran adalah =  ",luas)
        
#halaman hitung persegi panjang
if (selected == 'Menghitung Luas Persegi Panjang') :
    st.title('Menghitung Luas Persegi Panjang')
    panjang = st.number_input("Masukkan Nilai Panjang", 0)
    lebar = st.number_input("Masukkan Nilai Lebar", 0)
    hitung = st.button("Hitung Luas")

    if hitung :
        luas = (panjang*lebar)
        st.write("Luas Persegi Panjang adalah =  ",luas)