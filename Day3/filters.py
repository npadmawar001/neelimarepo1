"""
filter eleemnts
filter(fn, Iterables)
based on T/F the elements are EXTRACTED and stored in Res.

"""
import re

num=[10,20,10, 15, 5, 30]
maxRes=list(filter(lambda en:en>10, num))
print(maxRes)  #[20, 15, 30]

fruits=['guava','orange','avacado','banana','apple']
fruits_f=list(filter(lambda ef: re.findall(r"^a",ef), fruits))
print(fruits_f)

numbrs={"first":10, "sec":7, "thrd":22, "frth":5, "fifth":17}
evenRes=dict(filter(lambda en:en[1]%2==0, numbrs.items()))
print(evenRes)


nums=[10,20,None, 15, 'NA', 30, None, None, 40, 'NA']
#justNums=list(filter(lambda x: x is not None, nums))
#justNums=list(filter(lambda x: x != 'NA', nums))

justNums=list(filter(lambda x: (x is not None) and (x != 'NA'), nums))
print(justNums)



