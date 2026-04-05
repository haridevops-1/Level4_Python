def CommonElements(nums1, nums2):
    if len(nums1) and len(nums2) == []:
        return "Invalid Input"
    else:
        result = []
        for i in range(0, len(nums1), +1):
            if nums1[i] in nums2:
                result.append(nums1[i])
        return result


print(CommonElements([1, 2, 3, 3, 2, 4], [1, 2, 4, 2, 45, 5]))
