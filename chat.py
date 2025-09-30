import streamlit as st
import random 

lista_respostas = ["Ok", "Claro", "Tem certeza?", "Tudo bem", "Entendu"]

def app():
    st.header("Hash Chat", divider=True)
    st.write("Escreva e interaja com nosso chat!")

    mensagem_usuario = st.chat_input("Digite aqui sua mensagem...") 
    if mensagem_usuario:
        if "mensagens" in st.session_state:
            mensagens = st.session_state["mensagens"]
        else:
            mensagens = []
            st.session_state["mensagens"] = mensagens

        # Adicionar no mensagens a mensagem que o usuário enviou:
        mensagens.append({"usuario": "user", "texto": mensagem_usuario})

        # Mensagem da resposta do assistente:
        resposta = random.choice(lista_respostas)
        mensagens.append({"usuario": "assistant", "texto": resposta})

        for mensagem in mensagens:
            # Colocar a mensagem do usuário na tela.
            with st.chat_message(mensagem["usuario"]):
                st.write(mensagem["texto"])


app()   