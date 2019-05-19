import praw

# Let's connect to reddit
reddit = praw.Reddit(client_id='enter your credentials here',
                     client_secret='enter your credentials here', password='enter your credentials here',
                     user_agent='enter your credentials here', username='enter your credentials here')

# Define subreddit
subreddit = reddit.subreddit('ArtificialInteligence')

# Chose reddit filter 
hot_ai = subreddit.hot(limit=10)

# Let's create a loop to get first 20 posts on a subject
for submission in hot_ai:
    if not submission.stickied:
        # Prints just title
        print("SIMPLE TITLE: ", submission.title)
        # Prints more specific informations
        #print("Specific informations: ", 'Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
                                                                           ###submission.visited))
        
        """ ADD COMMENTS PARSING """
        
        # Now we will create loop for comments, logic is pretty the same
        comments = submission.comments.list()
        for comment in comments:
            print('COMMENT:', comment.body)
            if len(comment.replies) > 0: # If there is any reply
                for reply in comment.replies:
                    print('REPLY:', reply)
                    if len(comment.replies) == 0:
                        print (40*'*')
                    else:
                        print("\t"+reply.body)
                        print (40*'*')
                        
        # Now let's try to create comment replace pairs
        submission.comments.replace_more(limit=0)
        # Set the results limit to 20. You can change if you like
        for comment in submission.comments.list()[:20]:
            print (40*'-')
            print('PARENT ID:',comment.parent())
            print('COMMENT ID:',comment.id)
            # Limit for output. You can change it if you like
            print(comment.body[:5000])