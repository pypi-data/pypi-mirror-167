def getmodmailcount(instance):
    """
    Script gets modmail count across multiple subreddits under the assumption there are mail perms on all subreddits

    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of the PRAW instance

    Returns
    -------
    count_list
        A list of subs and their associated modmail count

    Original Script
    ---------------
    for subreddit in reddit.redditor(str(reddit.user.me())).moderated():
        x=0
        for convo in reddit.subreddit(subreddit.display_name).modmail.conversations(limit=1000):
            x=x+1
        if x>0:
            print (subreddit.display_name, x)
    """
    count_list = []

    for sub in instance.redditor(str(instance.user.me())).moderated():
        x = 0
        for convo in instance.subreddit(sub.display_name).modmail.conversations(limit=1000):
            x += 1

        if x > 0:
            count_list.append([sub.display_name, x])
    
    return count_list