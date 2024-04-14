import random  # Import the random module for generating random numbers
import pygame  # Import the pygame module for creating the visualization
import sys  # Import the sys module for system-specific functions

def quicksort(arr, left, right, screen, clock):  # Define the quicksort function
    if left < right:  # Check if the left index is less than the right index
        pivot_index = partition(arr, left, right, screen, clock)  # Partition the array and get the pivot index
        quicksort(arr, left, pivot_index - 1, screen, clock)  # Recursively sort the left subarray
        quicksort(arr, pivot_index + 1, right, screen, clock)  # Recursively sort the right subarray

def partition(arr, left, right, screen, clock):  # Define the partition function
    pivot = arr[right]  # Choose the rightmost element as the pivot
    i = left - 1  # Initialize the index of the smaller element
    for j in range(left, right):  # Iterate through the subarray
        if arr[j] <= pivot:  # If the current element is smaller than or equal to the pivot
            i += 1  # Increment the index of the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap the current element with the element at the smaller index
            draw_array(screen, arr, i, j, clock, "Quicksort")  # Draw the updated array on the screen
    arr[i + 1], arr[right] = arr[right], arr[i + 1]  # Swap the pivot with the element at the next index of the smaller element
    draw_array(screen, arr, i + 1, right, clock, "Quicksort")  # Draw the updated array on the screen
    return i + 1  # Return the index of the pivot

def bubblesort(arr, screen, clock):  # Define the bubblesort function
    n = len(arr)  # Get the length of the array
    for i in range(n - 1):  # Iterate through the array
        for j in range(n - i - 1):  # Iterate through the unsorted part of the array
            if arr[j] > arr[j + 1]:  # If the current element is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the current element with the next element
                draw_array(screen, arr, j, j + 1, clock, "Bubblesort")  # Draw the updated array on the screen
    return arr  # Return the sorted array

def selectionsort(arr, screen, clock):  # Define the selectionsort function
    n = len(arr)  # Get the length of the array
    for i in range(n - 1):  # Iterate through the array
        min_index = i  # Assume the current element is the minimum
        for j in range(i + 1, n):  # Iterate through the unsorted part of the array
            if arr[j] < arr[min_index]:  # If the current element is smaller than the assumed minimum
                min_index = j  # Update the index of the minimum element
        if min_index != i:  # If the minimum element is not the current element
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the current element with the minimum element
            draw_array(screen, arr, i, min_index, clock, "Selection Sort")  # Draw the updated array on the screen
    return arr  # Return the sorted array

def shufflesort(arr, screen, clock):  # Define the shufflesort function
    while True:  # Keep shuffling until the array is sorted
        shuffled = arr[:]  # Create a copy of the array
        random.shuffle(shuffled)  # Shuffle the elements randomly
        draw_array(screen, shuffled, -1, -1, clock, "Shufflesort")  # Draw the shuffled array on the screen
        if shuffled == sorted(arr):  # If the shuffled array is sorted
            return shuffled  # Return the sorted array

def radixsort_lsd(arr, screen, clock):
    max_num = max(arr) # Find the maximum number in the array
    exp = 1 # Initialize the exponent to 1
    while max_num // exp > 0: # Iterate until the maximum number divided by the exponent becomes 0
        counting_sort(arr, exp, screen, clock) # Call counting_sort for each digit place
        exp *= 10 # Multiply the exponent by 10 to move to the next digit place
    return arr # Return the sorted array

def counting_sort(arr, exp, screen, clock):
    n = len(arr) # Get the length of the array
    output = [0] * n # Create an output array of the same size as the input array
    count = [0] * 10 # Create a count array to store the count of each digit (0-9)

    for i in range(n): # Iterate through each element in the array
        index = arr[i] // exp # Calculate the index based on the current digit place
        count[index % 10] += 1 # Increment the count for the corresponding digit

    for i in range(1, 10): # Iterate through the count array (except the first element)
        count[i] += count[i - 1] # Modify the count array to store the cumulative count

    i = n - 1 # Start from the rightmost element of the array
    while i >= 0: # Iterate through the array from right to left
        index = arr[i] // exp # Calculate the index based on the current digit place
        output[count[index % 10] - 1] = arr[i] # Place the element in the output array based on the count
        count[index % 10] -= 1 # Decrement the count for the corresponding digit
        i -= 1 # Move to the previous element

    for i in range(n): # Iterate through each element in the output array
        arr[i] = output[i] # Copy the elements from the output array back to the original array
        draw_array(screen, arr, i, -1, clock, "Radix Sort (LSD)")  # Draw the current state of the arraydef draw_array(screen, arr, index1, index2, clock, algorithm):  # Define the function to draw the array on the screen
    screen.fill((0, 0, 0))  # Fill the screen with a white background
    bar_width = screen.get_width() // len(arr)  # Calculate the width of each bar based on the screen width and array length
    for i, value in enumerate(arr):  # Iterate through the array elements
        height = value * 4  # Calculate the height of the bar based on the element value
        colour = (255, 255, 255)  # Set the default colour of the bar to white
        if i == index1 or i == index2:  # If the current index matches the specified indices
            colour = (137, 20, 227)  # Set the colour of the bar to purple
        pygame.draw.rect(screen, colour, (i * bar_width, screen.get_height() - height, bar_width, height))  # Draw the bar on the screen

    font = pygame.font.Font(None, 36)  # Create a font object
    label = font.render(algorithm, True, (255, 255, 255))  # Render the algorithm name as text
    screen.blit(label, (10, 10))  # Draw the algorithm name on the screen

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    original_arr = [random.randint(1, 100) for _ in range(50)]

    print("Original array:", original_arr)

    algorithms = [
        ("Quicksort", lambda arr: quicksort(arr, 0, len(arr) - 1, screen, clock)),
        ("Radix Sort (LSD)", lambda arr: radixsort_lsd(arr, screen, clock)),
        ("Bubblesort", lambda arr: bubblesort(arr, screen, clock)),
        ("Selection Sort", lambda arr: selectionsort(arr, screen, clock)),
        ("Shufflesort", lambda arr: shufflesort(arr, screen, clock)),
    ]

    for algorithm_name, algorithm_func in algorithms:
        arr = original_arr[:]
        print(f"{algorithm_name}:")
        algorithm_func(arr)
        print(arr)

        pygame.time.delay(1000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Call the main function
