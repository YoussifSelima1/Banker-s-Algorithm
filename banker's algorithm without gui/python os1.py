import numpy as np
def need_matrix(max_matrix,alloc_matrix):
    need_matrix=np.zeros((len(max_matrix),len(max_matrix[0])),dtype=int)
    for i in range(len(max_matrix)):
        for j in range(len(max_matrix[0])):
            need_matrix[i][j]=max_matrix[i][j]-alloc_matrix[i][j]
    return need_matrix
def safe_sequence(need_matrix,available_matrix):
    safe_seq=[]
    completed=[False]*len(need_matrix)
    while False in completed:
        for i in range(len(need_matrix)):
            if completed[i]==False:
                for j in range(len(need_matrix[0])):
                    if need_matrix[i][j]>available_matrix[0][j]:
                        break
                
                else:
                    safe_seq.append(i)
                    completed[i]=True
                    for j in range(len(available_matrix[0])):
                        available_matrix[0][j]+=need_matrix[i][j]
    return safe_seq

if __name__=="__main__":
    n=int(input("Enter the number of processes: "))
    m=int(input("Enter the number of resources: "))
    #take total instances from user
    total_instances=[]
    for i in range(m):
        total_instances.append(int(input("Enter the total number of instances of resource {}: ".format(i+1))))
    max_matrix=np.zeros((n,m),dtype=int)
    alloc_matrix=np.zeros((n,m),dtype=int)
    available_matrix=np.zeros((1,m),dtype=int)
    for i in range(n):
        for j in range(m):
            max_matrix[i][j]=int(input("Enter the maximum need of process {} for resource {}: ".format(i+1,j+1)))
    for i in range(n):
        for j in range(m):
            alloc_matrix[i][j]=int(input("Enter the current allocation of process {} for resource {}: ".format(i+1,j+1)))
    #calculate available matrix
    for i in range(m):
        available_matrix[0][i]=total_instances[i]-np.sum(alloc_matrix[:,i])

    need_matrix=need_matrix(max_matrix,alloc_matrix)
    safe_seq=safe_sequence(need_matrix,available_matrix)
    #add 1 safe_seq
    for i in range(len(safe_seq)):
        safe_seq[i]+=1

    if len(safe_seq)==0:
        print("The system is in unsafe state")
        print("The need matrix is: \n",need_matrix)
        print("The available matrix is: \n",available_matrix)
        print("The maximum matrix is: \n",max_matrix)
        print("The allocation matrix is: \n",alloc_matrix)
        exit()
    print("The system is in safe state")
    print("The safe sequence is: ",safe_seq)

