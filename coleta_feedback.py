import csv
import smtplib, ssl
from email.message import EmailMessage
from datetime import datetime, timedelta


MY_EMAIL = "xxxxxxxxxxxxxx"
MY_PASSWORD = "xxxxxxxxxxxxxxxxxx"
FEEDBACK_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScJB-uUfSZyStgbO59oZDpY77zwGk4fpNfBehJpaaV5RKSv-Q/viewform?usp=publish-editor"  # ex.: link do Google Forms
REMETENTE_NOME = "Empresa X"
CSV_PATH = "sales.csv"


def send_feedback_email(name: str, email: str, order_id: str):
    assunto = f"Como foi sua experiência com a Empresa X? (Pedido {order_id})"

    texto = (
        f"Olá {name},\n\n"
        "Tudo bem? Gostaríamos de saber como foi sua experiência no processo de compra.\n"
        "Você pode nos avaliar rapidamente neste link:\n"
        f"{FEEDBACK_FORM_URL}\n\n"
        "Sua opinião é muito importante para melhorarmos nosso atendimento.\n"
        "Obrigado!\n"
        f"{REMETENTE_NOME}"
    )

    html = f"""
    <div style="font-family:Arial,Helvetica,sans-serif;line-height:1.5">
      <p>Olá <strong>{name}</strong>,</p>
      <p>Esperamos que esteja tudo certo com o seu pedido <strong>{order_id}</strong> </p>
      <p>
        Você poderia avaliar sua experiência com nosso atendimento?
        Leva menos de 1 minuto:
      </p>
      <p style="margin:16px 0">
        <a href="{FEEDBACK_FORM_URL}" target="_blank"
           style="background:#0b5; color:#fff; padding:12px 18px; text-decoration:none; border-radius:6px; display:inline-block;">
           Avaliar atendimento
        </a>
      </p>
      <p style="font-size:14px;color:#555">
        Se preferir, responda a este e-mail com seus comentários.
      </p>
      <hr style="border:none;border-top:1px solid #eee;margin:16px 0" />
      <p style="font-size:12px;color:#777">
        Obrigado!<br/>
        {REMETENTE_NOME}
      </p>
    </div>
    """

    msg = EmailMessage()
    msg["Subject"] = assunto
    msg["From"] = f"{REMETENTE_NOME} <{MY_EMAIL}>"
    msg["To"] = email


    msg.set_content(texto)
    msg.add_alternative(html, subtype="html")

    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as conn:
        conn.starttls(context=context)
        conn.login(MY_EMAIL, MY_PASSWORD)
        conn.send_message(msg)
    print(f"[OK] Enviado para {name} <{email}> (pedido {order_id})")

def is_delivered_yesterday(date_str: str) -> bool:

    delivered = datetime.strptime(date_str, "%Y-%m-%d").date()
    hoje = datetime.now().date()
    ontem = hoje - timedelta(days=1)
    return delivered == ontem

def main():
    total, enviados = 0, 0
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            name = row["name"].strip()
            email = row["email"].strip()
            order_id = row["order_id"].strip()
            delivered_at = row["delivered_at"].strip()

            if is_delivered_yesterday(delivered_at):
                try:
                    send_feedback_email(name, email, order_id)
                    enviados += 1
                except Exception as e:
                    print(f"[ERRO] {email}: {e}")

    print(f"Concluído. {enviados}/{total} e-mails enviados.")

if __name__ == "__main__":
    main()
