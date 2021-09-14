'''#brute Force time- O(m*n)
#space- O(1) no extra space
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i=0
        ans=[]
        for i in range(0,len(nums2)):
            for j in range(0,len(nums1)):
                if nums2[i]==nums1[j]:
                    nums1[j]=float('inf')
                    ans.append(nums2[i])
                    break
        return ans'''
'''
#using hashmap time- O(m+n)
soace=O(n) extra space used for hashmap
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            ans=[]
            d1={}
            for i in nums1:
                if i in d1:
                    d1[i]=d1[i]+1
                else:
                    d1[i]=1
            for i in nums2:
                if i in d1 and d1[i]>0:
                    ans.append(i)
                    d1[i]=d1[i]-1
            return ans
'''
#binary search
#time comp-nlogn+mlogm+nlogm --> O(nlogn+mlogm)
#space- O(1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        m=len(nums2)
        if n>m:
            return self.intersect(nums2,nums1)
        else:
            nums1=sorted(nums1)
            nums2=sorted(nums2)
            ans=[]
            l=0
            h=len(nums2)-1
            for i in range(0,len(nums1)):
                target=nums1[i]
                bsidx=self.binarysearch(nums2,l,h,target)
                if bsidx!=-1:
                    ans.append(target)
                    l=bsidx+1
            return ans
    def binarysearch(self,nums,l,h,target):
        while l<=h:
                    mid=(l+h)//2
                    if target==nums[mid]:
                        if l==mid or nums[mid-1]<nums[mid]:
                            return mid
                        else:
                            h=mid-1
                    elif target<nums[mid]:
                        h=mid-1
                    else:
                        l=mid+1
        return -1
            
        


        
