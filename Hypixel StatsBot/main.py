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
                if 'text' != "":
                    data = bot.getadata(text)
                    playerKarma= str(data['player']['karma'])
                    playerData = str(data['player'])
                    bot.sendMessage(chat_id, "karma del giocatore: "+text+" è pari a: "+playerKarma)

        time.sleep(5)

        # L'api key scadrà il: 03/06/2024
        # Lapi non permette di eseguire ricerche sullo stesso giocatore in un intervallo di tempo troppo breve
