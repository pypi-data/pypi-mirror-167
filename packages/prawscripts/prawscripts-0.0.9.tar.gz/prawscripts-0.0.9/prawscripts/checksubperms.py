def checksubperms(instance):
    """
    Script to check the user's permission status in different subreddits

    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of your PRAW instance
    
    Returns
    -------
    A list of subreddits and the user's permission status within it

    Original Script
    ---------------
    for subreddit in reddit.redditor(str(reddit.user.me())).moderated():
        for moderator in reddit.subreddit(subreddit.display_name).moderator():
            if (moderator.name == str(reddit.user.me()) and str(moderator.mod_permissions) != "['all']"):
                print (f'{subreddit.display_name}: {moderator.mod_permissions}')
    """
    return [[f"{sub.display_name}: {moderator.mod_permissions}"
             for moderator in instance.subreddit(sub.display_name).moderator()
             if (moderator.name == str(reddit.user.me()) and str(moderator.mod_permissions) != "['all']")]
            for sub in instance.redditor(str(instance.user.me().moderated()))]