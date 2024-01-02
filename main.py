#--- Deber de Desarrollo de Sistemas ---
#Nombre: Kevin Santiago Zurita Saritama
#Paralelo: SIR-S6-P1
#Fecha de entrega: 01-01-2024

from dotenv import load_dotenv
import re

import os

from ec.llm.service.InferenceService import InferenceService
from ec.llm.utils.const import CLEAN_TEXT

if __name__ == '__main__':
    load_dotenv('secrets/.env')
    #print(os.getenv('OPENAI_API_KEY'))
    # custom_dict = {'a': 'b'}
    # print(custom_dict['c'])
    # print(custom_dict.get('c', 'kepler'))
    print ("La conversión binaria del número ingresado es: ")
    print(InferenceService().invoke('2024'))
