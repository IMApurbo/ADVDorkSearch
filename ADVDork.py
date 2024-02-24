import argparse
import os
import time 
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style


# ANSI color escape codes
BLUE = Fore.BLUE
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Style.RESET_ALL
END = '\033[0m'

def print_with_animation(text, color):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(0.03)  # Adjust the sleep duration for speed
    print(RESET)

def print_colored_figlet_text(text, color):
    try:
        os.system(f"figlet -f slant '{text}' > temp_figlet.txt")  # Generate figlet text to a temporary file
        with open("temp_figlet.txt", "r") as file:
            figlet_output = file.read()
        os.remove("temp_figlet.txt")  # Remove temporary file

        colored_text = f"{color}{figlet_output}{RESET}"  # Apply color after figlet
        print(colored_text)
    except FileNotFoundError:
        print(f"{RED}Error:{RESET} 'figlet' command not found. Please install figlet.")

def google_search(dork, num_results):
    try:
        for url in search(dork, num_results=num_results):
            print(BLUE + "[+]" + END, RED + url + END)
    except Exception as e:
        print(BLUE + "[+]" + END, RED + "Failed to perform Google search:" + END, e)

def bing_search(dork, num_results):
    try:
        base_url = "https://www.bing.com/search"
        params = {'q': dork}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', class_='b_algo')
            for link in links:
                href = link.get('href')
                print(BLUE + "[+]" + END, RED + href + END)
        else:
            print(BLUE + "[+]" + END, RED + "Failed to perform Bing search" + END)
    except Exception as e:
        print(BLUE + "[+]" + END, RED + "Failed to perform Bing search:" + END, e)

def yahoo_search(dork, num_results):
    try:
        base_url = "https://search.yahoo.com/search"
        params = {'p': dork}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', class_='ac-algo')
            for link in links:
                href = link.get('href')
                print(BLUE + "[+]" + END, RED + href + END)
        else:
            print(BLUE + "[+]" + END, RED + "Failed to perform Yahoo search" + END)
    except Exception as e:
        print(BLUE + "[+]" + END, RED + "Failed to perform Yahoo search:" + END, e)

def duckduckgo_search(dork, num_results):
    try:
        base_url = "https://duckduckgo.com/html"
        params = {'q': dork}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', class_='result__a')
            for link in links:
                href = link.get('href')
                print(BLUE + "[+]" + END, RED + href + END)
        else:
            print(BLUE + "[+]" + END, RED + "Failed to perform DuckDuckGo search" + END)
    except Exception as e:
        print(BLUE + "[+]" + END, RED + "Failed to perform DuckDuckGo search:" + END, e)

def main():
    print_colored_figlet_text("KORISHEE THE CYBERMASTER", GREEN)
    print_with_animation("PRESENTING A AUTOMATED SQL PARAMETER FINDER FOR SQLI", BLUE)
    parser = argparse.ArgumentParser(description=BLUE + "Perform dorking on search engines" + END)
    parser.add_argument("-d", "--dork", type=str, help=BLUE + "Dork string to search for" + END, required=True)
    parser.add_argument("-e", "--engine", type=str, help=BLUE + "Search engine (google, bing, yahoo, duckduckgo)" + END, required=True)
    parser.add_argument("-n", "--num_results", type=int, help=BLUE + "Number of search results to retrieve" + END, default=10)
    args = parser.parse_args()

    dork = args.dork
    engine = args.engine.lower()
    num_results = args.num_results

    if engine == 'google':
        google_search(dork, num_results)
    elif engine == 'bing':
        bing_search(dork, num_results)
    elif engine == 'yahoo':
        yahoo_search(dork, num_results)
    elif engine == 'duckduckgo':
        duckduckgo_search(dork, num_results)
    else:
        print(BLUE + "[+]" + END, RED + "Unsupported search engine" + END)

if __name__ == "__main__":
    main()
