# IARA-assistente-vendas


 - Clonar esse repo
````
git clone xxxxxxx
````
 - Criar ambiente virtual:
````
python -m venv venv_assistente
````
 - Ativar ambiente virtual:
```
#Linux
source venv_assistente/bin/activate
#ou
#Windows
.\venv_assistente\Scripts\activate
```
 - Instalar dependências:
```
pip install -r requirements.txt
#ou
pip  install --force-reinstall -r requirements.txt
```
 - Definir variáveis de ambiente via .env ou outra estratégia

```

IDENTITY_PLATFORM_REST_API="XXXXX"
IDENTITY_PLATFORM_API_KEY="XXXXXX"
PROJECT_ID="XXXXXXX"
REGION="XXXXXXX"
LLM_MODEL="XXXXXXXXX"
```
 - Executar app:
```
sh run.sh
```
Caso queira gerar uma imagem para implantação no Cloud Run:

 - Gerar imagem:
````
docker build -t us-central1-docker.pkg.dev/[PROJECT_ID]/demos/demo_assist_vendas.
````
 - Enviar imagem para o Registry:
````
docker push us-central1-docker.pkg.dev/[PROJECT_ID]demos/demo_assist_vendas
````
