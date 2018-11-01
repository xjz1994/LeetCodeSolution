class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = 0
        m = {}
        for i in emails:
            info = i.split("@")
            local = info[0]
            domain = info[1]
            local = local.split("+")[0].replace(".", "")
            email = local + "@" + domain
            if not m.get(email, None):
                res = res + 1
            m[email] = True
        return res


emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
res = Solution().numUniqueEmails(emails)
print(res)


"testemail+david@lee.tcode.com"
