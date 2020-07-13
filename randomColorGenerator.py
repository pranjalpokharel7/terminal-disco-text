import random
import time

def randomColorSelector():
    """
        Returns a random color (string) from the 8-bit terminal colors available.
    """
    colors8Bit = {
        # "Black" : "\u001b[30m",
        "Red" : "\u001b[31m",
        "Green" : "\u001b[32m",
        "Yellow" : "\u001b[33m",
        "Blue" : "\u001b[34m",
        "Magenta" : "\u001b[35m",
        "Cyan" : "\u001b[36m",
        "White" : "\u001b[37m"
    }
    
    # generate a random color from red to white, for black/dark terminals, black(0) is not visible so commented out
    random.seed(time.time())
    randKey = random.choice(list(colors8Bit))

    return colors8Bit[randKey]