import sys

def main(args=None):
    # parse user arguments
    if args is None:
        args = sys.argv[1:]

    # run the entire process of creating a csv file for each fund in the input list
    from transferMaster import transferProcess
    currentTransfer = transferProcess('testInput.txt', '13F-HR')
    print('running right now...')   
    currentTransfer.run()
    
if __name__ == "__main__":
    main()
