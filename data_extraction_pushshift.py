import pandas as pd
from pmaw import PushshiftAPI
import datetime as dt
import argparse

# Function to extract data using pushshiftAPI (it's an old script -- Pushshift API is discontinued (This might give and idead how to extract data from reddit))
def extract_data(before, after, subreddit, limit, num):

    # Calling the API
    api = PushshiftAPI()

    sub_reddit_data = api.search_submissions(
                            subreddit = subreddit,
                            limit = limit,
                            before = before,
                            after = after
                        )

    # Converting the data into pandas dataframe
    comments = pd.DataFrame(sub_reddit_data)
    comments.to_csv('./flair_dataset' + '_' + str(num) + '.csv', header = True, index = False, columns = list(comments.axes[1]))

    return comments

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--subreddit",
        type = str
    )

    parser.add_argument(
        "--limit",
        type = int
    )

    parser.add_argument(
        "--after",
        type = str
    )

    parser.add_argument(
        "--before",
        type = str
    )

    parser.add_argument(
        "--n",
        type = int
    )

    args = parser.parse_args()

    ls = []
    for dates_ in [args.before, args.after]:
        date_dt = dt.datetime.strptime(dates_, '%Y-%m-%d')

        unix_time = int(dt.datetime(date_dt.year,date_dt.month,date_dt.day,0,0).timestamp())

        ls.append(unix_time)

    extract_data(before = ls[0],
                 after = ls[1],
                 subreddit = args.subreddit,
                 limit = args.subreddit,
                 num = args.n
    )