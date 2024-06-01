import requestHandler
import time

# init bot 
bot = requestHandler.rh()
lastUpdateId = None
# bot in funzione
while True:
    
    updates = bot.getUpdates(lastUpdateId)
    if updates['ok'] == False:
        print("errore telegram -> " + updates['description'])
    else:
        updates = updates['result']
        # se il messaggio non è vuoto
        if len(updates) > 0:
            # controllo se nel messaggio c'è il campo textol dire che  che vuil mesaggio è un testo e non una posizione o un'immagine
            if 'text' in updates[-1]['message']:
                text = updates[-1]['message']['text']
                chat_id = updates[-1]['message']['chat']['id']
                user_id = updates[-1]['message']['from']['id']
                lastUpdateId = updates[-1]['update_id'] + 1
                # avvio del bot
                if updates[-1]['message']['text'] != "/start":
                    data = bot.getadata(text)
                    try:
                        playerKarma = str(data['player']['karma'])
                    except:
                        playerKarma = "karma non trovato "
                    try:
                        bwEXP = str(data['player']['stats']['Bedwars']['Experience'])
                    except:
                        bwEXP = "bwEXP non trovata"
                    try:
                        dbwinstreak = str(data['player']['stats']['Bedwars']['winstreak'])
                    except:
                        dbwinstreak = "dbwinstreak non trovata"
                    try:
                        playerSocial = str(data['player']['socialMedia']['links']['YOUTUBE'])
                    except:
                        playerSocial = "social non trovati"

                    messaggio= "karma del giocatore: "+text+" è pari a: " + playerKarma +", \r\n bed wars EXP: "+ bwEXP +", \r\n bed wars winstreak: "+ dbwinstreak + " \r\n Social: "+ playerSocial
                    bot.sendMessage(chat_id, messaggio)
                else:
                    messaggio = "ciao, scrivimi il nome del player di cui vuoi sapere i dati"
                    bot.sendMessage(chat_id, messaggio)


        time.sleep(5)

        