class Solution():
    def solve(self, a):
        if(len(a)==0):
            return [None, None, None, None]
        b=[]

        for num in a:
            b.append(float(num))
        mean=self.calu(b)
        var=self.calvars(b)
        y=self.calsk(b)
        y2=self.calku(b)
        result =[mean,var,y,y2]
        return result

    def calu(self,b):

	    sums=0
	    for nums in b:
	        sums+=nums
	    return sums/float(len(b))
    def calvars(self,b):
        if(len(b)<=1):
            return None
        u = self.calu(b)
        sum1 = 0.0
        for nums in b:
            temp = (nums - u) ** 2

            sum1 += temp
        var = sum1 / (float(len(b))-1.0)
        return var
    def calvar(self,b,c):
        if(len(b)<=1):
            return None
        u=self.calu(b)
        sum1=0.0
        for nums in b:
            temp=(nums-u)**c

            sum1+=temp
        var=sum1/(float(len(b)))
        return var
    def calsk(self,b):
        if (len(b) <= 1):
            return None
        v2=self.calvar(b,2)
        v3=self.calvar(b,3)
        y=v3/(v2**1.5)
        return y
    def calku(self,b):
        if (len(b) <= 1):
            return None
        v2=self.calvar(b,2)
        v4=self.calvar(b,4)
        print v4
        y=v4/(v2*v2)-3.0
        return y
s=Solution()
print s.solve([])