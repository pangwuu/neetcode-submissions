import heapq

TOP_N = 10

class Tweet:
    def __init__(self, userId: int, tweetId: int, timestamp: int) -> None:
        self.userId = userId
        self.tweetId = tweetId
        self.timestamp = timestamp

class User:
    def __init__(self, userId: int) -> None:
        self.userId = userId
        self.followers = set() # an array of users
        self.tweets = []
    
    def post(self, tweetId: int, timestamp: int) -> None:
        newTweet = Tweet(self.userId, tweetId, timestamp)
        self.tweets.append(newTweet)
    
    def follow(self, userId: int) -> None:
        self.followers.add(userId)
        print(f'{self.userId} currently follows {self.followers}')
    
    def unfollow(self, userId: int) -> None:
        # O(n) operation! optimise with sets?
        if userId in self.followers:
            self.followers.remove(userId)

        print(f'{self.userId} currently follows {self.followers}')
    
    def getNewsFeed(self, userIdMap: dict) -> List[int]:
        # get ALL tweets from all followers, and put them into a priority queue
        newsFeed = []
        heapq.heapify(newsFeed)

        for followerId in self.followers:
            tweets = userIdMap[followerId].tweets
            for tweet in tweets:
                # we're using a min heap to get it so for the most recent we need to make it negative
                heapq.heappush(newsFeed, [-tweet.timestamp, tweet.tweetId])
        
        # include your own tweets
        for tweet in self.tweets:
            heapq.heappush(newsFeed, [-tweet.timestamp, tweet.tweetId])
        
        # pop the top 10 (or however many is in the news feed)
        popped_num = min(TOP_N, len(newsFeed))
        top_10 = []
        for _ in range(popped_num):
            popped = heapq.heappop(newsFeed)
            if popped not in top_10:
                top_10.append(popped)

        return [i[1] for i in top_10]


class Twitter:

    def __init__(self):
        # userId -> User object
        self.mappings = {}
        self.global_time = 0
    
    def makeNewUser(self, newUserId: int) -> None:
        if newUserId not in self.mappings:
            new_user = User(newUserId)
            self.mappings[newUserId] = new_user
        self.global_time += 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.makeNewUser(userId)

        if userId in self.mappings:
            user = self.mappings[userId]
            user.post(tweetId, self.global_time)
        
        self.global_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.makeNewUser(userId)

        user = self.mappings[userId]
        self.global_time += 1
        return user.getNewsFeed(self.mappings)


    def follow(self, followerId: int, followeeId: int) -> None:
        self.makeNewUser(followerId)
        self.makeNewUser(followeeId)

        if followerId not in self.mappings:
            # make new user
            newUser = User(followerId)
            self.mappings[followerId] = newUser
        
        user = self.mappings[followerId]
        user.follow(followeeId)
        self.global_time += 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.makeNewUser(followerId)
        self.makeNewUser(followeeId)       

        user = self.mappings[followerId]
        user.unfollow(followeeId)    
        self.global_time += 1    
