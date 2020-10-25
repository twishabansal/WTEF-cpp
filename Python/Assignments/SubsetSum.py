import itertools
def get_subset_for_sum(arr, k):
    A=[]
    for i in range(len(arr)+1):
        listing=[list(x) for x in itertools.combinations(arr,i)]
        for j in range(len(listing)):
            if sum(listing[j])==k:
                A.append(listing[j])
    if len(A)!=0 and len(A)!=1:
        for i in range(len(A)):
            A[i].sort()
        for k in range(len(A)-1):
            j=k+1
            while j<len(A):
                if A[k]==A[j]:
                    del A[j]
                    j-=1
                j+=1
        return A
    elif len(A)==1:
        return A[0]
    else:
        return None

    
    