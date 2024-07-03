def main():
    iternum = 0
    N = int(input('Enter the value for N: '))
    for i in range(N):
        for j in range(i + 1):  # Complete for loop statement
            print(f'({i}, {j})', end=' ')
            iternum = iternum + 1
        
        print()  


    ########################################
    # Do not delete the return statement
    ########################################
    return iternum


if __name__ == '__main__':
    main()
