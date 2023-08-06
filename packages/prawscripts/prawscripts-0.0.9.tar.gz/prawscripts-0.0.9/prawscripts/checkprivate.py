def checkprivate(instance):
    """
    Script to check if sub is privated.

    Parameters
    ----------
    instance : PRAW Reddit Instance
        The name of the PRAW Instance

    Returns
    -------
    A list of subs that are privated

    Original Script
    ---------------
    for subreddit in reddit.redditor(str(reddit.user.me())).moderated():
        if (subreddit.subreddit_type == 'private'):
            print (subreddit.display_name, " ", subreddit.subreddit_type)
    """
    return [f"{sub.display_name}"
            for sub in instance.redditor(str(instance.user.me())).moderated()
            if (sub.subbredit_type == "private")]