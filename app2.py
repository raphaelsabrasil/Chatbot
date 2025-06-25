import streamlit as st 

st.title("Meu Segundo Aplicativo")

st.sidebar.title("Configurações")

st.sidebar.subheader("Nome do Usuário")
nome_usuario = st.sidebar.text_input("Digite seu nome")

st.header("Nome do Usuário")
st.subheader(nome_usuario)

st.sidebar.subheader("Números")
num1 = st.sidebar.number_input("Digite o primeiro número")
num2 = st.sidebar.number_input("Digite o segundo número")


st.sidebar.subheader("Operação")
operacao_selecionada = st.sidebar.radio("Escolha a operação que você quer realizar", ("Adição", "Subtração"))

btn_calcular = st.button("Calcular")

if btn_calcular:
    st.header("Operação escolhida")
    st.subheader(operacao_selecionada)
    st.header("Numeros selecionados")
    st.subheader(f"O primeiro número é: {num1}. O segundo número é: {num2}.")
    st.header("Resultado da Operação")
    if operacao_selecionada == "Adição":
        resultado = num1 + num2
    else:
        resultado = num1 - num2
    st.subheader(f"O Resultado da operação selecionada é: {resultado}")

    st.write("Esse foi um tutorial básico sobre o Streamlit.")
    