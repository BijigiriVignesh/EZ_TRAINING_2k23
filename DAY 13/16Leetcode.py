class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapper ={

            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        for  number in digits:
            if not res:
                for i in mapper[number]:
                    res.append(i)
            else:
                temp =[]
                for letter in mapper[number]:
                    for word in res:
                        temp.append(word + letter)
                res = temp
        print(res)
        return res

