import requests,os
from pyfiglet import Figlet
import os

def display():
        f = Figlet()
        text = f.renderText('Gcosx . Js')
        console_width = os.get_terminal_size().columns
        lines = text.split('\n')
        max_line_length = max(len(line) for line in lines)
        margin = (console_width - max_line_length) // 2
        for line in lines:
            print(' ' * margin + line)
def gen_email(n=0):
    response = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=10')
    if response.status_code == 200:
                emails = response.json()
                return emails[0]
        

def cutter(email='domen@domain.com'):
    domen = email[:email.find('@')]
    domain = email[(email.find('@')+1):]
    return domen,domain

def get_mailbox(domen,domain):
    response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={domen}&domain={domain}')
    if response.status_code==200:
        mailbox = response.json()
        return mailbox
def w_msg_id(domen,domain,id):
    response = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={domen}&domain={domain}&id={id}')
    if response.status_code==200:
        mailbox = response.json()
        return mailbox
display()
while True:
    try:
        query = int(input('1.Generate Email\n\n2.MailBox\n\n3.Mailbox with msg ID\n\n4.Clear Terminal\n\n5.Quit\n\n>> '))
        if query==1:
            print(('-'*50),'\n','Generated Email :',gen_email())
            print('-'*50)
        elif query==2:
            email = cutter(input('Enter your tempmail : '))
            data = get_mailbox(email[0],email[1])
            if not data:
                print('-'*18)
                print('Mailbox is empty.')
                print('-'*18)
            else:
                for i in data:
                    print('\n\n\n')
                    for j in i:
                        print('\t\t',j,':',i[j])
                    if len(data)==1:
                        print('\n\n\n')
        elif query==3:
            email = cutter(input('Enter your tempmail : '))
            id = input('Message ID : ')
            data = w_msg_id(email[0],email[1],id)
            print('\n\n\n')
            for i in data:
                if i=='body' or i=='htmlBody':
                    continue
                if not data[i]:
                    print('\t\t',i,'>> Empty')
                    continue
                print('\t\t',i,':',data[i])
            print('\n\n\n')
        elif query==4:
            os.system('cls')
            display()
        elif query==5:
            break
        else:
            print('-'*35)
            print('Incorrect choose,please try again!')
            print('-'*35)
    except Exception as e:
        print('-'*50)
        print('System has stopped. Please check your steps.\nError :',e)
        print('-'*50)

                                                                  
