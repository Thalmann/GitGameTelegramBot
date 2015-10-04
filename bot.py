import requests
import time
import TelegramAPI

old_update_id = TelegramAPI.load_update_id()
m = TelegramAPI.get_message(old_update_id)
update_id = old_update_id if m.empty else m.update_id

while True:   
    print("running")
    message = TelegramAPI.get_message(update_id)
    if not message.empty:
        print(message.text)
        print(message.message_id)
        user = message.from_
        print(user.first_name)
        print(user.last_name)
        print(user.id_)
        print(message.date)
        print(message.chat)
        print(message.update_id)
        #### What shall happen :::::


        ####        
        update_id += 1
        TelegramAPI.save_update_id(update_id)
    time.sleep(1)
