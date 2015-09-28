import requests
import time
import TelegramAPI

old_update_id = TelegramAPI.load_update_id()
update_id = TelegramAPI.get_update_id(TelegramAPI.get_message(), old_update_id)

while True:   
    print "running"
    message = TelegramAPI.get_updates_message({"offset": update_id})
    if message[u"result"] != []:
        print TelegramAPI.get_text_message(message)
        chat_id = TelegramAPI.get_chat_id(message)
        #### What shall happen :::::


        ####        
        update_id += 1
        TelegramAPI.save_update_id(update_id)
    time.sleep(1)
