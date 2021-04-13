import aiohttp_jinja2
import smtplib, ssl, email


@aiohttp_jinja2.template('mail.html')
async def get_form(request):
    return {}

@aiohttp_jinja2.template('mail.html')
async def send(request):
    form = await request.post()
    Recipient = str(form['Recipient'])
    Subject = str(form['Subject'])
    Body = str(form['Body'])

    try:
        smtp_server = "smtp.gmail.com"
        port = 587
	#sender email adrees and password
        sender = "testemailid32@gmail.com"
        password = "narutotest12"
	#email subject and body
        message = """Subject:{}\n \n{}""".format(Subject, Body)

		#establishing connection with gmail server
        server = smtplib.SMTP(smtp_server,port)
        server.starttls() 
        #login into sender account
        server.login(sender, password)
        #send mail
        server.sendmail(sender, Recipient, message)
        return {'response' :'Email sent!'}
        
    except Exception:
        return {'response' : 'Error sending mail'}
