def checkbanstatus(instance, username):
    """
    Simple script that checks if someone is banned from any of your subs

    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of your PRAW instance
    username : str
        The name of the Redditor in question

    Returns
    -------
    sub_list
        A list of subs user is banned from

    Original Script
    ---------------
    for subreddit in reddit.redditor(str(reddit.user.me())).moderated():
        try:
            if any(reddit.subreddit(subreddit.display_name).banned(redditor="USERNAME")):
                print(subreddit.display_name)
        except:
            continue
    """
    sub_list = []

    for sub in instance.redditor(str(instance.user.me())).moderated():
        try:
            if any(instance.subreddit(sub.display_name).banned(redditor=username)):
                sub_list.append(sub.display_name)
        except:
            continue

    return sub_list