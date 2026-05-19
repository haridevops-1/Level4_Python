# Given an array of Integers identify the maximum occurring element.
# Example:

# Input : [5,5,4,1,1,1,6,7,8], Output : 1
# Input : [5] , Output: 5
# Input: [1,2,2,3,3] , Output : [2,3]
# Input : [], Output: ‘invalid input’


# def is_maximumOccurring(arr: list[int]):
#     if len(arr) == 0:
#         return "Invalid Input"
#     if len(arr) == 1:
#         return arr
#     else:
#         empty_dict = {}
#         for i in range(0, len(arr), +1):
#             if arr[i] not in empty_dict:
#                 empty_dict[arr[i]] = 1
#             else:
#                 empty_dict[arr[i]] += 1
        # return empty_dict
        # for key in empty_dict:



# print(is_maximumOccurring([5, 5, 4, 1, 1, 1, 6, 7, 8]))  ## Output : 1

# print(is_maximumOccurring([5]))  ## Output : 5
