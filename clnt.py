def ScktClient():
    from socket import socket,AF_INET,SOCK_DGRAM
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    print("If you did not execute server file this is not going to work."
          "Do not pay attention this message if you have already executed the server file. ")
    message = str.encode(input("Type your input in lowercase:"))
    clientSocket.sendto(message,(serverName,serverPort))
    message, clientAddress = clientSocket.recvfrom(2048)
    print("Last form of your input is: " + message.decode("utf-8"))
    clientSocket.close()


if __name__ == '__main__':
    ScktClient()