import random
import time

def randomColorSelector():
    """
        Returns a random color (string) from the 8-bit terminal colors available.
    """
    colors8Bit = {
        0 : "\u001b[30m",
        1 : "\u001b[31m",
        2 : "\u001b[32m",
        3 : "\u001b[33m",
        4 : "\u001b[34m",
        5 : "\u001b[35m",
        6 : "\u001b[36m",
        7 : "\u001b[37m"
    }
    
    # generate a random color from red(1) to white(7), for black/dark terminals, black(0) is not visible
    random.seed(time.time())
    rand = random.randint(1,7) 

    return colors8Bit[rand]