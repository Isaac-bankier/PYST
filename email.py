##############################
#          email.py          #
#       Email validator      #
#      By Isaac Bankier      #
##############################

def validate(email, verbos=False):
    """Email validator"""
    valid = True #Assume the email is valid
    bannedChars = list("<>!#$%^&*()+=/*+|[]{};:, ") #List of characters that CANNOT be in an email address
    forcedChars = list("@.") #List of characters that MUST be in the email

    for char in bannedChars: #Go through each of the banned characters
        if char in email: #Check if its in the email
            valid = False #Make the email invalid if it is
            if verbos: #For testing
                print("[*] Invalid char '"+char+"' found. Email is no longer valid.") #Print extra info

    for char in forcedChars: #Go through each of the forced characters
        if char not in email: #Check if its not in the email
            valid = False #Make the email invalid if it is
            if verbos: #For testing
                print("[*] Essential char '"+char+"' not found. Email is no longer valid.") #Print extra info

    #make sure there is no more than on @
    sections = email.split("@")

    if len(sections) != 2: #check if there are more or less sections split by @'s
        valid = False #Make the email invalid if it is
        if verbos: #For testing
            print("[*] More than one '@'. Email is no longer valid.") #Print extra info

    #Work on the username section of the email
    #         isaacbankier@gmail.com
    #         ------------

    userSection = sections[0] #Grab everything before the @

    #pretty sure there is no work to be done here...

    #Work on the host section of the email
    #        isaacbankier@gmail.com
    #                     ---------

    hostSection = sections[1] #Grab everything after the @

    #The host section should have a host name and several sub-domains (at least 1)
    #TODO rename this variable
    hostParts = hostSection.split(".") #

    if len(hostParts) < 2: #check if there are less than 2 sections of the host name
        valid = False #Make the email invalid if it is
        if verbos: #For testing
            print("[*] Invalid host name. Email is no longer valid.") #Print extra info

    return valid


print(validate(input("Please enter the email to be checked")))
