import requests
import sys

def main():
    ask_user()


def ask_user():
    global action

    print "########################################"
    print "Daddy and Elliott's special Roku Remote"
    print "########################################"
    print "\n"
    print "Available commands are:"
    print "on | off | nbc | abc | exit\n\n"

    action = raw_input('Enter the command:\n')

    perform_action()


def perform_action():
    exit_status = 0

    while (exit_status < 1):

      if action == "on":
        print "on"
        exit_status = 1

      elif action == "off":
        print "off"
        exit_status = 1

      elif action == "nbc":
        print "nbc"
        exit_status = 1

      elif action == "abc":
        print "abc"
        exit_status = 1

      elif action == "exit":
        exit(0)

      else:
        print "Invalid option.  Try again \n"
        exit_status = 1

    main()

if __name__ == "__main__":
    main()

