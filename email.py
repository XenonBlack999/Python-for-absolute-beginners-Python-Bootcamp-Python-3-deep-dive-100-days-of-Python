import smtplib

to = input("Enter the email of victim: ")
content = input("Enter the content of the email:\n")

def send_email(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # ✅ Fixed SMTP typo
        server.ehlo()  # ✅ Fixed eh10() typo
        server.starttls()  # Secure the connection
        
        # Securely store credentials instead of hardcoding them
        email = "your_email@gmail.com"
        password = "your_app_password"  # Use an app password, NOT your main password
        
        server.login(email, password)  # Login
        server.sendmail(email, to, content)  # Send email
        print("Email sent successfully!")
        
        server.quit()  # Close connection
    except Exception as e:
        print("Error:", e)

send_email(to, content)
