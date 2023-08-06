def checkcrosspostperms(instance):
    """
    Simple script that checks subs that doesn't allow crossposts

    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of the PRAW instance

    Returns
    -------
    sub_list
        A list of subs that does not allow crossposting

    Original Script
    ---------------
    for subreddit in reddit.redditor(str(reddit.user.me())).moderated():
        try:
            if not reddit.subreddit(subreddit.display_name).mod.settings()['allow_post_crossposts']:
                print(f'{subreddit.display_name} \n')
        except:
            continue
    """
    sub_list = []

    for sub in instance.redditor(str(instance.user.me())).moderated():
        try:
            if not instance.subreddit(sub.display_name).mod.settings()['allow_post_crossposts']:
                sub_list.append(sub.display_name)
        except:
            continue

    return sub_list