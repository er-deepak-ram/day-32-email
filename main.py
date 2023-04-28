import smtplib

my_email = "deepak.kumar2305@gmail.com"
password = "zgvkrwjgikynbwyw"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="nightrider.180@gmail.com", msg="Subject:Email from Python "
                                                                                     "code\n\nHello world")
