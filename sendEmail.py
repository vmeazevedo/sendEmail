import smtplib

def send_Email():
    try:
        msgFrom = str(remetente)
        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
        smtpObj.ehlo()
        smtpObj.starttls()
        msgTo = str(destinatario)
        toPass = str(token)             # Realizar o procedimento: https://www.treinaweb.com.br/blog/enviando-email-com-python-e-smtp
        smtpObj.login(msgTo, toPass)
        
        # Criamos o payload da mensagem com os dados do dicionario criado anteriormente
        msg = """
        %s
        """ % (txt)
        
        # Realizamos o envio dos dados para o e-mail escolhido
        smtpObj.sendmail(msgTo,msgFrom,'Subject: PyMail\n{}'.format(msg))
        smtpObj.quit()
        print("Email enviado com sucesso!")
    except:
        print("Erro ao enviar e-mail")

remetente = str(input("Remetente: "))
destinatario = str(input("Destinatário: "))
token = str(input("Token: "))
txt = str(input("Digite o corpo do seu e-mail: "))
send_Email()
