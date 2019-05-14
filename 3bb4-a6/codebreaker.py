def codebreaker(server, username):
        
    MAXATTEMPTS = 12
    ATTEMPT = 1
    Aux = []
    S = []

    server.newGame(username)

    for i in Colors:
        for j in Colors:
            for k in Colors:
                for l in Colors:
                    S.append((i, j, k, l))
    
    guess = ('red', 'red', 'green', 'green')

    while True:
        
        if ATTEMPT <= MAXATTEMPTS:
            
            if server.guessCode(username, guess) == "win":
                return print("%s, %s" % (username, ATTEMPT))
            
            else:
                pegs = server.guessCode(username, guess)
                
                for s in S:
                    black = sum(s == g for s, g in zip(guess, s))
                    white = sum(min(guess.count(c), s.count(c)) for c in Colors) - black
                    s_pegs = [black, white]
                    if pegs != s_pegs:
                        Aux.append(s)
                        
                for a in Aux:
                    if len(S) != 0 and S.count(a) > 0:
                        S.remove(a)
                        
                if len(s) != 0:
                    guess = choice(S)
                    
                ATTEMPT = ATTEMPT + 1
        
        else:
            return print("%s has lost" % username)