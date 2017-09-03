##############################
#          juice.py          #
#   99 bottles of juice...   #
#      By Isaac Bankier      #
##############################
 
#TODO replace the temp strings

def juicer(iterations=99):
    #Variables
    #define the song
    song = \
"""linux bottles of juice on the wall, linux bottles of juice.
Take one down, pass it around, gnu bottles of juice on the wall.

"""
#The song has two temporary strings (linux and gnu) that are replaced by the correct amount of juice

    while iterations > 0: #loop until we run out of juice
        print(song.replace("linux", str(iterations)).replace("gnu", str(iterations - 1))) # update the song with the correct amounts of juice.
        iterations -= 1 # use up one bottle of juice each iteration

    return

juicer(5)
