import streamlit as st
import pandas as pd
from selenium import webdriver

import tkinter as tk
from tkinter import filedialog
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)



st.title('Configurateur HAS de fiche Betie')
st.image('logo_betie.jpg')
st.text_input('Nom du Projet')
st.text_input('Utilisateur Betie')
st.text_input('Mot de passe Betie',type='password')
data=st.file_uploader('Données pour Betie')
dossier_telechargement = st.text_input('Dossier téléchargements - insérer ')
# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
st.write('Sélectionner dossier de téléchargements:')
clicked = st.button('Dossier téléchagement')
if clicked:
    dirname = st.text_input('Selected folder:', filedialog.askdirectory(master=root))
#dossier_rangement = st.text_input('Dossier de rangement')

#boutton = st.button('Créer les fiches Betie')

def creer_fiches(donnees):
    total = pd.read_excel(donnees)['Cubage béton'].sum()
    return(total)

if st.button('Créer les fiches Betie'):
    #result = creer_fiches(data)
    #st.write('result: %s' % result)
    URL = "http://ns381308.ovh.net/ecobilan/ficheProjet!ajouter.html?id=10744"
    firefoxOptions=Options()
    firefoxOptions.add_argument("--headless")
    service=Service(GeckoDriverManager().install())
    driver=webdriver.Firefox(options=firefoxOptions,service=service)
    driver.get(URL)
    st.markdown("Connexion à Betie réussie")

