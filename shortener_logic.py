import random
import string

# In memory database 

url_database = {}  # dictionary

def generate_short_code(length = 6) :
    """function to generate the shortened url"""
    # pool of all possible alphabets and digits
    characters = string.ascii_letters + string.digits
    # return random combination 6 characters from this pool
    return ''.join(random.choice(characters) for i in range(length))


def shorten_url(long_url):
    """the main function to shorten the url"""

    print(f"ORIGINAL URL: {long_url}")

    while(True):
        short_code = generate_short_code()
        
        if(short_code not in url_database):
            break


    url_database[short_code] = long_url

    # let's pretend our website it short.ly for now
    short_url = "http://short.ly/" + short_code

    print(f"SHORTENED URL: {short_url}\n")

    return short_code


def get_long_url(short_code):
    """Retrieves the original URL from a short code"""

    long_url = url_database.get(short_code) # returns None if short_code not present in the dictionary (database)
 
    if(long_url) :
        print(f"Redirecting to: {long_url}")
    else :
        print("Short code not found!")

    return long_url


""""Testing Our Logic"""

code1 = shorten_url("https://www.google.com/search?q=introduction+to+system+design")
code2 = shorten_url("https://en.wikipedia.org/wiki/Artificial_intelligence")

# try to retrieve above urls

print("-----Retrieving URLs-----")
get_long_url(code1)
get_long_url(code2)

get_long_url("nonexistent") # this is to check failing case