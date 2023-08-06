import os
import sys
import argparse
from argparse import RawTextHelpFormatter
from datetime import datetime
import pyfiglet

progname = os.path.basename(sys.argv[0])
author = 'Alok Bharadwaj, Maarten Joosten, Stefan T Huber, Arjen Jakobi, Reinier de Bruin'
version = "0.1"

test_run_command = "emmer test"

description = "A python toolkit for the cryo-EM developer"

main_parser = argparse.ArgumentParser(prog="emmer", description=description, formatter_class=RawTextHelpFormatter)

##################### ADD TEST RUN COMMAND ##############################
main_parser.add_argument('--test', action='store_true', help='Run the test suite')

def print_start_banner():
    """
    Prints a start banner
    """
    from textwrap import fill
    import time
    try:
        username = os.environ['USER']
    except KeyError:
        username = 'User: unknown'
    
    today_date = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")

    print("="*80)
    print("="*80)
    print_text = pyfiglet.figlet_format("EMmer", font="big")
    print(print_text)
    print("\t"*6 + "Version: v{}".format(version))
    print("."*80)
    print("  |  ".join(["User: {}".format(username), "Date: {}".format(today_date), "Time: {}".format(time_now)]))
    print("\n")
    print("Authors:\n")
    author_list = ["Arjen J. Jakobi (TU Delft)",  "Alok Bharadwaj (TU Delft)", "Reinier de Bruin (TU Delft)", \
                "Maarten Joosten (TU Delft)", "Stefan T. Huber (TU Delft)"]
    for author in author_list:
        print("\t{} \n".format(author))
    print("Running tests. Please wait...")
    ## Delay for a bit to make sure the banner is printed before the tests start
    
    time.sleep(1)
    print("="*80)
    print("="*80)

    
def main():
    """
    Main function
    """
    from coverage import Coverage  ## To measure code coverage
    from emmer.tests.run import run_tests
    print_start_banner()
    cov = Coverage()
    cov.start()
    ############################## RUN TESTS ##############################
    run_tests()
    ############################## END TESTS ##############################
    cov.stop()
    cov.save()
    


if __name__ == '__main__':
    main()
