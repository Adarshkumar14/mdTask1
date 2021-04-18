import smtplib
import urlib.request as urlib
sender_email = "doniksingh@gmail.com"
message = "Testing is Successfull!!,app is going to prod world"
rec_email = "adarsh.adarshsingh12@gmail.com"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("doniksingh@gmail.com",""PaSS@1234)
server.sendmail("Adarsh singh","adarsh.adarshsingh12@gmail.com",message)

