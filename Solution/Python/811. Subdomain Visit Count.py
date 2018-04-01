class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = dict()
        for i in cpdomains:
            arr = i.split(" ")
            times = arr[0]
            webArr = arr[1].split(".")
            cur = ""
            for i in range(len(webArr) - 1, -1, -1):
                if len(cur) > 0:
                    cur = webArr[i] + "." + cur
                else:
                    cur = webArr[i]
                d[cur] = d.get(cur, 0) + int(times)

        res = []
        for i in d:
            res.append(str(d[i]) + " " + i)
        return res


s = Solution()
cpdomains = ["900 google.mail.com", "50 yahoo.com",
             "1 intel.mail.com", "5 wiki.org"]
res = s.subdomainVisits(cpdomains)
print(res)
