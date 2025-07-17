class Solution(object):
    """
    N = # of emails in the list of emails 
    M = # of items in the email string 

    Runtime Complexity: O(N * M) [for using a list]

    Spacetime Complexity: O(N * M)
    """

    def numUniqueEmails(self, emails): 
        '''
        Note: the set contains unique items. 

        General Approach: 

        go through email list, removing the dots in the local 
        name and remove everything after the '+' sign, 
        but before the '@' sign in the local name.

        After removal, add the email to the set and after adding 
        all of them, return the length of the set (a set is used to 
        contain the unique emails).  
        ''' 


        unique_emails = set()  

        for email in range(len(emails)):

            split_email = self.splitEmails(emails[email])

            if split_email not in unique_emails:
                unique_emails.add(split_email)
        return len(unique_emails)



    def splitEmails(self, email): 
        '''  
        Handle the splitting of the emails
        ''' 

        split_email = []

        #find the index of '@' 
        indexof_ampersand = email.index('@')


        for value in range(len(email)): 
            if email[value].isalnum():
                split_email.append(email[value])
            elif email[value] == '+':
                split_email.append(email[indexof_ampersand:])
                break
            else:
                continue
        return ''.join(split_email)




firstSet_emails = Solution()
print(firstSet_emails.numUniqueEmails(["test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"]))



