# Sistema do Natal de 2023

> Esse projeto foi construido para promover o evento de Natal na cidade de Nova Friburgo pela Prefeitura Municipal de Nova Friburgo em 2023.

### Principais tecnologias utilizadas
[![Python](https://img.icons8.com/color/48/000000/python.png)](https://www.python.org/)
[![Django](https://img.icons8.com/color/48/000000/django.png)](https://www.djangoproject.com/)
[![Bootstrap](https://img.icons8.com/color/48/000000/bootstrap.png)](https://getbootstrap.com/)

## 💻Pré-requisitos
- Versão 3 ou mais recente do Python.

## 📦 Instalação de dependências
Antes de instalar as dependências, é altamente recomendado que haja a criação de um ambiente virtual(*Virtual Environment*) o qual ficará isolado a hospedagem dos pacotes necessários para a execução do projeto. Logo, para tal ato, execute em um terminal dentro da pasta principal o seguinte comando:

`python3 -m venv nomeDoAmbienteVirtual`

Após a inicialização do ambiente(*venv*) com o nome desejado(*nomeDoAmbienteVirtual*), é necessário entrar dentro do espaço. Desse modo, execute o devido comando dependendo do sistema operacional dentro da mesma pasta que foi criada a *venv* usado:

**Windows**

Usando PowerShell:

`venv\Scripts\Activate.ps1`

Usando o _prompt_ de comando:

`venv\Scripts\activate.bat`

**Distribuições GNU/Linux e MacOS**

`source venv/bin/activate`

Agora, basta inserir os pacotes cruciais para o sistema através do comando que deve ser utilizado dentro do diretório onde o ambient virtual se encontra:

`pip install -r requirements.txt`

Ou baixe os módulos a seguir:

- asgiref==3.4.1
- beautifulsoup4==4.11.1
- certifi==2023.7.22
- charset-normalizer==3.2.0
- Django==3.2.15
- django-bootstrap-v5==1.0.11
- django-colorfield==0.8.0
- et-xmlfile==1.1.0
- fontawesomefree==6.1.2
- idna==3.4
- importlib-metadata==4.8.3
- openpyxl==3.1.2
- pdfkit==1.0.0
- Pillow==10.0.0
- PyMySQL==1.0.2
- python-dateutil==2.8.2
- pytz==2022.2.1
- pyYAML==6.0
- requests==2.82.2
- six==1.16.0
- soupsieve==2.3.2.post1
- sqlparse==0.4.2
- typing\_extensions==4.1.1
- urllib3==1.26.16
- zipp==3.6.0

## 🔧Configurações

### Configurando as variáveis de ambiente.
Para definir as variáveis do ambiente do projeto, deve-se criar um arquivo chamado `.envvars.yaml` na raiz do projeto contendo as seguintes informações conforme o modelo abaixo:

```
db_host: '127.0.0.1'
db_name: 'nomedobanco' # Este projeto foi pensando para suportar MySQL ou MariaDB.
db_user: 'usuariodobanco' # Usuário do banco com todas as permissões para a base de dados.
db_pw: 'senhadobanco' # A senha do respectivo usuário do banco.
django_secret_key: 'secretkey123456' # Insira sua django secret key.
debug_mode: True # Use True para DEBUG or False para PRODUCTION.
sqlite_mode: True # Use True para usar a engine do SQLITE, mas faça isso apenas em desenvolvimento.
email_sistema: 'seu@email.com' # E-mail utilizado para recuperação de senha.
email_pw: 'su@senha123' # Senha do email acima.
hCAPTCHA_Public_Key: '6484-dsadad4994ds9492314' # Inscreva-se https://www.hcaptcha.com/.
hCAPTCHA_Secret_Key: '6484-dsadad4994ds94914dsd4900c0952' # Cadastre seu site após se inscrever.
GOOGLE_OAUTH2_PUBLIC_KEY: '74526484-dsadad494d2314.apps.googleusercontent.com' # Inscreva-se https://console.cloud.google.com/ e gere as chaves para seu site.
GOOGLE_OAUTH2_SECRET_KEY: 'GOCSPX-dsadad49das9494d2314'
FACEBOOK_DEVELOPER_PUBLIC_KEY: '4994ds949494d14' # Inscreva-se https://developers.facebook.com/ e gere as chaves para seu site
FACEBOOK_DEVELOPER_SECRET_KEY: '494d231479ff65cb6307b3'
```

## Usando o projeto
Comece criando as tabelas do banco com o seguinte comando feito na linha de comando dentro da pasta do projeto:

**Windows**

`python manage.py migrate`

**Distribuições GNU/Linux e MacOS**

`python3 manage.py migrate`

Para entrar dentro do *Django Admin*, é fundamental criar um super usuário usando o comando:

**Windows**

`python manage.py createsuperuser`

**Distribuições GNU/Linux e MacOS**

`python3 manage.py createsuperuser`

No campo de usuário, deve-se informar o **e-mail**. As credenciais(e-mail e senha) serão utilizados para acessar o *Django Admin*.

## Contribuindo com o projeto
Para ajudar em tal sistema, você pode:

- Comentar na *issue* para qual você deseja se voluntariar ou solicitar mais informações.
- Criar um *fork* deste repositório.
- Desenvolver o sistema seguindo as funcionalidades e critérios de aceitação.
- Criar um *pull request* detalhando as alterações realizadas.
