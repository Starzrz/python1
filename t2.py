import numpy
import math


class Solution():
    def solve(self):
        a = [285,
             307,
             318,
             296,
             346,
             328,
             340,
             311,
             334,
             315,
             327,
             321,
             353,
             347,
             295,
             322,
             301,
             333,
             347,
             362,
             365,
             303,
             315,
             347,
             365,
             361,
             304,
             236,
             280,
             328,
             262]
        b = [167,
             145,
             49,
             162,
             213,
             215,
             230,
             239,
             246,
             198,
             212,
             180,
             343,
             230,
             79,
             134,
             161,
             196,
             259,
             275,
             342,
             207,
             139,
             278,
             329,
             341,
             157,
             193,
             216,
             249,
             184]
        d = []
        for i in range(len(a)):
            temp = float(a[i] - b[i])
            d.append(temp)
        print d
        mean = numpy.mean(d)
        var = numpy.var
        print mean,var
        s = math.sqrt(var)

        t1 = 1.6955
        n = len(d)
        t = mean / (s/ math.sqrt(n-1))

        re = 'YES'
        if (t <t1):
            re = 'NO'
        return [t, re]


s = Solution()
print s.solve()
