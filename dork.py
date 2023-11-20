
from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time
from os import system

system('cls')
system('color a')


if sys.version[0] in "2":
    print ("\n[x] ..n00b.. Dorks Eye Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\tDorks Eye \033[1;91mI like to See Ya, Hacking \033[0m😃\n\n")
    exit()




try:
    data = input("\n[+] Do You Like To Save The Output In A File? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Give The File a Name: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Saving is Skipped...")
    print ("\n" + "  " + "»" * 78 + "\n")


# ... (your existing code)

def dorks():
    try:
        dork = input("\n[+] Enter The Dork Search Query: ")
        amount = input("[+] Enter The Number Of Websites To Display: ")
        print("\n ")

        requ = 0
        counter = 0
        unique_urls = set()  # Set to store unique URLs

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print("[+] ", counter, results)
            
            requ += 1
            if requ >= int(amount):
                break

            url = results.split('/')[2]  # Extracting the domain part of the URL
            unique_urls.add(url)

            data = url
            logger(data)
           # Add a delay of 2 seconds between requests

        print("\n[•] Unique URLs:")
        for idx, url in enumerate(unique_urls, start=1):
            print(f"{idx}. {url}")

    except KeyboardInterrupt:
        print("\n")
        print("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)

    print("[•] Done... Exiting...")
    print("\n\t\t\t\t\033[34mDorks Eye\033[0m")
    print("\t\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
    sys.exit()

# ... (your existing code)

# =====# Main #===== #
if __name__ == "__main__":
    dorks()

