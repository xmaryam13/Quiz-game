import socket
from threading import Thread
from tkinter import *



nickname = input("Enter your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))
print("Connected with the server...")


def  goAhead(self,name):
    self.login.destroy()
    self.name = name 
    rcv = Thread(target = self.receive)
    rcv.start()

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        self.login = Toplevel()
        self.login.title('Login')
        self.go = Button(self.login, text = 'CONTINUE',font='Helvetica 14 bold',command = lambda: self.goAhead(self.entryName.get()))
    
    def receive(self):
        while True:
            try:
                message = client.recv(2084).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass

            except:
                print('An error has occured')
                client.close()
                break

def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()

