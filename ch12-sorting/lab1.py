class NaturalMergeSorter:
    def __init__(self):
        return

    # Solution:
    def get_sorted_run_length(self, integer_list, start_index):
        
        # for invalid runs
        if (start_index < 0) or (start_index > len(integer_list)-1):
            return 0
        
        # start with a run of one
        count = 1
        current_index = start_index
        
        # while current_index is less than the rightmost index
        while(current_index < len(integer_list) - 1):
            
            # if the value in the next index is greater or equal to the value at current, increment count and current index by one
            if (integer_list[current_index] <= integer_list[current_index + 1]):
                count += 1
                current_index += 1
            # otherwise break the while loop and return the count
            else:
                break    
        return count        
        
    def natural_merge_sort(self, integer_list):
        # Initial Starting Index
        left_start = 0
        
        # The while loop is exited by returning in the first if statement when the run equals the
        # length of the list, meaning the list is sorted
        while(True):
            
            # Find left run
            left_run = self.get_sorted_run_length(integer_list, left_start)

            # If the run == the length of the list the list is sorted. Thus we return, exiting the algorithm and loop
            if (left_run == len(integer_list)):
                return

            # If the first run ends at the end of the list, we set the left starting index to 0 and restart the loop
            if (left_run + left_start) == len(integer_list):
                left_start = 0
                
            # Otherwise the left and right runs are merged 
            else:
                # the right starting point and the right run are determined
                right_start = left_start+left_run
                right_run = self.get_sorted_run_length(integer_list, right_start)
                
                # left and right sides are merged
                self.merge(integer_list, left_start, right_start - 1, right_start + right_run - 1)

                # if the end of the second run is at the end of the list we set the left start to 0
                if (right_start + right_run) == len(integer_list):
                    left_start = 0
                
                # otherwise we set the left start to the index after the right side ends
                else:
                    left_start = right_start + right_run
            
    #End Solution

    def merge(self, numbers, left_first, left_last, right_last):
        merged_size = right_last - left_first + 1

        merged_numbers = [None] * merged_size
        merge_pos = 0
        left_pos = left_first
        right_pos = left_last + 1

        # Add smallest element from left or right partition to merged numbers
        while left_pos <= left_last and right_pos <= right_last:
            if numbers[left_pos] <= numbers[right_pos]:
                merged_numbers[merge_pos] = numbers[left_pos]
                left_pos += 1
            else:
                merged_numbers[merge_pos] = numbers[right_pos]
                right_pos += 1

            merge_pos += 1

        # If left partition isn't empty, add remaining elements to merged_numbers
        while left_pos <= left_last:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
            merge_pos += 1

        # If right partition isn't empty, add remaining elements to merged_numbers
        while right_pos <= right_last:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
            merge_pos += 1

        # Copy merged numbers back to numbers
        for merge_pos in range(merged_size):
            numbers[left_first + merge_pos] = merged_numbers[merge_pos]
