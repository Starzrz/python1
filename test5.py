class Solution():
    def solve(self, a):
        mean=self.calu(a)
        var=self.calvar(a)
        result =[mean,var]
        return result

    def calu(self,b):
	    sums=0
	    for nums in b:
	        sums+=nums
	    return sums/float(len(b))
    def calvar(self,b):
        u=self.calu(b)
        sum1=0.0
        for nums in b:
            temp=(b-u)**2
            sum1+=temp
        var=sum1/float(len(b))
        return var
s=Solution()
print s.solve([1,2,3])
import numpy
