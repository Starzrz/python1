import numpy
import math
class Solution():
	def solve(self):
         a = [112.15,
             114.59,
             118.71,
             113.07,
             108.87,
             112.91,
             115.67,
             115.1,
             111.49,
             121.38,
             118.36,
             131.07,
             125.71,
             128.27,
             124.28,
             127.64,
             123.94,
             125.78,
             129.49,
             122.0,
             129.43,
             113.8,
             112.98,
             126.2,
             113.61,
             100.08,
             116.1,
             124.79,
             112.69,
             114.36,
             105.56]
         z=1.65
         mean=numpy.mean(a)
         var=numpy.var(a)
         s=math.sqrt(var)
         n=len(a)
         res1=(z*s)/math.sqrt(n)
         result1=[mean-res1,mean+res1]
         return result1
s=Solution()
print s.solve()


