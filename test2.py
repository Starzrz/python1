'''
from log_api import log
import math
class Solution():
	def solve(self):
	    n=51
	    n=math.sqrt(n)
	    s=4.9
	    z1=1.1/(s/n)
	    z1=round(z1,2)
	    z2=1.96
	    log([z1,z2])
	    return [0.95,z1,1]

import math
class Solution7():
	def solve(self):
	    u=5.0
	    x=4.6
	    s=2.2
	    n=20
	    n=math.sqrt(n)
	    z=(x-u)/(s/n)
	    z=round(z,2)
	    result=[19.0,z,1]
	    log(result)
	    return result
class Solution10():
	def solve(self):
	    sum1=43+21+35+0.0
	    p1=1.0/3.0
	    p3=21.0/sum1
	    dis = p1-p3
	    dis = round(dis,2)
	    result = [98,dis,0]
	    log(result)
	    return result

