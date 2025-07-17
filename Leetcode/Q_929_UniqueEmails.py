class Solution(object):
    """
    N = # of emails in the list of emails 
    M = # of items in the email string 

    Runtime Complexity: O(N * M^2) [for strings]


    Spacetime Complexity: O(N * M) 
    - creating a set and adding all the emails onto it, results 
    in O(N)
    - creating a new string for each email and adding items to it
    is O(M) time
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
        
        split_email = ''


        #find the index of '@' 
        indexof_ampersand = email.index('@')


        for value in range(len(email)): 
            if email[value].isalnum():
                split_email += email[value]
            elif email[value] == '+':
                split_email += email[indexof_ampersand:]
                break
            else:
                continue
        return split_email




firstSet_emails = Solution()
print(firstSet_emails.numUniqueEmails(["test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"]))



