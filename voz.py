# Instalar
# pip install SpeechRecognition
# pip install gTTS
# pip install playsound==1.2.2
# pip install PyAudio


# Importar librerias
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


# definimos la funcion para poder cachar el operador
def recognise():
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=5)
    try:
        sp = r.recognize_google(audio,language='es-ES')
        # tan facil como castear la voz a un entero
        s = int(sp)
        print("Tu dijiste ", s)
        return s
    except Exception as e:
        print(e)
        print("No pude escuchar, repitelo")
        return recognise()


# Declaramos el reconocedor
r = sr.Recognizer()

# Activar el microfono como recurso que estara permanentemente en escucha
with sr.Microphone(device_index=0) as source:
    print('Identificate')
    # Guardamos lo que ha escuchado el microfono en variable
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, phrase_time_limit=5.0)

    # Iniciar una excepcion
    try:
        # Con el reconocedor de google pasamos el audio a texto
        aud_text = r.recognize_google(audio, language='es-ES')

        # Si el texto es igual a la contrasena
        if aud_text == 'Hola':
            # Damos bienvenida
            print('Bienvenido usuario')
            print(
                'Cual es la operacion que desea realizar? SUMA, RESTA, MULTIPLICACION O DIVISION?')
            # Convertir de texto a audio y guardamos el archivo mp3
            tts = gTTS(
                'Bienvenido usuario, Cual es la operaciOn que desea realizar? SUMA, RESTA, MULTIPLICACION O DIVISION?', lang='es-ES')
            tts.save('bienvenida.mp3')
            # Reproducimos el archivo mp3
            playsound('C:/Users/dazae/OneDrive/Escritorio/bienvenida.mp3')

            # Generamos un nuevo recurso de audio
            audio2 = r.listen(source, phrase_time_limit=5.0)
            operacion = r.recognize_google(audio2, language='es-ES')

            print('La operacion seleccionada fue: {}'.format(operacion))
            tts = gTTS('La operacion seleccionada fue', lang='es-ES')
            tts.save('operacionSeleccionada.mp3')
            playsound('C:/Users/dazae/OneDrive/Escritorio/operacionSeleccionada.mp3')

            # EJECUTAR LA OPERACION CON ALGUNAS CONDICIONES
            # SOLICITAR NUMERO 1 Y NUMERO 2

            if operacion == 'suma':
                with sr.Microphone() as source:
                    print('Dime el primer numero: ')
                num1q = recognise()

                print('Dime el segundo numero: ')
                num2q = recognise()

                rSuma = num1q+num2q
                print("El resultado de la suma es: ", rSuma)
               

                tts = gTTS('El resultado de la suma es' + rSuma, lang='es-ES')
                tts.save('operacionSuma.mp3')
                playsound('C:/Users/dazae/OneDrive/Escritorio/operacionSuma.mp3')

            elif operacion == 'resta':
                with sr.Microphone() as source:
                    print('Dime el primer numero: ')
                num1q = recognise()

                print('Dime el segundo numero: ')
                num2q = recognise()

                rResta = num1q-num2q
                print("El resultado de la resta es: ", rResta)
                

                tts = gTTS('El resultado de la resta es' +rResta, lang='es-ES')
                tts.save('operacionResta.mp3')
                playsound('C:/Users/dazae/OneDrive/Escritorio/operacionResta.mp3')

            elif operacion == 'multiplicación':
                
                with sr.Microphone() as source:
                    print('Dime el primer numero: ')
                    num1q = recognise()

                    print('Dime el segundo numero: ')
                    num2q = recognise()

                    m=num1q*num2q
                    print("El resultado de la multiplicacion es: ", m)
                

                    tts = gTTS('El resultado de la suma es'+m, lang='es-ES')
                    tts.save('operacionMultiplicacion.mp3')
                    playsound('C:/Users/dazae/OneDrive/Escritorio/operacionMultiplicacion.mp3')

            elif operacion == 'división':
                
                with sr.Microphone() as source:
                    print('Dime el primer numero: ')
                num1q = recognise()

                print('Dime el segundo numero: ')
                num2q = recognise()

                resta = num1q/num2q
                print("El resultado de la division es: ", resta)
     

                tts = gTTS('El resultado de la suma es' +
                           resta, lang='es-ES')
                tts.save('operacionSeleccionada.mp3')
                playsound('C:/Users/dazae/OneDrive/Escritorio/operacionSeleccionada.mp3')

            # DECIR POR VOZ EL RESULTADO
        else:
            print('Acceso denegado, tu dijiste: {}'.format(aud_text))
            tts = gTTS('Acceso denegado, tu dijiste:', lang='es-ES')
            tts.save('accesoDenegado.mp3')
            playsound('C:/Users/dazae/OneDrive/Escritorio/acceso.mp3')
    except:
        print('Lo siento, no puedo escucharte')