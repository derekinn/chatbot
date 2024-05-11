import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext

GOOGLE_API_KEY = "AIzaSyBw8yTii6UGtM9iQ15N1jCRsn79c7kDICw"  # Substitua pela sua API KEY
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

safety_settings = {
    "harassment": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)
chat = model.start_chat(history=[])

def enviar_mensagem():
    mensagem = caixa_entrada.get("1.0", tk.END).strip()
    caixa_entrada.delete("1.0", tk.END)
    if mensagem:
        caixa_conversa.config(state="normal")
        caixa_conversa.insert(tk.END, "Você: " + mensagem + "\n\n", "usuario")
        caixa_conversa.config(state="disabled")

        resposta = chat.send_message(mensagem)
        caixa_conversa.config(state="normal")
        caixa_conversa.insert(tk.END, "Botzin: " + resposta.text + "\n\n", "bot")
        caixa_conversa.config(state="disabled")
        caixa_conversa.see(tk.END)

janela = tk.Tk()
janela.title("Chatbot com Gemini Pro")
janela.config(bg="#202124")  # Fundo escuro

caixa_conversa = scrolledtext.ScrolledText(janela, state="disabled", bg="#202124", fg="white", font=("Helvetica", 12), wrap=tk.WORD)
caixa_conversa.tag_configure("usuario", foreground="#8AB4F8")
caixa_conversa.tag_configure("bot", foreground="#F1F3F4")
caixa_conversa.pack(pady=10, padx=10, expand=True, fill="both")

caixa_entrada = tk.Text(janela, height=3, bg="#303134", fg="white", font=("Helvetica", 12), insertbackground="white", bd=0)
caixa_entrada.pack(pady=10, padx=10, fill="x")

botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem, bg="#444649", fg="white", relief=tk.FLAT, font=("Helvetica", 10))
botao_enviar.pack(pady=(0, 10))

janela.bind("<Return>", lambda event: enviar_mensagem())
janela.mainloop()