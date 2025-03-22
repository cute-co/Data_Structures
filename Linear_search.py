def Linear_search(n,arr,key):
    for i in range(n):
        if arr[i]==key:
            return i
    return -1    
if __name__ == "__main__":
    n=int(input("Enter the size"))
    arr=list(map(int,input("Enter the Elements").split())) 
    key=int(input("Enter the key value"))      
    result=Linear_search(n,arr,key)
    if result != -1:
        print(f"Element found at index {result}") 
    else:
        print("Element not found")           