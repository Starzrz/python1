import math
import numpy
import urllib
import csv
class Solution():
    def solve(self):

        csv_reader = urllib.urlopen('http://py.mooctest.net:8081/dataset/population/population_old.csv', 'utf-8')
        data = csv.reader(csv_reader)
        a = []
        column1 = [row[1] for row in data]
        for i in range(3, len(column1)):
            a.append(float(column1[i]))
        print a
        csv_reader = urllib.urlopen('http://py.mooctest.net:8081/dataset/population/population_total.csv', 'utf-8')
        data = csv.reader(csv_reader)
        b = []
        column2 = [row[4] for row in data]
        for i in range(5, len(column2)):
            b.append(float(column2[i]))
        print b
        c = [];
        for i in range(len(a)):
            per = float(a[i]) / float(b[i]);
            per = 100 * per
            c.append(per)

        n = len(c)

        a = 0.1
        z = 1.65
        u = numpy.mean(c)
        s = numpy.var(c)
        print s
        re1 = z * math.sqrt(s) / math.sqrt(n)
        result1 = [u - re1, u + re1]
        x1 = 43.7730
        x2 = 18.4927
        re2 = (n - 1) * s / x1
        re3 = (n - 1) * s / x2
        result2 = [re2, re3]
        result = [result1, result2]
        return result

s = Solution()
print s.solve()