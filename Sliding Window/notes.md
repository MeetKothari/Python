# 01 - Sliding Window Algorithm!

The Sliding window is a problem-solving technique for problems that involve arrays/lists. These problems are easy to solve using a brute force approach in O(n^2) or O(n^3). Using the 'sliding window' technique, we can reduce the time complexity to O(n).
------------------
![](@attachment/Clipboard_2022-04-05-11-44-40.png)
------------------

'''

{
  # O(n) solution for finding
# maximum sum of a subarray of size k
 
 
def maxSum(arr, k):
    # length of the array
    n = len(arr)
 
    # n must be greater than k
    if n < k:
        print("Invalid")
        return -1
 
    # Compute sum of first window of size k
    window_sum = sum(arr[:k])
 
    # first sum available
    max_sum = window_sum
 
    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
 
    return max_sum
 
 
# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))

}

'''
