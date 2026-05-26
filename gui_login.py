# gui_login.py
# LOGIN EDUCACIONAL - Tkinter + Terminal Hacker

import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import time

# =========================
# CONFIG
# =========================

USUARIO_REAL = "seven"
PASSWORD_REAL = "choi123"

MAX_INTENTOS = 3
TIEMPO_BLOQUEO = 15

IP_FALSA = "192.168.0.24"

intentos = 0
bloqueado_hasta = 0

# =========================
# LOGS
# =========================

def escribir_terminal(texto):
    terminal.insert(tk.END, texto + "\n")
    terminal.see(tk.END)


def guardar_log(usuario, password, resultado):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    linea = (
        f"[{fecha}] "
        f"IP: {IP_FALSA} | "
        f"USER: {usuario} | "
        f"PASS: {password} | "
        f"STATUS: {resultado}"
    )

    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea + "\n")

    escribir_terminal(linea)

# =========================
# LOGIN
# =========================

def login():

    global intentos
    global bloqueado_hasta

    # Verifica bloqueo
    if time.time() < bloqueado_hasta:
        restante = int(bloqueado_hasta - time.time())

        messagebox.showwarning(
            "Sistema bloqueado",
            f"Esperá {restante} segundos"
        )

        escribir_terminal(
            f"[!] LOGIN BLOCKED - {restante}s remaining"
        )

        return

    usuario = entry_usuario.get()
    password = entry_password.get()

    escribir_terminal("\n========================")
    escribir_terminal("[+] LOGIN ATTEMPT")
    escribir_terminal(f"[+] USER: {usuario}")
    escribir_terminal(f"[+] PASS: {password}")

    # Login correcto
    if usuario == USUARIO_REAL and password == PASSWORD_REAL:

        escribir_terminal("[+] ACCESS GRANTED")

        guardar_log(usuario, password, "SUCCESS")

        messagebox.showinfo(
            "Login",
            "Acceso concedido"
        )

        intentos = 0

    # Login incorrecto
    else:

        intentos += 1

        escribir_terminal("[-] ACCESS DENIED")
        escribir_terminal(
            f"[-] FAILED ATTEMPTS: {intentos}/{MAX_INTENTOS}"
        )

        guardar_log(usuario, password, "FAILED")

        messagebox.showerror(
            "Login",
            "Acceso denegado"
        )

        # Bloqueo
        if intentos >= MAX_INTENTOS:

            bloqueado_hasta = time.time() + TIEMPO_BLOQUEO

            escribir_terminal(
                f"[!] SYSTEM LOCKED {TIEMPO_BLOQUEO}s"
            )

            messagebox.showwarning(
                "Bloqueado",
                f"Demasiados intentos\n"
                f"Bloqueado {TIEMPO_BLOQUEO} segundos"
            )

            intentos = 0

# =========================
# GUI
# =========================

ventana = tk.Tk()

ventana.title("Secure Login Terminal")
ventana.geometry("700x500")
ventana.configure(bg="black")
ventana.resizable(False, False)

# =========================
# TITULO
# =========================

titulo = tk.Label(
    ventana,
    text="SECURE AUTH TERMINAL",
    bg="black",
    fg="lime",
    font=("Consolas", 20, "bold")
)

titulo.pack(pady=10)

# =========================
# FRAME LOGIN
# =========================

frame = tk.Frame(
    ventana,
    bg="black"
)

frame.pack(pady=10)

# Usuario
label_usuario = tk.Label(
    frame,
    text="Usuario",
    bg="black",
    fg="lime",
    font=("Consolas", 12)
)

label_usuario.grid(row=0, column=0, padx=10, pady=10)

entry_usuario = tk.Entry(
    frame,
    width=30,
    bg="#101010",
    fg="lime",
    insertbackground="lime",
    font=("Consolas", 12)
)

entry_usuario.grid(row=0, column=1)

# Password
label_password = tk.Label(
    frame,
    text="Contraseña",
    bg="black",
    fg="lime",
    font=("Consolas", 12)
)

label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(
    frame,
    show="*",
    width=30,
    bg="#101010",
    fg="lime",
    insertbackground="lime",
    font=("Consolas", 12)
)

entry_password.grid(row=1, column=1)

# Botón
boton = tk.Button(
    ventana,
    text="INICIAR SESION",
    command=login,
    bg="#111111",
    fg="lime",
    activebackground="black",
    activeforeground="lime",
    width=25,
    height=2,
    font=("Consolas", 11, "bold")
)

boton.pack(pady=15)

# =========================
# TERMINAL
# =========================

terminal = ScrolledText(
    ventana,
    width=80,
    height=15,
    bg="black",
    fg="lime",
    insertbackground="lime",
    font=("Consolas", 10)
)

terminal.pack(pady=10)

# Mensaje inicial
escribir_terminal("====================================")
escribir_terminal(" SECURE AUTH TERMINAL v1.0")
escribir_terminal("====================================")
escribir_terminal("[+] SYSTEM READY")
escribir_terminal(f"[+] FAKE IP: {IP_FALSA}")

# =========================
# START
# =========================

ventana.mainloop()
