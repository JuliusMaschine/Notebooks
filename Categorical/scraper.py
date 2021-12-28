import praw
import os
from dotenv import load_dotenv
import csv
import itertools
import threading
import time
import sys

# Load environment variables
load_dotenv()

done = False
# here is the animation


def animate():
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        if done:
            break
        sys.stdout.write("\rloading " + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\rDone!     ")


t = threading.Thread(target=animate)
t.start()
# long process here


# Create a reddit instance
data = {}
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent="watcherbot",
)
# Get the top posts from the subreddit
subreddit = reddit.subreddit(
    """ConservativeKiwi
    +PersonalFinanceNZ
    +newzealand+universityofauckland
    +Coronavirus_NZ"""
)
hot_list = subreddit.hot(limit=None)

# set the keyword
keywords = [
    "covid",
]


# Loop through the posts
def scrape():
    for submissions in hot_list:
        num_title = 1

        submissions.comments.replace_more(limit=0)

        # Get the title of the post and exclude the stickied posty
        subreddit_conditions = [
            not submissions.stickied,
            any(word in submissions.selftext.lower() for word in keywords),
            any(word in submissions.title.lower() for word in keywords),
            any(word in comments.body for word in keywords for comments in submissions.comments.list()),
        ]

        if all(subreddit_conditions):
            num_com = 0

            data[submissions.title] = {}

            data[submissions.title][submissions.selftext] = submissions.score

            # Loop through the comments
            comments = submissions.comments.list()[:100]

            data[submissions.title]["comments"] = {}

            # Loop through the comments
            for comment in comments:
                num_com += 1

                # Get the comment text and append it to the list as responses
                # to the submission
                reply = comment.body
                reply_score = comment.score
                data[submissions.title]["comments"][reply] = reply_score

        # limit the posts to 100 top posts in the hot section
        if num_title == 100:
            break


scrape()

# To compile the data to a csv file
with open("data1.csv", "w") as csvfile:
    fieldnames = ["title", "post", "post_score", "comment", "comment_score"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    # write the title, selftext, score, comment, comment_score into the
    # csv file
    for title, contents in data.items():
        for post, score in contents.items():
            if post == "comments":
                for comment, comment_score in score.items():
                    writer.writerow(
                        {
                            "title": title,
                            "comment": comment,
                            "comment_score": comment_score,
                        }
                    )
            else:
                writer.writerow(
                    {
                        "title": title,
                        "post": post,
                        "post_score": score,
                    }
                )


time.sleep(10)
done = True
