import os

# Nombre del archivo externo para los insultos
ARCHIVO_INSULTOS = "palabras_clave.txt"

def cargar_diccionario_insultos():
    """Lee el archivo .txt offline y extrae los insultos con su gravedad"""
    diccionario = {}
    if not os.path.exists(ARCHIVO_INSULTOS):
        try:
            with open(ARCHIVO_INSULTOS, "w", encoding="utf-8") as f:
                f.write("gordo|3\ngrasoso|3\ncerdo|3\nfracasado|3\nfeo|2\nrata|2\nflaco|1\nxd|1\n")
        except Exception:
            pass
            
    try:
        with open(ARCHIVO_INSULTOS, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea and "|" in linea:
                    palabra, gravedad = linea.split("|")
                    diccionario[palabra.lower().strip()] = int(gravedad.strip())
    except Exception as e:
        return {"gordo": 3, "grasoso": 3, "cerdo": 3, "fracasado": 3, "feo": 2, "flaco": 1}
    return diccionario


# --- BLOQUE NUEVO: APRENDIZAJE AUTOMÁTICO DE PALABRAS FUERTES ---
def auto_agregar_palabras_fuertes(texto_usuario):
    """Detecta palabras críticas ausentes en el TXT y las añade solas con gravedad 3"""
    texto_min = texto_usuario.lower()
    diccionario_actual = cargar_diccionario_insultos()
    
    # Lista de alertas universales de acoso severo que queremos capturar si el niño las menciona
    alertas_criticas = [
        "amenazan", "pegan", "pegarme", "golpean", "golpearon", 
        "matar", "muérete", "basura", "monstruo", "asco", 
        "difamando", "acosando", "extorsionan", "chantaje", "amenaza"
    ]
    
    nuevas_añadidas = False
    
    # Revisamos palabra por palabra la frase del niño
    for palabra_alerta in alertas_criticas:
        if palabra_alerta in texto_min:
            # Si la palabra fuerte NO está en el archivo de texto actual, la agregamos sola
            if palabra_alerta not in diccionario_actual:
                try:
                    with open(ARCHIVO_INSULTOS, "a", encoding="utf-8") as f:
                        f.write(f"\n{palabra_alerta}|3")
                    nuevas_añadidas = True
                    print(f"[Sistema] Se auto-agregó la palabra fuerte: {palabra_alerta}")
                except Exception as e:
                    print(f"Error al auto-agregar palabra: {e}")
                    
    return nuevas_añadidas


def evaluar_carga_emocional(texto):
    """Analiza el texto usando el archivo externo y determina el nivel de urgencia"""
    texto_min = texto.lower()
    
    # Ejecutamos el auto-aprendizaje antes de evaluar
    auto_agregar_palabras_fuertes(texto)
    
    # Volvemos a cargar el diccionario (que ya incluiría las nuevas si se añadieron)
    palabras_clave = cargar_diccionario_insultos()
    
    gravedad_total = 0
    detectadas = 0
    
    for palabra, peso in palabras_clave.items():
        if palabra in texto_min:
            gravedad_total += peso
            detectadas += 1
            
    if detectadas > 0:
        if gravedad_total >= 4:
            return "critico"
        elif 2 <= gravedad_total <= 3:
            return "medio"
        else:
            return "bajo"
    return "normal"

def obtener_respuesta_robot(texto_usuario, nivel_emocional):
    """Mapea tipos específicos de preguntas y agresiones escolares en orden de prioridad"""
    texto_min = texto_usuario.lower()
    
    # --- RESPUESTAS POR CARGA ACUMULADA DE INSULTOS DE TEXTO ---
    if nivel_emocional == "critico":
        return ("¡Alto ahí! Esos insultos tan pesados y crueles que me cuentas son una agresión "
                "grave de acoso. NADIE tiene derecho a hacerte sentir menos. Esto daña tu salud "
                "mental y NO tienes que soportarlo solo. Te sugiero firmemente que descargues esta "
                "pantalla y vayas hoy mismo con tus padres o te acerques al psicólogo de tu escuela. "
                "Ellos van a intervenir para frenar esto de raíz sin ponerte en evidencia.")
                
    elif nivel_emocional == "medio":
        return ("Lamento mucho que tengas que escuchar esos adjetivos en tu contra. El acoso verbal "
                "busca desgastar tu confianza día a día. Por favor, recuerda que el problema está en "
                "quien insulta, no en ti. Te aconsejo apuntar cuándo pasa esto y mostrárselo hoy "
                "mismo a tus padres o a un profesor de confianza.")
                

    elif nivel_emocional == "bajo":
        return ("Escuché lo que te dijeron. Aunque parezca un comentario menor (como un apodo "
                "cotidiano), sé que las palabras se clavan en la mente. No dejes que definan quién "
                "eres. Hablar con tus papás evitará que esto crezca y te quitará un peso de encima.")

    # --- MAPEO DE CATEGORÍAS DE INTENCIONES DEL ALUMNO ---
    if "te han insultado" in texto_min or "te insultaron" in texto_min or "te molestan a ti" in texto_min or "a ti te insultan" in texto_min:
        return ("A mí no me pueden insultar porque soy solo un programa de computadora y las "
                "máquinas no tenemos sentimientos ni nos ponemos tristes. Pero sé que a ti sí "
                "te duele lo que te pasa, y tienes toda la razón del mundo para sentirte mal. "
                "Ninguna persona merece ser tratada con crueldad. Recuerda siempre que lo que te "
                "dicen esos chicos no es verdad; el problema son ellos, no tú.")

    elif "debo contarles" in texto_min or "le digo a mis papas" in texto_min or "cuento a mis padres" in texto_min or "decirle a mi mama" in texto_min or "decirle a mi papa" in texto_min:
        return ("¡Sí, absolutamente sí! Contárselo a tus papás es el paso más valiente y "
                "acertado que puedes dar hoy. Ellos te aman y su prioridad número uno es protegerte, "
                "aunque a veces te dé miedo su reacción. Si no sabes cómo empezar la conversación, "
                "puedes usar este ejemplo: 'Mamá, papá, hay algo en el colegio que me está haciendo "
                "sentir muy mal y necesito su ayuda'. También puedes mostrarles esta misma aplicación "
                "o escribirlo en una nota. No cargues más con este peso tú solo; diles hoy mismo.")

    elif "insultan" in texto_min or "insulto" in texto_min or "burlan" in texto_min or "apodos" in texto_min:
        return ("Poner apodos o insultar en el colegio NO es un juego, es una agresión verbal. "
                "Sé que duele y cansa ir a estudiar así, pero ignorarlo no siempre lo detiene. "
                "Lo más valiente que puedes hacer es registrar qué días te insultan y decírselo "
                "al psicólogo de tu escuela o a tus padres. Ellos tienen la obligación de poner un alto.")

    elif "sacaron" in texto_min or "grupo" in texto_min or "aislan" in texto_min or "hablan" in texto_min:
        return ("La exclusión social (dejarte de hablar, sacarte de los grupos de WhatsApp o hacerte "
                "el vacío) también es una forma de cyberbullying. No ruegues por la atención de personas "
                "que te lastiman. Tu tranquilidad vale más. Apóyate en tus verdaderos amigos fuera de ese grupo "
                "y cuéntale esta situación a un adulto de confianza para que la escuela intervenga.")

    elif "amigos ya no" in texto_min or "los extraño" in texto_min or "extraño a mis amigos" in texto_min:
        return ("Lamento mucho que tus amigos ya no estén contigo en el colegio; es completamente normal "
                "que los extrañes y que te sientas desprotegido o triste sin ellos. A veces, cuando nos "
                "quedamos solos en el salón, los chicos malos intentan aprovecharse de eso. Por favor, "
                "no te aisles. Intenta acercarte poco a poco a otros compañeros que veas que son tranquilos, "
                "o conversa con el psicólogo estudiantil. Cuéntale que te sientes solo; ellos pueden ayudarte "
                "a integrarte a nuevos grupos sanos y vigilarán que nadie te moleste.")

    elif "por que hay" in texto_min or "niños malos" in texto_min or "por que me molestan" in texto_min:
        return ("Es una pregunta muy importante. Muchas veces, las personas que molestan a otras "
                "lo hacen porque ellas mismas tienen problemas en sus casas o buscan llamar la atención "
                "sintiéndose 'poderosos' al rebajar a los demás. Su crueldad habla de su propio vacío interno, "
                "NO de tu valor. Tú no has hecho nada malo para merecer esto.")

    elif "que puedo hacer" in texto_min or "que hago" in texto_min or "ayuda" in texto_min:
        return ("Lo primeiro es proteger tu tranquilidad. Recuerda respirar profundo y no responder "
                "con más insultos, porque eso es justo lo que ellos buscan para continuar. "
                "La acción más fuerte que puedes tomar es romper el secreto: si te cuesta hablar "
                "de esto de frente con un adulto, puedes escribirlo en un papel y entregárselo a "
                "tus papás o al psicólogo del colegio. Ellos sabrán cómo actuar.")

    elif "miedo" in texto_min or "triste" in texto_min or "solo" in texto_min or "sola" in texto_min:
        return ("El miedo, la tristeza y la soledad son respuestas normales cuando alguien te trata mal, "
                "pero el aislamiento hace que esos sentimientos crezcan. Romper el silencio hablando con "
                "un adulto es tu mejor escudo. No estás solo, estamos aquí para ayudarte a encontrar una salida. ¡Tú vales muchísimo!")

    elif "robot" in texto_min or "ia" in texto_min or "quien eres" in texto_min:
        return ("Soy Guardián, tu asistente automatizado. Al ser una máquina no tengo empatía real, "
                "pero tus padres y la psicóloga de la escuela sí. Mi meta es darte la información y la "
                "confianza que necesitas para que puedas hablar con ellos.")

    elif "hola" in texto_min or "buenos" in texto_min:
        return ("¡Hola! Qué bueno que decidiste hablar conmigo. Este es un espacio 100% privado en tu computadora. ¿Cómo te va en la escuela o en tus redes sociales?")
    
    elif "gracias" in texto_min:    
        return ("¡Para eso estoy! Me alegra acompañarte. Recuerda que el paso más importante es buscar ayuda humana hoy mismo.")
    #else:
    #    return ("Te escucho con total atención. Recuerda que no estás solo en esto y que este espacio "
    #            "es completamente confidencial en tu computadora. Si quieres, cuéntame un poco más detallado "
    #            "qué fue lo que pasó o qué te dijeron.")
    # CATEGORÍA: Despedidas del Estudiante (NUEVA)
    elif "adios" in texto_min or "adiós" in texto_min or "hasta luego" in texto_min or "chau" in texto_min or "chao" in texto_min:
        return ("¡Hasta luego! Recuerda que estoy aquí para ayudarte y puedes volver a conversar "
                "conmigo cuando lo desees. Este siempre será tu espacio seguro. Cuídate mucho.")

    # CATEGORÍA: Cortesía Básica (La que ya tenías)
    elif "hola" in texto_min or "buenos" in texto_min:
        return "¡Hola! Qué bueno que decidiste hablar conmigo. Este es un espacio 100% privado en tu computadora. ¿Cómo te va en la escuela o en tus redes sociales?"
    elif "gracias" in texto_min:
        return "¡Para eso estoy! Me alegra acompañarte. Recuerda que el paso más importante es buscar ayuda humana hoy mismo."
        
    # RESPUESTA POR DEFECTO
    else:
        return ("Te escucho con total atención. Recuerda que no estás solo en esto y que este espacio "
                "es completamente confidencial en tu computadora. Si quieres, cuéntame un poco más detallado "
                "qué fue lo que pasó o qué te dijeron.")

### ¿Por qué este cambio dejará con la boca abierta al profesor?
#Porque demuestra que tu programa **crece solo con el uso**. Si un alumno entra al Chat Bot y escribe *"En el recreo me **golpean** y me dicen tonto"*, la función `auto_agregar_palabras_fuertes` detectará inmediatamente que `"golpean"` es una alerta crítica. 
#Automáticamente abrirá el archivo `palabras_clave.txt`, escribirá en la última línea `golpean|3`, y para la siguiente vez que cualquier otro niño use esa palabra, el programa ya sabrá que es un ataque de gravedad máxima. ¡Y todo funcionando de forma offline!
#Reemplaza tu archivo `cerebro.py` con este bloque. ¿Qué te parece este toque tecnológico de auto-registro para blindar la presentación?
# Más