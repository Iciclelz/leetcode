class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = dict()
        self.following = dict()
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId in self.tweets:
            self.tweets[userId].append((tweetId, self.time))
        else:
            self.tweets[userId] = [(tweetId, self.time)]
            
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feed = list()

        feed += self.tweets[userId] if userId in self.tweets else list()
        if userId in self.following:
            for user in self.following[userId]:
                feed += self.tweets[user] if user in self.tweets else list()
        
        feed = list(set(feed))
        feed.sort(reverse=True, key=lambda x : x[1])
        return list(map(lambda x : x[0], feed))[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = { followeeId }
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)