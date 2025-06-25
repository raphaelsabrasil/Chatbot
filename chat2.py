import openai
import streamlit as st
import os

openai.api_key = os.getenv("SENHA_OPEN_AI")

st.title("Chat com ChatGPT Turbo")
st.write("***")

if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = []

pergunta = st.text_input("Digite a pegurta:")
btn_enviar = st.button("Enviar pergunta")
if btn_enviar:
    st.session_state.hst_conversa.append({"role": "user", "content": pergunta})
    retorno_openai = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = st.session_state.hst_conversa,
        max_tokens = 500,
        n=1
    )
    st.session_state.hst_conversa.append(
        {"role": "assistant",
         "content": retorno_openai['choices'][0]['message']['content']})

if len(st.session_state.hst_conversa) > 0:
    for i in range(len(st.session_state.hst_conversa)):
        if i % 2 == 0:
            st.write("Você: " + st.session_state.hst_conversa[i]['content'])
        else:
            st.write("Reposta IA: " + st.session_state.hst_conversa[i]['content'])


