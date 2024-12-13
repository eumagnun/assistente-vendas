import streamlit as st
from PIL import Image
from app_services.app_service_identity_platform import log_out, is_logged_in


if is_logged_in():
    pg = st.navigation([st.Page("./app_pages/app_page_chat.py",title= "IARA Assistente de Vendas",icon="🤖"), 
                        st.Page(log_out,title= "Logout",icon=":material/logout:"),
                    ],)
else:
    pg = st.navigation([st.Page("./app_pages/app_page_login.py",title= "Login",icon= "🔑"),
                        ],)
    

im = Image.open("favicon.ico")

st.set_page_config(page_title="IARA",
                   layout='wide',
                   page_icon=im,)
                  
pg.run()