
class Solution:
    def sumOfDivisors(self, N):
        for i in range(0, N):
            if N % i == 0:
                result += i
        return result


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)