from openai import OpenAI
import streamlit as st 
import os

# Uso de senha com Variável de Ambiente
client = OpenAI(
    api_key=os.environ['SENHA_OPEN_AI'],        # verificar nova senha OpenAI
) 
# ou pode usar >>> client = OpenAI(api_key = os.getenv("SENHA_OPEN_AI"))

# ou pip install python_dotenv >>>
# from dotenv import load_dotenv
# import os

# load_dotenv()
# api_key = os.environ['SENHA_OPEN_AI']

st.title("Chat com ChatGPT")
st.write("***")

if "hst_conversa" not in st.session_state:
    st.session_state.hst_conversa = []

pergunta = st.text_input("Digite a pergunta:")
btn_enviar = st.button("Enviar pergunta")
if btn_enviar:
    st.session_state.hst_conversa.append({"role": "user", "content": pergunta})
    retorno_openai = client.chat.completions.create(
        model = "gpt-4.1",
        messages = st.session_state.hst_conversa,
        max_tokens = 500,
        n=1,
    )
    # Conforme código descrito nos docs da OpenAI >>> https://platform.openai.com/docs/api-reference/chat/create >>>
    # st.write(retorno_openai.choices[0].message.content)
    st.session_state.hst_conversa.append(
        {"role": "assistant",
         "content": retorno_openai.choices[0].message.content}
    )
    
if len(st.session_state.hst_conversa) > 0:
    for i in range(len(st.session_state.hst_conversa)):
        if i % 2 == 0:
            st.write("Você: " + st.session_state.hst_conversa[i]['content'])
        else:
            st.write("Reposta IA: " + st.session_state.hst_conversa[i]['content'])