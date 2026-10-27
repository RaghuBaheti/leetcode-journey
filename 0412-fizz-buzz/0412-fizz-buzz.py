class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        lst = []
        for i in range(1, n+1):
            lst.append(str(i))
            if i%3 == 0:
                lst.pop()
                lst.append("Fizz")
            if i%5 == 0:
                lst.pop()
                lst.append("Buzz")
            if i%3 ==0 and i%5 == 0:
                lst.pop()
                lst.append("FizzBuzz")
        return lst