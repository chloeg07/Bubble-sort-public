def bubble_sort(arr):
    n = len(arr)
    #Traverse through all elements in the list
    for i in range(n):
        #Track if any elements were swapped in this iteration
        swapped = False
        #Last i elements are already sorted
        for j in range(0, n - i - 1):
            #Display the array with elements being compared highlighted
            print_array_with_comparison(arr, j, j + 1)
            
            #Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                #Display swap
                print(f"\033[91mSwapping {arr[j]} and {arr[j + 1]}\033[0m")
                #\033[93m...\033[0m: Colors the text yellow. 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            else:
                #Display no swap
                print(f"\033[92mNo swap needed for {arr[j]} and {arr[j + 1]}\033[0m")
                #Colors the text to red. 
        
        #Print the array after each pass
        print("Array after pass", i + 1, ":", arr)
        print()

        #If no elements were swapped, the array is already sorted
        if not swapped:
            break

def print_array_with_comparison(arr, index1, index2):
    #Print the array with two elements being compared highlighted
    for i in range(len(arr)):
        if i == index1 or i == index2:
            #Highlight the elements being compared in yellow
            print(f"\033[93m{arr[i]}\033[0m", end=' ')
        else:
            print(arr[i], end=' ')
    print()  #New line after printing the array

if __name__ == "__main__":
    #Get user input, split it into strings, and convert to integers in one step
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print("Unsorted array:", arr)
    print()

    bubble_sort(arr)

    print("Sorted array:", arr)
