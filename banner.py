##############################
#         banner.py          #
#      Banner generator      #
#      By Isaac Bankier      #
##############################

#TODO add pattern support

def banner(text, pretext="| ", posttext=" |", banner="="):
    bannerText = pretext + text + posttext # The text to be displayed in the banner
    bannerPart = len(bannerText) * banner # The header and footer for the banner
    finalBanner = bannerPart + "\n" + bannerText + "\n" + bannerPart # The final banner
    return finalBanner

print(banner(input("What is the message for your banner: ")))
