from socket import *



msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
server = "smtp.mail.yahoo.com"
port = 587
emailFrom = "simone0934567@yahoo.com"
emailTo = "prtyprnces95@yahoo.com"


#Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = (server, port)
#Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


#Send HELO command and print server response.
heloCommand = 'HELO Simone\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

#clientSocket.login('simone0934567@yahoo.com', 'Crazy4yhuu;')

#Send MAIL FROM command and print server response.
#Fill in start
fromCommand = 'MAIL FROM: ' + emailFrom + '\r\n'
clientSocket.send(fromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

#Fill in end


#Send RCPT TO command and print server response.
#Fill in start
rcptCommand = 'RCPT TO: ' + emailTo + '\r\n'
clientSocket.send(rcptCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Fill in end


# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)

#Fill in end



# Send message data.
# Fill in start
clientSocket.send(msg.encode())


# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)


# Fill in end


# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)              
# Fill in end
