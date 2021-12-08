goal = input("Dᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴀᴋᴇ ᴀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?")
answers = ["yes", "y", "yeah", "yep", "yup", "yea", "sure", "correct"]
if goal.lower() in answers:
    shopping_list = []
    item_number = int(input("Hᴏᴡ ᴍᴀɴʏ ɪᴛᴇᴍs ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?"))
    while item_number > 0:
        answer = input("Wʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?")
        shopping_list.append(answer)
        item_number -= 1
    add_more = input("Dᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴍᴏʀᴇ ɪᴛᴇᴍs ᴛᴏ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?")
    while add_more.lower() == "yes" or goal.lower() == "y":
        answer = input("Wʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?")
        shopping_list.append(answer)
        add_more = input("Dᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴍᴏʀᴇ ɪᴛᴇᴍs ᴛᴏ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ?")
    remove = input("Dᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀɴʏᴛʜɪɴɢ ғʀᴏᴍ ᴛʜᴇ ʟɪsᴛ?")
    if remove.lower() == "yes" or goal.lower() == "y":
        removed = input("Wʜᴀᴛ ɪᴛᴇᴍ ɪɴ ᴛʜᴇ ʟɪsᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴍᴏᴠᴇ?")
        for number in range(len(shopping_list)):
            if removed.lower() == shopping_list[number].lower():
                shopping_list.pop(number)
                break
    print("Yᴏᴜʀ sʜᴏᴘᴘɪɴɢ ʟɪsᴛ ʜᴀs:")
    for item in shopping_list:
        print(item)
else:
    print("OK, ʙʏᴇ!")