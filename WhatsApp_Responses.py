def response(input_message):
    message = input_message.lower()
    if(message == "nice"):
        return "very nais"
    elif(message =="thanks"):
        return "No Problem"
    elif(message=="happy birthday"):
        return "Thank You"
    else:
        return "Ok, I'll check it out"
