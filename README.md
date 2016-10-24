# SEC Crawler

## Instructions For Git
        # Get my code
        git clone https://github.com/ironpup/quovo-webcrawl
        cd quovo-webcrawl

        # set up and activate virtual environment
        virtualenv venv
        source venv/bin/activate

        # install from requirements
        pip install -r requirements.txt

        # run module with or without arguments
        python3 webcrawl
        python3 webcrawl ciks.txt 13F-HR

## Instructions
In a text file in the root directory, provide a list of ciks, one to each line.  
I have included ciks.txt with some examples.
Run the module 'webcrawl' with 2 possible arguments:
the name of the file of ciks and the form.

If neither is provided, the crawler will automatically look for 'ciks.txt' and form '13F-HR', as provided
in the prompt.

For each cik that has filed that form, a csv will be generated in 'csv' folder, with a name that provides information about that report.

## Assumptions
I assumed that you would want to be able to parse multiple ids with a single run of the process

## Further Things I would do with more time
The nature of small code challenges is to demonstrate what I am capable of in a production environment.

With that said, I have a limited amount of time I can devote to this challange.  
Here is a list of additional things I would do if I had more time / I was working on this professionally:

1.  Tests.  I am aggressive with code coverage.  I would write unit and integration tests.  
2.  Error logging.  Right now, if a process succeeds, a csv is created - an error (such as the user asked for a non-existant CIK or asked for a CIK which has not ever filed the given report) simply results a print out of the stack trace.  In the past, I have built systems that writes a detailed log of the error if a problem fails.  This is an example of what I envision: the users a list of 10 CIKs and the "13F-HR" report, 6 of the CIKs are valid, and result in 6 unique csv files; however, for the 4 which failed (for whatever reason), there are 4 different txt files that log why it failed.
