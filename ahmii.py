‎#URL_Shortener script coded by Ahmii 
‎import requests
‎import time
‎from colorama import Fore, Style, init
‎init(autoreset=True)
‎
‎def typeprint(text, color=Fore.WHITE):
‎for ch in text:
‎print(color + ch, end='', flush=True)
‎time.sleep(0.01)
‎print(Style.RESET_ALL)
‎
‎def shorten_tinyurl(url):
‎return requests.get("http://tinyurl.com/api-create.php", params={'url': url}).text
‎
‎def shorten_isgd(url):
‎return requests.get("https://is.gd/create.php", params={'format': 'simple', 'url': url}).text
‎
‎def shorten_dagd(url):
‎return requests.get("https://da.gd/s", params={'url': url}).text.strip()
‎
‎def shorten_cleanuri(url):
‎res = requests.post("https://cleanuri.com/api/v1/shorten", data={'url': url})
‎return res.json().get("result_url", "Error")
‎
‎def shorten_clckru(url):
‎return requests.get(f"https://clck.ru/--?url={url}").text.strip()
‎
‎def shorten_cuttly(url):
‎return requests.get(f"https://cutt.ly/api/api.php?key=test&short={url}").text
‎
‎def shorten_0x0st(url):
‎return requests.post("https://0x0.st", files={"file": (None, url)}).text.strip()
‎
‎def shorten_gggg(url):
‎return requests.get(f"https://gg.gg/api.php?longurl={url}").text.strip()
‎
‎def shorten_psbe(url):
‎return requests.get(f"https://psbe.in/api/short?url={url}").text.strip()
‎
‎def shorten_lnurl(url):
‎return requests.post("https://ln.run/api/link/shorten", data={"url": url}).json().get("short_link", "Error")
‎
‎def shorten_siasy(url):
‎return requests.get(f"https://siasy.in/api?url={url}").text.strip()
‎
‎def shorten_ur1(url):
‎return requests.get(f"http://ur1.ca/index.php?longurl={url}").text.strip()
‎
‎def shorten_shrtco(url):
‎return requests.get(f"https://api.shrtco.de/v2/shorten?url={url}").json()['result']['short_link']
‎
‎def shorten_tnysh(url):
‎return requests.post("https://tny.sh/api/shorten", data={"url": url}).json().get("short", "Error")
‎
‎def shorten_sid(url):
‎return requests.get(f"https://s.id/api.php?url={url}").text.strip()
‎
‎def menu():
‎print(Fore.YELLOW + """
‎Choose a URL Shortener Service:
‎1. TinyURL
‎2. is.gd
‎3. da.gd
‎4. CleanURI
‎5. clck.ru
‎6. cutt.ly
‎7. 0x0.st
‎8. gg.gg
‎9. psbe.in
‎10. ln.run
‎11. siasy.in
‎12. ur1.ca
‎13. shrtco.de
‎14. tny.sh
‎15. s.id
‎""")
‎
‎def main():
‎typeprint("\n🔗 MultiLinkX - Free 15x URL Shorteners by Ahmii editor 🔗", Fore.CYAN)
‎menu()
‎choice = input(Fore.GREEN + "📌 Enter your choice (1-15): ").strip()
‎long_url = input(Fore.BLUE + "\n🌐 Enter Long URL: ").strip()
‎
‎typeprint("\n⏳ Processing your request...\n", Fore.MAGENTA)
‎
‎try:
‎if choice == "1":
‎short = shorten_tinyurl(long_url)
‎elif choice == "2":
‎short = shorten_isgd(long_url)
‎elif choice == "3":
‎short = shorten_dagd(long_url)
‎elif choice == "4":
‎short = shorten_cleanuri(long_url)
‎elif choice == "5":
‎short = shorten_clckru(long_url)
‎elif choice == "6":
‎short = shorten_cuttly(long_url)
‎elif choice == "7":
‎short = shorten_0x0st(long_url)
‎elif choice == "8":
‎short = shorten_gggg(long_url)
‎elif choice == "9":
‎short = shorten_psbe(long_url)
‎elif choice == "10":
‎short = shorten_lnurl(long_url)
‎elif choice == "11":
‎short = shorten_siasy(long_url)
‎elif choice == "12":
‎short = shorten_ur1(long_url)
‎elif choice == "13":
‎short = shorten_shrtco(long_url)
‎elif choice == "14":
‎short = shorten_tnysh(long_url)
‎elif choice == "15":
‎short = shorten_sid(long_url)
‎else:
‎print(Fore.RED + "❌ Invalid choice! Please run again.")
‎return
‎
‎print(Fore.LIGHTGREEN_EX + f"✅ Short URL:\n👉 {short}")
‎except Exception as e:
‎print(Fore.RED + f"⚠️ Error: {e}")
‎
‎if __name__ == "__main__":
‎main()
‎
