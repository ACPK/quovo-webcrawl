import sys

def main(args=None):
    # parse user arguments
    if len(args) == 0:
      cikListFile = 'ciks.txt'
      form = '13F-HR'
    else:
      cikListFile = args[0]
      form = args[1]
    # run the entire process of creating a csv file for each fund in the input list
    from transferMaster import transferProcess
    print('running right now with ciks in ', cikListFile, ' and form ', form)
    currentTransfer = transferProcess(cikListFile, form)
    currentTransfer.run()
    
if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
