class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        div = 1
        while x >= 10 * div:
            div *= 10
            
        
        while x:
            right = x % 10
            left = x // div
            if right !=  left : return False
            
            x = (x % div) // 10
            div = div / 100
        return True




""" for reverse """
# num = int(input("Enter a number: "))
# reverse = 0
# while num > 0:
#     rem = num % 10                  # extract the last digit
#     reverse = reverse * 10 + rem    # append rem to the end of the reversed number
#     num //= 10                      # drop the last digit
# print("Reversed number: ", reverse)
# numer = 123%10
# numere = 123//100
# print(numer)
# print(numere)

# chopping
# num = 121
# result = (num%100) // 10
# print(result)

#checking ,if 121 so 100
# x = 12134
# div = 1
# while x>= 10 * div:
#     div *= 10
# print(div)


