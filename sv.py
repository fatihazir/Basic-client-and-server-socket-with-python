def ScktServer():
    from socket import socket,AF_INET,SOCK_DGRAM
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("",serverPort))
    print("Server ready to receive message. Please send from client.")
    while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        print("Message has received to server. First appearance of the message is: " + message.decode("utf-8"))
        modifiedMessage = message.upper()
        serverSocket.sendto(modifiedMessage,clientAddress)


if __name__ == '__main__':
    ScktServer()



