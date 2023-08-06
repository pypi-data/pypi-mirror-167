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
    A list of python dictionaries that contain the copy of the comment link and the original reddit link.

    Original Script
    ---------------
    for submission in reddit.subreddit("SUBREDDIT_NAME_HERE").new(limit=50):
        for i in reddit.subreddit("SUBREDDIT_NAME_HERE").search(submission.title, limit=5):
            if i.title == submission.title and submission.url != i.url:
                print ("copy:", "www.reddit.com/r/SUBREDDIT_NAME_HERE/comments/"+submission.id)
                print ("original:", "www.reddit.com/r/SUBREDDIT_NAME_HERE/comments/" + i.id)
    """
    return [[{"copy": f"www.reddit.com/r/{sub_name}/comments/{submission.id}",
              "original": f"www.reddit.com/r/{sub_name}/comments/{i.id}"}
             for i in instance.subreddit(sub_name).search(submission.title, limit=5)
             if i.title == submission.title and submission.url != i.url]
            for submission in instance.subreddit(sub_name).new(limit=num_post)]