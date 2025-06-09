import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from SE_pro_data import make_csv
import logging

logging.basicConfig(filename="SEpro.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def email_sender():
    try:
        make_csv()
        sender = "channafutras@gmail.com"
        receiver = sender
        smtps = "smtp.gmail.com"
        ps = "yvoi eeij rsvw vvbq"
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = "Crypto CSV email"
        message.attach(MIMEText("THE crypto email" , "plain"))
        with open("Crypto.csv" , "r") as f :
            attachment = MIMEApplication(f.read() , "csv")
        attachment.add_header("content-disposition" , "attachment" , filename="Crypto.csv")
        message.attach(attachment)
        server= smtplib.SMTP(smtps , 587)
        server.starttls()
        server.login(sender , ps)
        server.sendmail(sender, receiver, message.as_string())
        server.quit()
        logging.info("Email sent")
        print("Email sent")
    except Exception as e:
        logging.error(f"Exception in sending email : {e}")
        print(f"Exception in sending email : {e}")
    except TypeError or NameError or UnboundLocalError as e:
        logging.error(f"Error in sending email : {e}")
        print(f"Error in sending email : {e}")
          
        
