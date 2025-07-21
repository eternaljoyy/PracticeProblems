class Solution:
    def calPoints(self, operations):
        ''' 
        N = # of items in the operations stack  

        Runtime Complexity: O(N) 
        - going through all items in operations array one by one

        Spacetime Complexity: O(N) 
        - worst-case: adding all numbers to the records stack (if the 
        operations array contained all integers) 
        ''' 

        # stack of records 
        records = []


        for item in range(len(operations)): 

            if operations[item] == "C":
                if records: 
                    records.pop()
            elif operations[item] == "D":
                if records:
                    records.append(records[-1] * 2) 
            elif operations[item] == "+":
                if len(records) >= 2:
                    records.append(records[-1] + records[len(records)-2])
                elif len(records) == 1:
                    records.append(records[-1])
            else:
                val = int(operations[item]) 
                records.append(val)
        return sum(records)


#testcases 
first_rec = Solution()
print(first_rec.calPoints(["5","2","C","D","+"]))

second_rec = Solution()
print(second_rec.calPoints(["5","-2","4","C","D","9","+","+"]))


third_rec = Solution()
print(third_rec.calPoints(["1","C"]))

fourth_rec = Solution()
print(fourth_rec.calPoints(["D", "C", "+", "30"]))