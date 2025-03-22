def Bubble_sort(n,arr):
    Swapped=False
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True

if __name__ == "__main__":
    n=int(input("Enter the number of elements"))
    arr=list(map(int,input("Enter the elements").split()))
    Bubble_sort(n,arr)
    for i in range(n):
        print("%d" %arr[i],end=" ")               