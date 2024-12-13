
from app_services.app_service_gemini import call_llm 
from app_services.app_service_dao import get_data
import streamlit as st
import pandas as pd
from app_services.app_service_firestore import save_feedback


def generate_content(region, pergunta, data,message_placeholder):
    persona = """
                Você é IARA uma experiente analista de dados focados em vendas de carros 
                Sua missão é apoiar gestores de vendas através da análise de dados relacionados ao time de vendas e gerar insights e recomendações com o objetivo de melhorar as vendas da empresa
                Analise todo com o conjunto de dados antes de responder solicitações.
                Cada registro do conjundo de dados fornecido representa uma venda
                Não invente informações
                Gere respostas em markdown
              """
    resposta = call_llm(region, pergunta, data,persona)
    resposta = resposta.replace("$", "\$")
    st.session_state.QUESTION = pergunta
    st.session_state.ANSWER = resposta 

    with message_placeholder:
        st.markdown(st.session_state.ANSWER  , unsafe_allow_html=True)


@st.dialog("Avaliar")
def get_feedback():
    if "QUESTION" in st.session_state and st.session_state['QUESTION'] is not None:
        st.write(st.session_state['QUESTION'])
        feedback_mapping = ["Ruim", "Bom"]
        feedback_selected = st.feedback("thumbs",key="feedback_sentiment1")
        
        if feedback_selected is not None:
            save_feedback("IARA", "CHAT",feedback_mapping[feedback_selected], st.session_state['QUESTION'] ,st.session_state['ANSWER'] )
            st.session_state['QUESTION'] = None
            st.rerun()

if "data" not in st.session_state:
    data = get_data()
    st.session_state.data = data

tab1, tab2 = st.tabs(["Dados", "Exemplos de Perguntas"])

with tab1:
    with st.expander(f"Dados de Vendas..."):
        st.dataframe(pd.DataFrame(st.session_state['data'])) 

with tab2:
    with st.expander(f"Exemplos de perguntas..."):
        st.write("Qual o cenário geral da carteira do time de vendas")
        st.write("Preciso dar uma atenção especial para qual vendedor?")      


with st.container(border=1,):
    col1, col2 = st.columns([1,6])
    with col1:
        st.image(image="image_logo.png",width=100)  
    
    with col2:
        st.markdown('<h4 class="caixa-titulo"><font color="red">IA</font color>RA | Assistente de Vendas 💬</h4>', unsafe_allow_html=True)


placeholder = st.empty()    

with st.sidebar:

        st.session_state['SELECTED_REGION']  = st.selectbox(
            "Selecione a região",
            (
            "us-central1",
            "us-east1",
            "us-east4",
            "us-west1",
            "southamerica-east1",
            "southamerica-west1",                          
            "asia-east1",
            "asia-east2",),
            index=3,

        )
        
        if st.button("Feedback",use_container_width=True,type="secondary"):
            get_feedback()
            
  

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display assistant response in chat message container
message_placeholder = st.empty()
prompt = st.chat_input("Faça alguma pergunta...")
st.session_state.messages.append(prompt)    


if 'presentation' not in st.session_state:
    st.session_state['presentation'] = 'done'
    generate_content(st.session_state['SELECTED_REGION'] ,"De forma breve, quem é você e sobre o que podemos falar?", None,message_placeholder) 

if st.session_state['ANSWER']:
    with placeholder:
        st.session_state['ANSWER']  

if prompt:
    with placeholder,st.spinner('Analisando solicitação...'): 
        generate_content(st.session_state['SELECTED_REGION'] ,prompt, str(st.session_state['data']),message_placeholder)    


