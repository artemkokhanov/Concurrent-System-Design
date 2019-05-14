import xmlrpc.client

#server = xmlrpc.client.ServerProxy("http://jhub3.cas.mcmaster.ca:8049")
server = xmlrpc.client.ServerProxy("http://localhost:8000")

for i in range(len(server.topScores())):
    print(server.topScores()[i])