import json
import requests
import streamlit as st

from requests.exceptions import HTTPError
from google.oauth2.credentials import Credentials
import app_config as app_config


def sign_in_with_email_and_password(email, password):
    request_url = "%s:signInWithPassword?key=%s" % (app_config.IDENTITY_PLATFORM_REST_API, app_config.IDENTITY_PLATFORM_API_KEY)
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
    
    req = requests.post(request_url, headers=headers, data=data)
    # Check for errors
    try:
        req.raise_for_status()
    except HTTPError as e:
        raise HTTPError(e, req.text)
        
    response =  req.json()

    return  Credentials(response['idToken'], response['refreshToken'])

def log_in(usuario, senha, placeholder):
    try:
        creds =  sign_in_with_email_and_password(usuario, senha)
        if(creds.token):
            st.session_state["logged_in"] = True
            print(str(creds))
            st.success("Logged in!")
            st.rerun()
            placeholder.empty()
    except HTTPError as e:
        print(e)
        st.error("Não foi possivel autenticar!")

def log_out():
    st.session_state["logged_in"] = False
    st.info("Logged out!")
    st.rerun()

def is_logged_in():
    return st.session_state.get("logged_in", False)

 