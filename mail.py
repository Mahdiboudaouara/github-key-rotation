import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(id):


    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        with open('./google_creds.txt', 'r') as file:
            sender_email = file.readline().strip()    
            sender_password = file.readline().strip() 
    except FileNotFoundError:
        print(f"Error: credentials file not found!")
        exit(1)

    try:
        with open('./recipient_email.txt', 'r') as file:
            recipient_email = file.read()   
    except FileNotFoundError:
        print(f"Error: recipient email file not found!")
        exit(1)

    subject = f'GitHub SSH Key Rotation Notification - ID: {id}'

    body = f"""
    <html>
    <body>
        <p>Hello,</p>

        <p>This is a notification regarding the recent SSH key rotation performed for your GitHub account. 
        The old SSH key has been backed up, and a new key has been successfully generated and added to your GitHub account.</p>

        <p><strong style="color: #ff6347;">ID: {str(id)}</strong></p> <!-- Highlighted ID in red -->

        <p>If you encounter any issues or have questions, please feel free to reach out.</p>

        <p>Best regards,<br>
        Mahdi Boudaouara</p>
    </body>
    </html>
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add custom header with the ID
    msg['X-Custom-ID'] = str(id)  # Ensure ID is converted to string

    # Attach the HTML body to the email
    msg.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print('Email sent successfully.')

    except Exception as e:
        print(f'Error: {e}')

    finally:
        server.quit()
        