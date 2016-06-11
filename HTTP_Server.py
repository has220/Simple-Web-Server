#--------------------------Program Description----------------------------#
'''
 This program simulates a simple web server in python. It introduces the 
 basics of socket programming with TCP connections. At the top of the code 
 is the definitions for libraries, next is the client_thread function
 and third is the main function. 
 '''

'''
To execute the code, place HTTP_Server.py and HelloWorld.html in the same directory
on secure shell. Then in the secure shell terminal, type: python HTTP_Server.py 12000
to run the program. 
'''




#----------------------------library declarations--------------------------------#
from socket import *       #import everything from socket library
import threading           #import threading library 





#-----------------------main thread, continue communication with client------------------------#

def main():
    
    serverHost = ''        #deal with various hosts
    serverPort = 12000     #random port number
    
    #create TCP serverSocket object ("Welcome" socket)
    serverSocket = socket(AF_INET, SOCK_STREAM)  

    #Prepare a server socket

    serverSocket.bind((serverHost, serverPort))  #bind socket to address and port

    serverSocket.listen(1)                       #listen for incoming connections 

    
    #start the live server
    while True:
    
    
        #Estabilish the connection
        print("Ready to serve...")
    
        #accept connections
        connSocket, address = serverSocket.accept()    
    
    
        #instantiate thread with target and arguments
        t = threading.Thread(target=next_client, args=(connSocket, address))
        
        #start threading clients
        t.start()
        
        
        #clients information (ip address and port number)
        print("Now connected to the following client (Address:Port)---> " + 
        address[0] + ":" + str(address[1]) + "\n")
    


  
        
    #close the server socket        
    serverSocket.close()










#----------------function for threading multiple clients ----------------------#

def next_client(connectionSocket, addr):
  
    
    try:
        

        #receive data on the connectionSocket
        message = connectionSocket.recv(1024)   
           


        #check if the file is empty
        if message == "":
            
        
            #close the client socket
            connectionSocket.close()
            
           

           
       
        #if the file is not empty
        else:
            
            #open file for reading and obtain its contents
            filename = message.split()[1]
        
            f = open(filename[1:]) 
        
            outputdata = f.read()
            
            #close the file after reading its contents
            f.close()
            
        
            #Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
        
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
        
                connectionSocket.send(outputdata[i])
                
     
            
            
        
        
        
        
        #close client socket
        connectionSocket.close()
        
        
      
        
        
        
    #catch error that occurs when the requested file is not at the server     
    except IOError:
    
        #Send response message for file not found
        connectionSocket.send("404 ERROR: FILE NOT FOUND\r\n\r\n")
       
            
        #Close client socket
        connectionSocket.close()
        
       
                
        
        
#---------------Call main function to begin program execution--------------#      
main()        
    