def checksharedsubs(instance, user1, user2):
    """
    Script for checking what subreddits two users share

    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of your PRAW instance
    user1 : str
        The name of first user
    user2 : str
        The name of second user

    Returns
    -------
    A list of shared subreddits between the two users

    Original Script
    ---------------
    user1 = reddit.redditor("NAME")
    user2 = reddit.redditor("NAME")

    for subreddit in user1.moderated():
        for moderator in reddit.subreddit(subreddit.display_name).moderator():
            if moderator.name == user2.name:
                print (subreddit.display_name)
    """
    return [[sub.display_name
             for moderator in instance.subreddit(sub.display_name).moderator()
             if moderator.name == user2.name]
            for sub in user1.name]