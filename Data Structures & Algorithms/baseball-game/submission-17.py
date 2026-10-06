class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score, score_end_idx = 0, -1
        scoreboard = []
        for i in range(len(operations)):
            if operations[i] == "+" and len(scoreboard) >= 2:
                scoreboard.append(scoreboard[score_end_idx - 1] + scoreboard[score_end_idx])
                score_end_idx += 1
            
            if operations[i] == "C" and scoreboard:
                scoreboard.pop()
                score_end_idx -= 1
            
            if operations[i] == "D" and len(scoreboard) >= 1:
                scoreboard.append(2 * scoreboard[score_end_idx])
                score_end_idx += 1
            
            if operations[i] not in ["+", "C", "D"]:
                scoreboard.append(int(operations[i]))
                score_end_idx += 1
            
            print(scoreboard)
        
        
        return sum(scoreboard)