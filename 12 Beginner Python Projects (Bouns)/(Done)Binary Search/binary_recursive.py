def binary_search(list, left, right, value):
    if right >= left:
        # Find the middle element 
        mid = int(left + (right - left) / 2)
        

        if list[mid] > value:
            return binary_search(list, left, mid - 1 , value)
        elif list[mid] < value:
            # Right 
            return binary_search(list, mid + 1, right, value)
        else:
            # Best case 
            return mid

    else:
        return -1 

def main():
    list = [2, 3, 4, 10, 15, 20, 30, 9, 11]
    x = 15

    size = len(list) - 1

    result = binary_search(list, 0, size, x)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in the List: ")



if __name__ == "__main__":
    main()