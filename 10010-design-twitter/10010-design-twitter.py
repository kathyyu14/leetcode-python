class Twitter:

    def __init__(self):
        self.count=0
        self.tweetMap = defaultdict(list) # tweet map
        self.followMap = defaultdict(set) # follower set 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        # Go through the users followers and add their tweets to the minHeap list
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap[followeeId]
            for tweet in tweets:
                minHeap.append(tweet)
        
        heapq.heapify(minHeap)
        for _ in range(10):
            if minHeap:
                _, tweetId = heapq.heappop(minHeap)
                res.append(tweetId)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)