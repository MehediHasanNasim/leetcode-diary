# using built in module
class Solution(object):
    def numUniqueEmails(self, emails):
        unique = set()
        for e in emails:
            local, domain = e.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            unique.add((local, domain))
        return len(unique)
    
# without using built in module
class Solution(object):
    def numUniqueEmails(self, emails):
        unique = set()
        for e in emails:
            i, local = 0, ''
            while e[i] not in ['@', '+']:
                if e[i] != '.':
                    local += e[i]
                i += 1
            while e[i] != '@':
                i += 1
            domain = e[i + 1:]
            unique.add((local, domain))       
        return len(unique)