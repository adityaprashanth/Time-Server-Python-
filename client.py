import socket 
import os
import tkinter as tk
import ssl

HOST ='127.0.0.1'
PORT =2121

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
ssl_sock = ssl_context.wrap_socket(clientSocket)

ssl_sock.connect((HOST,PORT))
print('Starting up GUI')

root = tk.Tk()
root.title('My Window')
root.geometry('500x300')

var = tk.StringVar()
l = tk.Label(root, bg='white', width=20, text='empty')
l.pack()
l.config(text='Enter your command:')
command = 'IND'

def print_selection():
	command = var.get()
	ssl_sock.sendall(command.encode())
	Data = ssl_sock.recv(1024).decode()
	lab.config(text=Data)
	if command == 'quit':
		print('Closing GUI')
		root.destroy()

r2 = tk.Radiobutton(root, text='United States of America -09:30', variable=var, value='USA', command=print_selection) # India is 9 hours and 30 minutes ahead of  USA
r2.pack()
r7 = tk.Radiobutton(root, text='Chile -08:30', variable=var, value='SA', command=print_selection) # India is 8 hours and 30 minutes ahead of chile
r7.pack()
r3 = tk.Radiobutton(root, text='United Kingdoms -05:30', variable=var, value='UK', command=print_selection) # india is 5 hours and 30 minutes ahead of UK
r3.pack()
r6 = tk.Radiobutton(root, text='Republic of South Africa -03:30', variable=var, value='RSA', command=print_selection) # India is 3 hours and 30 minutes ahead of South Africa
r6.pack()
r1 = tk.Radiobutton(root, text='India 00:00', variable=var, value='IND', command=print_selection)
r1.pack()
r5 = tk.Radiobutton(root, text='Japan +03:30', variable=var, value='JPN', command=print_selection) # japan is 3 hours and 30 minutes ahead of india
r5.pack()
r4 = tk.Radiobutton(root, text='Australia +05:30', variable=var, value='AUS', command=print_selection) #Australia is 5 hours and 30 minutes ahead of India
r4.pack()
r8 = tk.Radiobutton(root, text='QUIT', variable=var, value='quit', command=print_selection)
r8.pack()

lab = tk.Label(root, bg='white', width=20, text='empty')
lab.pack()

root.mainloop()
