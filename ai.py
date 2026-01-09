import os 
from dotenv import load_dotenv 
from openai import OpenAI


load_dotenv()

api_key = os.getenv('API_KEY')

client = OpenAI(
    api_key=api_key,
    base_url='https://bothub.chat/api/v2/openai/v1'
)

def get_ai_recommendation(user_text):
    response= client.chat.completions.create(
        model='gemini-2.0-flash-exp:free',
        temperature=0.9,
        messages=[
            {'role':'system','content':'Ты опытный  кинокритик, рекомендуй пользователю фильм, эмоционально и с  короткым описание, четко и по делу.'},
            {'role':'user','content': f'Я люблю фильмы как:{user_text}'}
        ],
    )

    return response.choices[0].message.content