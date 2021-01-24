class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = list()
        
        for x in range(1, n + 1):
            if x % 3 == 0 and x % 5 == 0:
                l.append('FizzBuzz')
            elif x % 3 == 0:
                l.append('Fizz')
            elif x % 5 == 0:
                l.append('Buzz')
            else:
                l.append(str(x))
                
        return l
            