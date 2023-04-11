from datetime import datetime

from datetime import date

from datetime import timedelta

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import smtplib

import ssl

import OpenSSL

import ssl

import os

import csv

sender = "your sender email id under these qoutes"

receiver = "your receiver email id under these qoutes"

password = "password under these qoutes"

today = date.today() + timedelta(days = 60)

ltdate = today.strftime("%Y/%m/%d")

lastdate = (datetime.strptime(ltdate, "%Y/%m/%d").date().isoformat() )  

urllist = "give full path of file if it is in another directory"

with open(urllist) as urls:

    for url in urls:

        try:

            url = url.strip()

            cert=ssl.get_server_certificate((url,443))

            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

            dat = x509.get_notAfter()

            expdat = dat.decode('utf-8')

            cnexpdat =  (datetime.strptime(expdat, '%Y%m%d%H%M%S%z').date().isoformat() )        

           

           

        except:

            pass

        if cnexpdat < lastdate:

                sub1 = 'SSL Expiry Alert For '

                sub2 = url

                message = MIMEMultipart()

                message["Subject"] = sub1 + sub2

                message["From"] = sender

                message["To"] = receiver              

                html1 = """\

                        <html>

                        <head>

                        <style>

                        BODY{background-color:white;}

                        TABLE{border-width: 1px;border-style: solid;border-color: black;border-collapse: collapse;}

                        TH{border-width: 1px;padding: 0px;border-style: solid;border-color: black;background-color:#00FF77;align:center;}

                        TD{border-width: 1px;padding: 4px;border-style: solid;border-color: black;background-color:#0089FF;color:white;align:center;}

                        </style>

                        </head>

                        <body>

                        <table style="width:100%">

                        <tr><th>Domain Name</th><th>Expiry Date</th></tr>

                        <tr><td align = center>

                        """

                html2 = url

                html3 = """\

                        </td><td align = center>

                        """

                html4 = datetime.strptime(cnexpdat, '%Y-%m-%d').strftime("%d-%B-%Y")

                html5 = """\

                        </td></tr>

                        </table>

                        </body>

                        </html>

                        """

                body = html1 + html2 + html3 + html4 + html5

                message.attach(MIMEText(body, 'html'))

                context = ssl.create_default_context()

                with smtplib.SMTP_SSL("your SMTP address under these quotes", 465, context=context) as server:

                    server.login(sender,password)

                    server.sendmail(

                        sender, receiver, message.as_string()

                    )


