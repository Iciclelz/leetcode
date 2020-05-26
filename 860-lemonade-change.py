class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = [0, 0, 0]
        
        for x in bills:
            if x == 5:
                money[0] += 1
            if x == 10:
                if money[0] >= 1:
                    money[1] += 1
                    money[0] -= 1
                else:
                    return False
            if x == 20:
                if money[1] >= 1 and money[0] >= 1:
                    money[2] += 1
                    money[1] -= 1
                    money[0] -= 1
                elif money[0] >= 3:
                    money[2] += 1
                    money[0] -= 3
                else:
                    return False
                
        return True