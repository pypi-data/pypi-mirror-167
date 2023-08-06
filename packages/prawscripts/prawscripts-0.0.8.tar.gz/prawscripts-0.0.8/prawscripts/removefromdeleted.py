def removefromdeleted(instance, sub_name):
    """
    Script to remove posts and/or comments from OPs that deleted their account

    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of the PRAW instance
    sub_name : str
        The name of subreddit you're working on

    Original Script
    ---------------
    # Define the subreddit you're working on
    subreddit = reddit.subreddit("YOUR_SUBREDDIT")

    # Fetch the last 1000 items and remove them if the OP deleted their acount.
    for i,post in enumerate(subreddit.new(limit=1000),1):
        print(f"{i} of 1000")
        if post.author is None:
            post.mod.remove()

        # Next 4 lines removes comments, remove these four lines to ignore comments.
        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            if comment.author is None:
                comment.mod.remove()
    """
    sub = instance.subreddit(sub_name)

    for i, post in enumerate(sub.new(limit=1000), 1):
        print(f"{i} of 1000")
        if post.author is None:
            post.mod.remove()

        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            if comment.author is None:
                comment.mod.remove()