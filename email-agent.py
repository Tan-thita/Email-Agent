from tkinter import *
import smtplib
import easyimap
from tkinter import messagebox
from email.mime.text import MIMEText

class Mainlogin():
    """docstring for login"""
    def __init__(self):
        top = Tk()
        top.title("Login")
        frame = Frame(top)
        logobj = log()
        logobj.loginfncn(top)
        top.mainloop()
        
class log():
    def loginfncn(self, Frame):
        def login_fncn():
            smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
            smtp_ssl_port = 465
            if(eid_entry.get() == "" and pw_text.get() == ""):
                msg = messagebox.showinfo( "login Dialoge", "Please enter Email and Password!!")
                pass
            else:
                username = eid_entry.get()
                password = pw_text.get()

                try:
                    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
                    server.login(username, password)
                except smtplib.SMTPAuthenticationError:
                        msg = messagebox.showinfo( "login Dialoge", "Invalid Email/Password, Try entering again\nIf the problem persists then try Disabling the 2-Factor-Authentication and Secure-Login of your account")
                        #addmore exceptions based on condition like 2FactorAuthentication
                except Exception as e:
                    msg = messagebox.showinfo( "login Dialoge", e)
                else:
                    msg = messagebox.showinfo( "login Dialoge", "Login Success!!")
                    top2 = Tk()
                    Frame.destroy()
                    server.quit()
                    sendobj = send()
                    sendobj.sendmail(top2, username, password)   #terminating connection
        eid_label = Label(Frame , text = "E - Mail:", relief = RAISED )
        eid_label.place(x = 5, y = 5)
        eid_entry = Entry(Frame, bd = 5, width = 30)
        eid_entry.place(x = 79, y = 5)
    
        pw_label = Label(Frame , text = "Password:", relief = RAISED )
        pw_label.place(x = 5, y = 35) #diff of y is 35ppx per control
        pw_text = Entry(Frame, bd = 5, show = "*")
        pw_text.place(x = 79, y = 35)

        send_btn = Button(Frame, text = "Login", fg = "black", activebackground = "black", activeforeground = "white", command = login_fncn)
        send_btn.place(x = 100, y = 70)
        
        Frame.geometry("350x120")
    
class send():
    def sendmail(self, Frame, username, password):
        '''function containing the whole sendmail gui and its resp fncns'''
        Frame.title("Send Mail")
        Frame.geometry('600x700')
        def Send_btn_fncn():
            smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
            smtp_ssl_port = 465
            sender = username
            targets = to_entry.get()
    
            if(to_entry.get()=="" and sub_entry.get()==""):
                msgb = messagebox.showinfo( "Sending Mail Dialoge", "please Enter 'TO:' and 'Subject:' feilds")
            else:
                msg = MIMEText(msg_text.get("1.0",'end-1c'))
                msg['To'] = to_entry.get()
                msg['From'] = sender
                msg['Cc'] = cc_entry.get()
                msg['Bcc'] = bcc_entry.get()
                msg['Subject'] = sub_entry.get()
                try:
                    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
                    server.login(username, password)
                    server.sendmail(sender, targets, msg.as_string())
                    to_entry.delete(0, 'end')
                    bcc_entry.delete(0, 'end')
                    sub_entry.delete(0, 'end')
                    msg_text.delete('1.0', END)
                    successlbl = Label(Frame, text = "Mail Sent!")
                    successlbl.place(x = 200, y = 595)
                except Exception as e:
                    msgb = messagebox.showinfo( "Sending Mail Dialoge", e)
                else:
                    server.quit()

        def logout_btn_fncn():
            smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
            smtp_ssl_port = 465
            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.quit()
            Frame.destroy()
            a = Mainlogin()

        def read_btn_fncn():
            smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
            smtp_ssl_port = 465
            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.quit()
            top3 = Tk()
            new = read_email()
            new.read(top3, username, password)

        to_label = Label(Frame , text = "TO:", relief = RAISED )
        to_label.place(x = 5, y = 5)
        to_entry = Entry(Frame, bd = 5, width = 35)
        to_entry.place(x = 74, y = 5)

        from_label = Label(Frame , text = "FROM:", relief = RAISED )
        from_label.place(x = 5, y = 40)
        from_label2 = Label(Frame , text = username )
        from_label2.place(x = 74, y = 40)

        cc_label = Label(Frame , text = "CC:", relief = RAISED )
        cc_label.place(x = 5, y = 75)
        cc_entry = Entry(Frame, bd = 5, width = 35)
        cc_entry.place(x = 74, y = 75)

        bcc_label = Label(Frame , text = "BCC:", relief = RAISED )
        bcc_label.place(x = 5, y = 110)
        bcc_entry = Entry(Frame, bd = 5, width = 35)
        bcc_entry.place(x = 74, y = 110)

        sub_label = Label(Frame, text = "Subject:", relief = RAISED )
        sub_label.place(x = 5, y = 145)
        sub_entry = Entry(Frame, bd = 5, width = 42)
        sub_entry.place(x = 74, y = 145)

        msg_label = Label(Frame , text = "Message:", relief = RAISED )
        msg_label.place(x = 5, y = 180)                                                                 #diff of y is 35ppx per control
        msg_text = Text(Frame, height = 20, width = 50, wrap = WORD)
        msg_text.place(x = 74, y = 180)

        send_btn = Button(Frame, text = "Send Mail", fg = "black", activebackground = "black", activeforeground = "white", command = Send_btn_fncn)
        send_btn.place(x = 10, y = 595)

        send_btn = Button(Frame, text = "Logout", fg = "black", activebackground = "black", activeforeground = "white", command = logout_btn_fncn)
        send_btn.place(x = 500, y = 595)

        read_btn = Button(Frame, text = "Read Mail", fg = "black", activebackground = "black", activeforeground = "white", command = read_btn_fncn)
        read_btn.place(x = 500, y = 650)

class read_email():
    def read(self, Frame, username, password):
        def read_logic():
            try:
                if(no_entry.get()==""):
                    msgb = messagebox.showinfo( "Reading Mail Dialoge", "please Enter a valid number")
                else:
                    n = int(no_entry.get())
                    i = 1
            except Exception as f:
                msgb = messagebox.showinfo( "Reading Mail Dialoge", "please Enter a valid number")
            try:
                imapper = easyimap.connect('imap.gmail.com', username, password)
                for mail_id in imapper.listids(n):
                    mail = imapper.mail(mail_id)
                    #print(mail.from_addr)
                    #print(mail.title)
                    #print(mail.body)
                    if(mail.attachments):
                        a = 'Some Attachments'
                    else:
                        a = ''
                    messagebox.showinfo( "Mail "+str(i), "Mail From: "+mail.from_addr+"\nTitle: "+mail.title+"\nBody: "+mail.body+"\n"+a)
                    i = int(i)
                    i+=1
            except Exception as e:
                print(e)
            imapper.quit()
        def exit():
            Frame.destroy()
        read_label = Label(Frame , text = "Enter the Number of Emails you want to read: " )
        read_label.place(x = 5, y = 5)
        no_entry = Entry(Frame, bd = 5, width = 5)
        no_entry.place(x = 317, y = 5)

        read_btn = Button(Frame, text = "Read Email", fg = "black", activebackground = "black", activeforeground = "white", command = read_logic)
        read_btn.place(x = 10, y = 35)

        send_btn = Button(Frame, text = "Exit", fg = "black", activebackground = "black", activeforeground = "white", command = exit)
        send_btn.place(x = 100, y = 35)

        Frame.title("Read Email")
        Frame.geometry('400x100')

if __name__ == "__main__":
    a = Mainlogin()
