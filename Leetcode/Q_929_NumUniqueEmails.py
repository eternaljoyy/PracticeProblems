class Solution:
            """
            :type emails: List[str]
            :rtype: int 

        ----------------------------------
        Approach A) 
        Go through list of emails 
        - extract the email according to the conditions given 
        - add email to the set (if its not already there)
        - return length of set  

        ----------------------------------
        N = length of all emails in the emails array 
        M = length of each individual email in the array 

        Runtime Complexity: 
            -> **Function numUniqueEmails(): O(N) * O(M)

        Spacetime Complexity: O(N)
            -> Worst case: all of the emails in the array would be 
            unique, therefore, each one would get added onto the set. 
        """   
    def numUniqueEmails(self, emails):

        unique_emails = set()


        for word in range(len(emails)):

            split_email = self.splitEmail(emails[word])

            if split_email not in unique_emails:
                unique_emails.add(split_email)

        return len(unique_emails)



    def splitEmail(self, split_email):

        # split_email = ''.join(domain.split('@'))
        new_email = ''

        for index in range(len(split_email)):
            if split_email[index].isalnum():
                new_email += split_email[index]
            elif split_email[index] == '+' or split_email[index] == '@':

                # TODO: Figure out how much runtime complexity the split[]
                # function takes
                new_email += split_email[split_email.index('@'):]
                break 
        return new_email



#Tests 
email = Solution()
print(email.numUniqueEmails(["m.y+name@email.com"]))


second_emails = Solution()
print(second_emails.numUniqueEmails(["test.email+alex@leetcode.com", 
    "test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))


third_emails = Solution() 
print(third_emails.numUniqueEmails(["test.email+alex@leetcode.com", "test.email@leetcode.com"]))

