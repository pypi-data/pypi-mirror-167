def searchnewestpost(instance, sub_name, num_post):
    """
    Script that searches for the N newest posts (limit up to 50).

    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of the PRAW instance
    sub_name : str
        Name of the subreddit
    num_post : num
        Number of post use wish to search (limit: 50)

    Returns
    -------
    post_list
        A list of post copy from search
    post_list_orig
        A list of original post from search
    """
    post_list = []
    post_list_orig = []

    for submission in instance.subreddit(sub_name).new(limit=num_post):
        for i in instance.subreddit(sub_name).search(submission.title, limit=5):
            if i.title == submission.title and submission.url != i.url:
                post_list.append(f"www.reddit.com/r/{sub_name}/comments/{submission.id}")
                post_list_orig.append(f"www.reddit.com/r/{sub_name}/comments/{i.id}")
    
    return post_list, post_list_orig