from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def call_ui():
	def sendmail():
		smtp_ssl_host = 'smtp.gmail.com'
		smtp_ssl_port = 465
		username = 'xxxxxxxxxxxxx'
		password = 'xxxxxxxxxxxxxxxxxxxxxx'
		sender = 'xxxxxxxxxxxxxxxxxx'
		targets = to_entry.get()
		msg = MIMEMultipart()
		msg['To'] =to_entry.get()
		msg['From'] = sender
		msg['Cc'] = cc_entry.get()
		msg['Bcc'] = bcc_entry.get()
		msg['Subject'] = sub_entry.get()
		msg.attach(MIMEText(msg_text.get("1.0","end-1c"), 'plain'))
		attach_file_name = attach_entry.get()
		attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
		payload = MIMEBase('application', 'octate-stream')
		payload.set_payload((attach_file).read())
		encoders.encode_base64(payload) #encode the attachment
		#add payload header with filename
		payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
		msg.attach(payload)
		try:
			server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
			server.login(username, password)
			server.sendmail(sender, targets, msg.as_string())
		except Exception as e:
			print("error is: ", e)

	root = Tk()
	root.title("Compose Email")

	#controlls
	to_label = Label(root, text = "TO:")
	cc_label = Label(root, text = "CC:")
	bcc_label = Label(root, text = "BCC:")
	subject_label = Label(root, text = "Subject:")
	Attachments_label = Label(root, text = "Attachments:")
	msg_label = Label(root, text = "Message Body:")
	to_entry = Entry(root, width = 40)
	cc_entry = Entry(root, width = 40)
	bcc_entry = Entry(root, width = 40)
	sub_entry = Entry(root, width = 40)	
	msg_text = Text(root, wrap = WORD, height = 15, width = 45)
	#attach_button = Button(root, text = "Select File")
	attach_entry = Entry(root, width = 40)
	submit_btn = Button(root, text = "Send Mail", command = sendmail)


	#placeholder method
	to_label.place(x = 5, y = 5)
	to_entry.place(x = 35, y = 5)
	cc_label.place(x = 5, y = 30)
	cc_entry.place(x = 35, y = 30)
	bcc_label.place(x = 5, y = 55)
	bcc_entry.place(x = 40, y = 55)
	subject_label.place(x = 5, y = 80)
	sub_entry.place(x = 70, y = 80)
	Attachments_label.place(x = 5, y = 105)
	#attach_button.place(x = 100, y = 105 )
	attach_entry.place(x = 100, y = 105)
	msg_label.place(x = 5, y = 140)
	msg_text.place(x = 5, y = 165)
	submit_btn.place(x = 5, y = 480)

	root.geometry("500x550")
	root.mainloop()

if __name__ == "__main__":
	call_ui()