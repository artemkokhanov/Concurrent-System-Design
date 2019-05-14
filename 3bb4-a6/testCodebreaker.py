import xmlrpc.client

#server = xmlrpc.client.ServerProxy("http://jhub3.cas.mcmaster.ca:8049")
server = xmlrpc.client.ServerProxy("http://localhost:8000")

# Guesses are generated randomly and once a guess is used it is removed from the set of all possible options. My code is a
# interpretation of the Five-guess algorithm.
# https://en.wikipedia.org/wiki/Mastermind_(board_game)?fbclid=IwAR2GOGFX9tv5lM6p58o3mVpDwUaPV1w9dAOs3K4llK2QYVBWG_tkQooFvO8

def testCodebreaker(username):
    codebreaker(server, username)