#Base Image to use
FROM python:3.9

ENV STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true
ENV PROJECT_ID=${PROJECT_ID}
ENV REGION=${REGION}
ENV LLM_MODEL=${LLM_MODEL}
ENV IDENTITY_PLATFORM_REST_API=${IDENTITY_PLATFORM_REST_API}
ENV IDENTITY_PLATFORM_API_KEY=${IDENTITY_PLATFORM_API_KEY}


EXPOSE 8080
WORKDIR /app
COPY app.py app_config.py requirements.txt favicon.ico image_logo.png /app/
ADD .streamlit ./.streamlit
ADD app_services ./app_services
ADD app_pages ./app_pages
ADD app_data ./app_data


#install all requirements in requirements.txt
RUN pip install -r requirements.txt

# Run the web service on container startup
CMD ["streamlit", "run", "app.py", "--server.port=8080"]