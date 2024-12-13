import streamlit as st
from app_services.app_service_identity_platform import log_in, log_out, is_logged_in

col1, col2 , col3= st.columns([2,3,2])
def login():
    with placeholder.container():
      
        with col2:
            with st.container(border=1,):
                st.image(image="image_logo.png",width=50)  
                st.markdown('<h4 class="caixa-titulo"><font color="red">IA</font color>RA | Assistente de Vendas 💬</h4>', unsafe_allow_html=True)
                username = st.text_input("Username", key="username" )
                password = st.text_input("Password", key="password", type="password")

                if st.button("Entrar"):
                    log_in(username,password,placeholder)


   
placeholder = st.empty()    
with col2:
    login()  

            



          