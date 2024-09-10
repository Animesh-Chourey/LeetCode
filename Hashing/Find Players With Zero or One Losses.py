class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[],[]]
        playerLoser = {}

        for winner, loser in matches:
            if winner not in playerLoser:
                playerLoser[winner] = 0 #add the player in the list  with loss count as 0
            
            # add the loser player in the list with loss count incremented by 1
            playerLoser[loser] = playerLoser.get(loser, 0) + 1 
        
        for player, lossCount in playerLoser.items():
            if lossCount == 0: # if the loss count is 0 add the player to the 0th index list
                answer[0].append(player)
            if lossCount == 1: # otherwise add the player to the 1st index list
                answer[1].append(player)
        
        answer[0] = sorted(answer[0])
        answer[1] = sorted(answer[1])

        return answer