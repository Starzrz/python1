import math
import numpy
import urllib
import csv
import tensorflow as tf;

class Solution():
    def solve(self):
        numbers=[1,2,3,4,5,6,7,8]
        return self.calmean(numbers)
        csv_reader = urllib.urlopen('http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv', 'utf-8')
        data = csv.reader(csv_reader)
        a = []
        column = [row[8] for row in data]
        for i in range(6, len(column) - 3):
            a.append(float(column[i]))
        print a
        csv_reader = urllib.urlopen('http://py.mooctest.net:8081/dataset/temperature/temperature_2014.csv', 'utf-8')
        data = csv.reader(csv_reader)
        b = []
        column2 = [row[8] for row in data]
        for i in range(5, len(column2) - 3):
            b.append(float(column2[i]))
        print b

        c = []
        for i in range(len(a)):
            c.append(b[i] - a[i])

        u3 = numpy.mean(c)
        s3 = numpy.var(c)
        print u3, s3
        n1 = len(a)
        t = u3 / (s3 / math.sqrt(n1))
        print t
        t1 = 1.6973
        if (t < t1):
            return 'NO'
        else:
            return 'YES'

    def calmean(self,a):
        sum = 0.0
        for num in a:
            sum += num
        return sum / float(len(a))

s = Solution()
print s.solve()
b1=[6879,
4572,
41736,
15617,
10387,
12519,
8328,
11200,
8598,
34825,
24654,
31594,
19173,
25679,
46753,
51936,
29647,
36869,
53596,
30889,
5805,
10333,
31499,
20685,
26023,
1284,
16265,
13717,
3143,
3648,
14220]
b2=[5739,
3418,
23654,
9455,
7140,
9590,
6298,
8951,
6687,
23157,
15543,
19417,
12114,
11968,
30616,
27263,
19467,
20923,
31282,
16506,
2947,
6419,
19224,
11080,
14577,
598,
10590,
7792,
1661,
1966,
7648]
c1=[6134,
3990,
35157,
13812,
9541,
11088,
7200,
9731,
7712,
28690,
20829,
24104,
15252,
20019,
37620,
40690,
23921,
29313,
41389,
25318,
4485,
9080,
27881,
16391,
22906,
1283,
14009,
10992,
2789,
3190,
13471]
c2=[5348,
3058,
21704,
8404,
6653,
8679,
5408,
7730,
6288,
20176,
14168,
17182,
10749,
10508,
27000,
23094,
16927,
17462,
25579,
14402,
2514,
5736,
16912,
10129,
13388,
555,
9255,
6595,
1540,
1833,
7200]
b3=[]
c3=[]
for i in range(len(b1)):
    temp1=float(b1[i]-b2[i])
    temp2=float(c1[i]-c2[i])
    b3.append(temp1)
    c3.append(temp2)
print b3,c3