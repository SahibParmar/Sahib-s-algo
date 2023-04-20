def find_placeof(arr,ele):
    start=0;end=len(arr)-1
    i=int((start+end)/2)
    fp=0
    while i>=start and i<=end :
        if arr[i]<=ele :
            start=i+1;end=end
            fp=i+1
        else:
            start=start;end=i-1
            fp=i
        i=int((start+end)/2)
    return fp

def find_element_at_i(arr1,arr2,i):
    if len(arr1)==0:
        return arr2[i]
    elif len(arr2)==0:
        return arr1[i]
    start1=0;start2=0
    end1=len(arr1)-1;end2=len(arr2)-1
    mid=int((start1+end1)/2)
    index=0
    while True:
        if len(arr1)==0:
            return arr2[i]
        elif len(arr2)==0:
            return arr1[i]
        
        j=find_placeof(arr2[start2:end2+1],arr1[mid])
        index=j+mid
        if index==i:
            return arr1[mid]
        elif index>i:
            arr1=arr1[0:mid]
            arr2=arr2[0:j]
            mid=int(len(arr1)/2)   
        else:
            arr1=arr1[mid+1:]
            arr2=arr2[j:]
            mid=int(len(arr1)/2) 
            i=i-index-1

def find_median(arr1,arr2):
    l1=l2=0
    if (len(arr1)+len(arr2))%2==0:
        l1=(len(arr1)+len(arr2))/2
        l2=l1+1
    else:
        l1=l2=(len(arr1)+len(arr2)+1)/2
    a= find_element_at_i(arr1,arr2,int(l1)-1)       # here l1-1 because l1 is n of term not index
    b=find_element_at_i(arr1,arr2,int(l2)-1)
    return (a+b)/2

arr1=[1];arr2=[4,5,6]
print(find_median(arr1,arr2))