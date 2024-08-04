import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

file = open('boletin_sabancaya_202427.txt', "r")
bulletinText = file.read()
file.close()

response = client.chat.completions.create(
    # model='gpt-3.5-turbo',
    model='gpt-4o-mini',
    messages=[
        {
            'role': 'system',
            'content': """Eres un asistente que extrae datos de un texto, en formato json con las siguientes llaves:
            - volcano_name, descripción: Nombre de volcán
            - analysis_period, descripción: Periodo de análisis, fechas de la forma YYYY-MM-DD separado por una ','
            - issued_at, descripción: Fecha de emisión en la forma YYYY-MM-DD
            - alert_level, descripción: Nivel de alerta
            - summary, descripción: Resumen
            """
        },
        {
            'role': 'user',
            'content': bulletinText
        }
    ],
    temperature=0,
    response_format={'type': 'json_object'}
)

print(response.choices[0].message.content)

