import smtplib
from email.message import EmailMessage

# Configurações
remetente = "seu email"
senha = ""
destinatario = "para qual email vai a mensagem"
assunto = "assunto"
mensagem = "mensagem"

# Criar a mensagem de e-mail
msg = EmailMessage()
msg['Subject'] = assunto
msg['From'] = remetente
msg['To'] = destinatario
msg.set_content(mensagem)

# Iniciar conexão com o servidor SMTP do Gmail
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    # Fazer login na conta do remetente
    server.login(remetente, senha)
    # Enviar e-mail
    server.send_message(msg)

print("E-mail enviado com sucesso para", destinatario)
