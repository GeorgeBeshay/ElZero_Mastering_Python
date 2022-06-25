# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On First And Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Result And Fourth Element And So On
# [5] Till One Element Is Left And This Is The Result Of The Reduce 
# [6] The Function Can Be Pre-Defined Function Or Lambda Function 
# -------------------------------------------------------------------------

from functools import reduce

# Example 1
def sumAll(num1,num2):
    return num1 + num2
numbers = [1,8,2,9,100]
result = reduce(sumAll,numbers) # ((((1+8)+2)+9)+100)
print(result)

print("=" * 39) # Separator # ---------------------------------------------

# Example 2
numbers = [1,8,2,9,100]
result = reduce((lambda num1,num2:num1+num2),numbers) # ((((1+8)+2)+9)+100)
print(result)

print("=" * 39) # Separator # ---------------------------------------------