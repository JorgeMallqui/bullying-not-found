import streamlit as st
import datetime

# --- CONFIGURACIÓN DE LA PÁGINA WEB ---
st.set_page_config(page_title="Escudo Digital - Alerta Cyberbullying", page_icon="🛡️", layout="centered")

# --- PALETA DE COLORES Y ANIMACIONES INTERACTIVAS (Beige, Melón y Latido CSS) ---
st.markdown("""
    <style>
    /* Fondo principal de la página (Beige muy suave y cálido) */
    .stApp {
        background-color: #FDF9F2;
    }
    
    /* Títulos principales */
    h1, h2, h3, h4 {
        color: #5D4A3E !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Contenedor centrado para el logotipo interactivo */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;
    }
    
    /* --- ANIMACIÓN DE LATIDO DE CORAZÓN (PULSE) --- */
    @keyframes latido {
        0% { transform: scale(1); }
        20% { transform: scale(1.1); }
        40% { transform: scale(1); }
        60% { transform: scale(1.15); }
        80% { transform: scale(1); }
        100% { transform: scale(1); }
    }
    
    /* Aplicamos el latido al emoji del escudo gigante */
    .escudo-interactivo {
        font-size: 70px;
        animation: latido 2.5s infinite ease-in-out;
        display: inline-block;
        cursor: pointer;
    }
    
    /* Cajas de texto modernas y redondeadas */
    .stTextArea textarea, .stTextInput input {
        background-color: #FFFFFF !important;
        border: 2px solid #E6D7C3 !important;
        border-radius: 12px !important;
        color: #4A3B32 !important;
    }
    
    /* Tarjetas de mensajes con estilo amigable */
    .tarjeta-guardian {
        background-color: #FFFFFF;
        border-left: 5px solid #FFB399;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.03);
        margin-top: 15px;
    }
    
    /* Botón Principal (Color Melón Amigable) */
    div.stButton > button:first-child {
        background-color: #FFB399 !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 0.8rem 2rem !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        font-size: 16px !important;
        box-shadow: 0px 4px 12px rgba(255, 179, 153, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    
    /* Efecto al pasar el mouse por el botón */
    div.stButton > button:first-child:hover {
        background-color: #FFA184 !important;
        transform: translateY(-2px);
        box-shadow: 0px 6px 15px rgba(255, 161, 132, 0.4) !important;
    }
    
    /* Estilo para las pestañas de la psicóloga */
    .streamlit-expanderHeader {
        background-color: #F5EBE0 !important;
        border-radius: 8px !important;
        color: #5D4A3E !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGOTIPO INTERACTIVO CON ANIMACIÓN DE LATIDO ---
st.markdown("""
    <div class="logo-container">
        <div class="escudo-interactivo">🛡️</div>
    </div>
""", unsafe_allow_html=True)

# --- BASE DE DATOS SIMULADA ---
if "base_datos" not in st.session_state:
    st.session_state.base_datos = []

# --- FUNCIÓN DE INTELIGENCIA ARTIFICIAL (Simulación NLP) ---
def analizar_reporte_ia(texto):
    texto_min = texto.lower()
    palabras_amenaza = ["matar", "golpear", "pegar", "amenaza", "veras", "cuidate", "extorsion", "plata", "dinero"]
    palabras_imagen = ["foto", "video", "imagen", "publicar", "compartir", "desnudo", "pack", "redes"]
    palabras_insulto = ["feo", "tonto", "gordo", "estupido", "idiota", "raro", "burlar", "grupo", "ws", "chat"]
    
    clasificacion = "Acoso Verbal / General"
    riesgo = "BAJO"
    
    tiene_amenaza = any(p in texto_min for p in palabras_amenaza)
    tiene_imagen = any(p in texto_min for p in palabras_imagen)
    tiene_insulto = any(p in texto_min for p in palabras_insulto)
    
    if tiene_amenaza:
        clasificacion = "Amenazas Coactivas / Extorsión"
        riesgo = "ALTO"
    elif tiene_imagen:
        clasificacion = "Difusión de imágenes sin consentimiento"
        riesgo = "ALTO"
    elif tiene_insulto:
        clasificacion = "Insultos y Difamación"
        riesgo = "MEDIO"
        
    return clasificacion, riesgo

# --- DISEÑO VISUAL DE LA PÁGINA ---
st.markdown("<h1 style='text-align: center; margin-bottom: 0px;'>Proyecto Bullying Not Found</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7A685C; font-size: 16px;'>Tu espacio seguro, confidencial y amigable contra el acoso en redes sociales.</p>", unsafe_allow_html=True)

st.markdown("---")

# Formulario de Reporte
st.write("### 📝 Cuéntanos qué está pasando")
st.write("<small style='color: #8A766A;'>No tienes que decir tu nombre. Tu reporte es 100% secreto y seguro.</small>", unsafe_allow_html=True)

texto_usuario = st.text_area("", placeholder="Escribe aquí con total confianza... Ej. 'Un grupo me sacó de un chat y están usando mis fotos para burlarse de mí...'")

evidencia = st.file_uploader("📂 Si tienes capturas de pantalla, mensajes o pruebas, súbelas aquí:", type=["png", "jpg", "jpeg"])

if st.button("🛡️ Enviar reporte de forma segura"):
    if texto_usuario.strip() == "":
        st.error("Por favor, escribe un poco sobre la situación para poder ayudarte.")
    else:
        tipo_acoso, nivel_riesgo = analizar_reporte_ia(texto_usuario)
        
        nuevo_caso = {
            "fecha": str(datetime.date.today()),
            "denuncia": texto_usuario,
            "categoria": tipo_acoso,
            "riesgo": nivel_riesgo,
            "estado": "Notificado a Psicología (Pendiente de intervención)"
        }
        st.session_state.base_datos.append(nuevo_caso)
        
        st.success("🔒 ¡Reporte enviado con éxito! Nadie en tu salón sabrá que lo enviaste tu.")
        
        st.markdown("---")
        
        # --- NUEVOS TEXTOS EMPÁTICOS DEL ROBOT GUARDIÁN ---
        st.write("### 🤖 Tu Consejero Virtual: Guardián")
        
        if nivel_riesgo == "ALTO":
            st.markdown(f"""
                <div class="tarjeta-guardian" style="border-left-color: #FF6B6B;">
                    <h4 style="color: #D32F2F !important; margin-top:0;">⚠️ Alerta de Seguridad Activada</h4>
                    <p style="color: #4A3B32;"><b>¡Hola! Aquí Guardián.</b> Escúchame bien: <b>lo que te está pasando NO es tu culpa</b> y no tienes por qué aguantarlo en silencio. Estás a salvo aquí.</p>
                    <p style="color: #4A3B32;">Hagamos esto juntos ahora mismo para protegerte:</p>
                    <ul>
                        <li><b>No borres nada:</b> Esas capturas son tu escudo. Guardas todas las pruebas posibles.</li>
                        <li><b>Bloquea sin miedo:</b> Restringe a esas cuentas de inmediato de tus redes sociales.</li>
                        <li><b>Respira hondo:</b> Ya le avisé en secreto a la psicóloga del colegio. Ella va a intervenir de forma segura para frenar esto sin ponerte en evidencia ante tus compañeros.</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="tarjeta-guardian" style="border-left-color: #FFB399;">
                    <h4 style="color: #5D4A3E !important; margin-top:0;">ℹ️ Análisis del Escudo Terminado</h4>
                    <p style="color: #4A3B32;"><b>¡Hola! Aquí Guardián.</b> Eres muy valiente por haber escrito esto hoy. Quiero que recuerdes algo importante: las palabras feas o las burlas en internet de los demás <b>no definen quién eres tú</b>.</p>
                    <p style="color: #4A3B32;">Te sugiero seguir estos pasos amigables:</p>
                    <ul>
                        <li><b>Cierra el chat:</b> No te quedes leyendo mensajes que te hacen daño. Apaga la pantalla un rato.</li>
                        <li><b>Ignora y junta pruebas:</b> No les respondas con más insultos, eso es lo que ellos buscan. Mejor toma captura y déjalos hablando solos.</li>
                        <li><b>Apóyate en tu gente:</b> Cuéntale a tus papás o a un profesor en el que confíes. La psicóloga del colegio también recibió tu reporte y revisará cómo ayudarte de forma discreta.</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

# --- PANEL EXCLUSIVO PARA LA PSICÓLOGA ---
st.markdown("---")
st.write("### 🔑 Acceso Restringido: Personal Autorizado")
password = st.text_input("Contraseña de la Psicóloga Escolar:", type="password")

if password == "psico123":
    st.write("#### 📂 Casos Recibidos en Tiempo Real (Bandeja de Entrada)")
    if len(st.session_state.base_datos) == 0:
        st.write("No hay reportes nuevos. El ambiente escolar está tranquilo.")
    else:
        for idx, caso in enumerate(st.session_state.base_datos):
            with st.expander(f"Caso #{idx + 1} - Riesgo: {caso['riesgo']} ({caso['fecha']})"):
                st.write(f"**Clasificación de la IA:** {caso['categoria']}")
                st.write(f"**Detalle de la denuncia:** {caso['denuncia']}")
                st.write(f"**Estado institucional:** {caso['estado']}")
                if st.button(f"Activar Protocolo de Convivencia (Caso #{idx + 1})"):
                    st.success("Protocolo activado: Citación a padres y entrevista de protección agendada.")
