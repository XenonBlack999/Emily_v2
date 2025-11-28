import pyjokes
import time  # optional, to slow down output

while True:
    joke = pyjokes.get_joke()
    print(joke)
    print("-" * 40)  # separator between jokes
    time.sleep(3)     # wait 3 seconds before next joke
