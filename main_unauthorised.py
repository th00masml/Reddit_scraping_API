import praw

# Let's connect to reddit
reddit = praw.Reddit(client_id='enter your credentials here',
                     client_secret='enter your credentials here', password='enter your credentials here',
                     user_agent='enter your credentials here', username='enter your credentials here')

# Define subreddit
subreddit = reddit.subreddit('ArtificialInteligence')

# Chose reddit filter 
hot_ai = subreddit.hot(limit=10)

for submission in hot_ai:
    if not submission.stickied:
        # Prints just title
        print("Simple title: ", submission.title)
        # Prints more specific informations
        print("Specific informations: ", 'Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
                                                                           submission.ups,
                                                                           submission.downs,
                                                                           submission.visited))