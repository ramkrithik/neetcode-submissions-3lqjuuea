from bisect import insort
class Leaderboard:

    def __init__(self):
        self.leaderboard = {}
        self.sorted_array = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = 0
            self.sorted_array.append((0,playerId))

        
        old_score = self.leaderboard[playerId]
        self.leaderboard[playerId]+=score
        new_score = self.leaderboard[playerId]
        
        self.sorted_array.remove((old_score,playerId))
        insort(self.sorted_array, (new_score,playerId))        

    def top(self, K: int) -> int:
        return sum(score for score, _ in self.sorted_array[-K:])

    def reset(self, playerId: int) -> None:
        old_score = self.leaderboard[playerId]
        self.sorted_array.remove((old_score,playerId))
        self.leaderboard[playerId]=0
        insort(self.sorted_array,(0,playerId))
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
