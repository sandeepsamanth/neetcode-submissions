class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left=1
        left_arr=[]

        for i in range(len(nums)):
            left_arr.append(left)
            left*=nums[i]

        right_arr=[]
        right=1
        for j in range(len(nums)-1,-1,-1):
            right_arr.append(right)
            right*=nums[j]

        for i in range(len(left_arr)):
            left_arr[i]=left_arr[i]*right_arr[len(nums)-1-i]
        print(left_arr)

        return left_arr