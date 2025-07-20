import streamlit as st
import streamlit.components.v1 as components
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from pathlib import Path


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Dashboard LUXAL", page_icon=":bar_chart:", layout="wide")


# Definir la ruta al archivo de configuración
config_path = Path(__file__).parent / '.streamlit' / 'config.yaml'

# Cargar la configuración desde el archivo YAML
with config_path.open() as file:
    config = yaml.load(file, Loader=SafeLoader)

# Crear el objeto de autenticación
authenticator = stauth.Authenticate(
    credentials=config['credentials'],
    cookie_name=config['cookie']['name'],
    cookie_key=config['cookie']['key'],
    cookie_expiry_days=config['cookie']['expiry_days']
)

# Renderizar el widget de inicio de sesión
fields = {
    'Form name': 'Iniciar sesión',
    'Username': 'Nombre de usuario',
    'Password': 'Contraseña',
    'Login': 'Iniciar sesión'
}
authenticator.login(location='main', fields=fields)

# Obtener el estado de autenticación desde st.session_state
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

authentication_status = st.session_state['authentication_status']
name = st.session_state.get('name')
username = st.session_state.get('username')

if authentication_status:
    authenticator.logout('Cerrar sesión', location='main')
    st.write(f'Bienvenido/a *{name}*')
    st.title('Dashboard LUXAL CORP S.A.S')
    # Aquí puedes agregar el contenido principal de tu aplicación
    def render_powerbi_dashboard():
        # HTML iframe del dashboard de Power BI con centrado
        powerbi_iframe = """
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <iframe title="Dashboard 2.1 con correcciones_1.863" 
                    width="1140" 
                    height="541.25" 
                    src="https://app.powerbi.com/reportEmbed?reportId=da1838c3-b954-491b-a9e8-ff9f8e22a0f5&autoAuth=true&ctid=585a4d92-db1d-4bbb-b5ac-c5299e3894e3" 
                    frameborder="0" 
                    allowFullScreen="true">
            </iframe>
        </div>
        """
        # Usar componentes para incrustar el iframe
        components.html(powerbi_iframe, height=650)

    render_powerbi_dashboard()

    # ---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)


elif authentication_status is False:
    st.error('Nombre de usuario o contraseña incorrectos')
elif authentication_status is None:
    st.warning('Por favor, ingresa tu nombre de usuario y contraseña')

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)