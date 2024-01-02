#--- Deber de Desarrollo de Sistemas ---
#Nombre: Kevin Santiago Zurita Saritama
#Paralelo: SIR-S6-P1
#Fecha de entrega: 01-01-2024

import os
from openai import OpenAI

from ec.llm.utils.const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT

class InferenceService:
    def __init__(self):
        self._model = os.getenv('OPENAI_MODEL', 'text-davinci-003')
        self._openai_client = self.initialize_openai_client()
        self._prompt_template = 'Convert {number} to binary'

    def initialize_openai_client(self):
        # Aquí podemos inicializar o instanciar tu cliente OpenAI según las necesidades.
        pass

    def __inference(self, prompt):
        return CLEAN_TEXT(self.__openai_client.completions.create(
            model=self.__model,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        ).choices[0].text)

    def invoke(self, number: int) -> str:
        prompt = self.__prompt_template.format(number=number)
        return self.__inference(prompt)
