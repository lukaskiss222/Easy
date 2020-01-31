def main:void(){

    n:int = readint()
    

    
    mat:int*(n)
    for i:int from 0 to n by 1 {
        temp:int(n)
        mat[i] = temp
        for j:int from 0 to n by 1 {
            mat[i,j] = readint()
        }
    }
    
    for k:int from 0 to n by 1{
        for i:int from 0 to n by 1{
            for j:int from 0 to n by 1{
                if mat[i,j] > (mat[i,k] + mat[k,j]){
                    mat[i,j] = mat[i,k] + mat[k,j] 
                }
            }
        }
    }

    printf("======OUTPUT======\n")
    for i:int from 0 to n by 1{
        for j:int from 0 to n by 1{
            printf("%d ",mat[i,j])
        }
        del mat[i]
        printf("\n")
    }
    del mat

}
