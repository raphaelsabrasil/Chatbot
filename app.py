import streamlit as st 

st.title("Meu Primeiro APP")
st.header("Header")
st.subheader("Subheader")

st.button("Reset", type="primary")
if st.button("Say Hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")


left, middle, right = st.columns(3)
if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", use_container_width=True):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")

left, right = st.columns(2)
if left.button("Hello!", use_container_width=True):
    left.markdown("Good morning!")
if right.button("Goodbye!", use_container_width=True):
    right.markdown("See you later!") 

name = st.text_input("Digite seu nome aqui:")
st.write(f"Seu nome é {name}")