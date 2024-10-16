// Returns the median of the 2 provided sorted arrays
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    // Store the merged array
    int *merged = calloc(nums1Size+nums2Size, sizeof(int));
    int mergedSize = 0; // Current size of the merged array
    int sumSize = nums1Size + nums2Size; // Number of elements
    int nums1Pointer = 0;
    int nums2Pointer = 0;

    // Merge the 2 provided lists into merged array
    while(nums1Pointer < nums1Size && nums2Pointer < nums2Size)
    {
        if(nums1[nums1Pointer] < nums2[nums2Pointer])
        {
            merged[mergedSize] = nums1[nums1Pointer];
            mergedSize++;
            nums1Pointer++;
        }
        else
        {
            merged[mergedSize] = nums2[nums2Pointer];
            mergedSize++;
            nums2Pointer++;
        }
    }
    while(nums1Pointer < nums1Size)
    {
        merged[mergedSize] = nums1[nums1Pointer];
        mergedSize++;
        nums1Pointer++;
    }
    while(nums2Pointer < nums2Size)
    {
        merged[mergedSize] = nums2[nums2Pointer];
        mergedSize++;
        nums2Pointer++;
    }
    
    // If there are an odd number of elements
    if(mergedSize % 2 != 0)
    {
        // Return the middle element
        return merged[mergedSize / 2];
    }
    // If there are an even number of elements
    else
    {
        // Return the mean of the 2 middle elements
        return (merged[mergedSize/2] + merged[(mergedSize/2) - 1]) / 2.0;
    }
}