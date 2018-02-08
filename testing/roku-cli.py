import requests


"""This has been tested on a TCL Roku based TV.  
Roku API is here:  https://sdkdocs.roku.com/display/sdkdoc/External+Control+API
"""

roku_ip = "192.168.50.70"
roku_url = 'http://' + roku_ip + ':8060'


def main():
    ask_user()


def ask_user():
    global action

    print "########################################"
    print "Daddy and Elliott's special Roku Remote"
    print "########################################"
    print "\n"
    print "Menu:"
    print "\n"
    print "1.  Turn TV On"
    print "2.  Turn TV Off"
    print "3.  NBC"
    print "4.  ABC"
    print "5.  CBS"
    print "6.  FOX"
    print "7.  Netflix"
    print "8.  Hulu"
    print "9.  YouTube"
    print "80. List all TV Channels"
    print "81. List all Roku Apps Installed"
    print "99. Quit"

    action = raw_input('Enter your selection:\n')

    perform_action()


def perform_action():
    exit_status = 0

    while (exit_status < 1):

      if action == "1":
        r = requests.post(roku_url + '/keypress/PowerOn')
        exit_status = 1

      elif action == "2":
        r = requests.post(roku_url + '/keypress/PowerOff')
        exit_status = 1

      elif action == "3":
        r = requests.post(roku_url + '/launch/tvinput.dtv?ch=4.1')
        exit_status = 1

      elif action == "4":
        r = requests.post(roku_url + '/launch/tvinput.dtv?ch=6.1')
        exit_status = 1

      elif action == "5":
        r = requests.post(roku_url + '/launch/tvinput.dtv?ch=10.1')
        exit_status = 1

      elif action == "6":
        r = requests.post(roku_url + '/launch/tvinput.dtv?ch=28.1')
        exit_status = 1

      elif action == "7":
        r = requests.post(roku_url + '/launch/12')
        exit_status = 1

      elif action == "8":
        r = requests.post(roku_url + '/launch/2285')
        exit_status = 1

      elif action == "9":
        r = requests.post(roku_url + '/launch/837')
        exit_status = 1

      elif action == "80":
       r = requests.get(roku_url + '/query/tv-channels')
       print r.content
       exit_status = 1

      elif action == "81":
       r = requests.get(roku_url + '/query/apps')
       print r.content
       exit_status = 1

      elif action == "99":
        exit(0)

      else:
        print "Invalid option.  Try again \n"
        exit_status = 1

    main()

if __name__ == "__main__":
    main()

