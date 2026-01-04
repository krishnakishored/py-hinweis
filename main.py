
# Import the Solution class from the correctly named module
from src.lc150 import merge_sorted_array

def main():
    print("Hello from py-hinweis!")


if __name__ == "__main__":
    # main()    
    sol = merge_sorted_array.Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol.merge(nums1, m, nums2, n) 
    # Example usage:
    print(nums1)  # Output should be [1,2,2,
