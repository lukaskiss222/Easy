def main:void(){
    n:int = readint() 

    if n < 1 {
        printf("Prilis male N!!!")
        return 
    }

    max:int = readint()
    for i:int from 0 to n - 1 by 1 {
        temp:int = readint()
        if temp > max {
            max = temp
        }
    } 
    printf("Maximum je: %d\n",max) 
}
