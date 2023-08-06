def antibrigadingbanbot(instance, brigaded_thread, brigading_source):
    """
    Script to generate a ban bot for anti-brigading purposes

    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of your PRAW instance
    
    Returns
    -------
    A ban bot for anti-brigading

    Original Script
    ---------------
    newline = "\n\n"

    submission1 = reddit.submission('5 OR 6 DIGIT ID OF BRIGADED THREAD IN YOUR SUBREDDIT')

    submission2 = reddit.submission(5 OR 6 DIGIT ID OF SOURCE OF BRIGADE')

    submission1.comments.replace_more()  #TAKES A WHILE TO LOAD, BE PATIENT

    for comment in submission1.comments.list():
        try:
            for comment2 in reddit.redditor(comment.author.name).comments.new(limit=200):
                if (comment2.submission.id == submission2.id):
                    comment.mod.remove()
                    if not any(reddit.subreddit(str(comment.subreddit)).banned(redditor=comment.author)):
                        banstring = (f'You have been banned for participating in a brigade. {newline}Brigaded thread participation: www.reddit.com/r/{comment.subreddit}/comments/{comment.submission}/title/{comment.id}{newline}Source of brigade:  www.reddit.com/r/{comment2.subreddit}/comments/{comment2.submission}/title/{comment2.id}')
                        reddit.subreddit(str(comment.subreddit)).banned.add(comment.author, ban_reason="brigade", ban_message= banstring)
                        print (comment.author)
        except KeyboardInterrupt: raise
        except Exception as error:
            print(error)
    """
    newline = "\n\n"
    brigaded_sub_thread = instance.submisisons(brigaded_thread)
    brigade_source = instance.submissions(brigading_source)

    brigaded_sub_thread.comments.replace_more()

    for comment in brigaded_sub_thread.comments.list():
        try:
            for comment2 in instance.redditor(comment.author.name).comments.new(limit=200):
                if (comment2.submission.id == submission.id):
                    comment.mod.remove()
                    if not any(instance.subreddit(str(comment.subreddit)).banned(redditor=comment.author)):
                        banstring = (
                            f"You have been banned for participating in a bridage. {newline}"
                            f"Brigaded thread participation: www.reddit.com/r/{comment.subreddit}/comments/{commit.submission}/title/{commit.id} {newline}"
                            f"Source of brigade: www.reddit.com/r/{comment2.subreddit}/comments/{comment2.submission}/title/{comment2.id}"
                        )
                        instance.subreddit(str(comment.subreddit)).banned.add(comment.author, ban_reason="brigade", ban_message= banstring)
                        print(comment.author)
        except KeyboardInterrupt:
            raise
        except Exception as error:
            print(error)
