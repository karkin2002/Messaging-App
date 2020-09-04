import socket
from _thread import *
from chatClass import chatString
import pickle 


port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.0.1.188"
# host = socket.gethostname()

try:
    s.bind((host, port))

except socket.error as e:
    str(e)

s.listen()

print("Waiting for a connection, Server Started")

chat = chatString("Beginning of the chat...\n")

def threaded_client(conn, player):
    global chat
    conn.send(pickle.dumps(chat))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048*8))
            newMessage = data
            if newMessage.message != None:
                chat.message = chat.message + newMessage.message

                if len(chat.message.splitlines()) >= 350:
                    chatList = chat.message.splitlines(True)
                    chatList.remove(chatList[0])
                    chat.message = ""
                    for eachLine in chatList:
                        chat.message += eachLine



            if not data:
                print("Disconnected")
                break

            else:
                reply = chat 


                # print("Received: ", data)
                # print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0

while True:
    
    conn, addr = s.accept()  
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))

    currentPlayer += 1