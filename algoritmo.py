#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Script para la descarga de información de LP DAAC
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: Created on Thu Sep 28 08:38:15 2017
# Version: 1.0
#######################################
"""

# librerías
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import urllib.request
import os

def main():
    # url para la descarga
    URL = "https://e4ftl01.cr.usgs.gov/MOLA/MYD13C1.006/"

    # realizar el request y obtener los subfolders
    r = requests.get(URL)

    # parsear la información
    soup = BeautifulSoup(r.text, "html.parser")

    # guardar links de subcarpetas
    array_subcarpetas = []

    # ciclo de parseo
    for link in soup.find_all("a"):
        array_subcarpetas.append(link.get("href"))

    # obtener los archivos individuales
    for subfolder in array_subcarpetas[7:]:
        # crear url de subcarpeta
        SUB_URL = "{}{}".format(URL,subfolder)

        # consulta subcarpeta
        print(SUB_URL)
        r_subfolder = requests.get(SUB_URL)

        # parser información
        soup_subfolder = BeautifulSoup(r_subfolder.text, "html.parser")

        array_archivos = []

        for link_carpetas in soup_subfolder.find_all("a"):
            array_archivos.append(link_carpetas.get("href"))

        # nombre del archivo
        nombre_archivo = array_archivos[-2]

        # url para descarga
        URL_DESCARGA = "{}{}{}".format(URL,subfolder,nombre_archivo)

        # descarga del archivo
        print(URL_DESCARGA)

        os.system("wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --keep-session-cookies {}".format(URL_DESCARGA))


if __name__ == '__main__':
    main()
