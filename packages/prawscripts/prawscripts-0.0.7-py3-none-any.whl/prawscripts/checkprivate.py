def checkprivate(instance, sub_list):
    """
    Script to check if sub is privated.

    Parameters
    ----------
    instance : PRAW Reddit Instance
        The name of the PRAW Instance

    Returns
    -------
    sub_list_results
        A list of subs that are privated
    """
    sub_list_results = [];

    for subreddit in instance.redditor(str(instance.user.me())).moderated():
        if (subreddit.subreddit_type == 'private'):
            sub_list_results.append(f"{subreddit.display_name}, {subreddit.subreddit_type}")

    return sub_list_results