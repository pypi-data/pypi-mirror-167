def searchmessageinboxkeyword(instance, keyword):
    """
    Script to search message inbox keyword

    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of the PRAW instance
    keyword : str
        The name of the word you're looking for in inbox

    Returns
    -------
    A list of messages from inbox with keyword

    Original Script
    ---------------
    for message in reddit.inbox.all(limit = None):
        if 'STRING' in str(message.body) or 'STRING' in str(message.subject):
            print(message.body)
    """
    return [message.body
            for message in instance.inbox.all(limit = None)
            if keyword in str(message.body) or keyword in str(message.subject)]