import heapq
import collections


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user = {}  # 当前系统用户字典
        self.Tid = 0  # 记录推文绝对id

    def _new_user(self, userId):
        F = {userId}  # 关注者集合，初始时关注自己
        T = collections.deque(maxlen=10)  # 推文列表，长度为10的双端队列，利用其超长即弹出特性
        self.user[userId] = {'F': F, 'T': T}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user:
            self._new_user(userId)
        self.user[userId]['T'].append((self.Tid, tweetId))  # 更新推文列表，记录(推文绝对id, 推文id)
        self.Tid += 1

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.user:  # 用户不存在
            return []
        Tlist = []
        for uid in self.user[userId]['F']:
            Tlist.extend(list(self.user[uid]['T']))  # 关注的推文
        T10 = heapq.nlargest(10, Tlist)  # 利用堆的性质取出最大10个
        return [T[1] for T in T10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.user:
            self._new_user(followerId)
        if followeeId not in self.user:
            self._new_user(followeeId)
        self.user[followerId]['F'].add(followeeId)  # 利用集合去重特性，省去重复关注的判断

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        # 两个用户均存在，且取关的不是自己
        if followerId in self.user and followeeId in self.user and followeeId != followerId:
            self.user[followerId]['F'].discard(followeeId)