def searchmessageinboxkeyword(instance, keyword):
    """
    Script to search message inbox keyword

    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of the PRAW instance
    keyword : str
        The name of the word you're looking for in inbox
    """
    messages = []
    for message in instance.inbox.all(limit = None):
        if keyword in str(message.body) or keyword in str(message.subject):
            #print(message.body)
            messages.append(message.body)
    
    return messages;