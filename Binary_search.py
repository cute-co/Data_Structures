def Bubble_sort(n,arr):
    Swapped=False
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
def Binary_search(n,arr,key):
    low=0
    high= n-1
    while low <= high :
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1                       

if __name__ == "__main__":
    n=int(input("Enter the number of elements"))
    arr=list(map(int,input("Enter the elements").split()))
    key=int(input("Enter the key value"))
    Bubble_sort(n,arr)
    print("Sorted array:"," ".join(map(str,arr)))
    result=Binary_search(n,arr,key)
    if result != -1:
        print(f"Element found at index {result}")   
    else:
        print("Element not found")            