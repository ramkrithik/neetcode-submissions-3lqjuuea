from heapq import heappush,heapify,nsmallest
class Twitter:

    def __init__(self):
        
        self.user_posts = {}
        self.follower_list = {}
        self.follower_feed = {}
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -=1
        if userId not in self.user_posts:
            self.user_posts[userId] = []

        self.user_posts[userId].append((self.time,tweetId))

        self.follower_list[userId] = self.follower_list.get(userId,set())

        self.follower_feed[userId] = self.follower_feed.get(userId, [])
        heappush(self.follower_feed[userId],(self.time,tweetId))

        for follower in self.follower_list.get(userId, set()):
            self.follower_feed[follower] = self.follower_feed.get(follower, [])
            heappush(self.follower_feed[follower],(self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:

        return [tweetId for _, tweetId in nsmallest(10, self.follower_feed.get(userId, []))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
           return
        
        self.follower_list[followeeId] = self.follower_list.get(followeeId,set())
        if followerId in self.follower_list[followeeId]:
           return
        self.follower_list[followeeId].add(followerId)

        
        self.follower_feed[followerId] = self.follower_feed.get(followerId,[])

        for post in self.user_posts.get(followeeId, []):
            heappush(self.follower_feed[followerId],post)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
           return

        if followeeId not in self.follower_list or followerId not in self.follower_list[followeeId]:
           return

        for post in self.user_posts.get(followeeId, []):
            self.follower_feed[followerId].remove(post)
        
        if followerId in self.follower_feed:
            heapify(self.follower_feed[followerId])
        if followeeId in self.follower_list:
            self.follower_list[followeeId].discard(followerId)
        

        
