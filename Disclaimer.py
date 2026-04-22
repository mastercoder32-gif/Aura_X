import sys

def show_disclaimer():
    # تعريف الألوان للتنسيق
    RED = "\033[1;31m"
    GOLD = "\033[1;33m"
    CYAN = "\033[1;36m"
    GREEN = "\033[1;32m"
    WHITE = "\033[1;37m"
    RESET = "\033[0m"
    
    print(f"\n{RED}" + "!" * 60)
    print(f"{WHITE}             AURA-X SECURITY | LEGAL NOTICE             ")
    print(f"{RED}" + "!" * 60 + f"{RESET}")
    
    print(f"\n{GOLD}[!] WARNING: ETHICAL USE ONLY{RESET}")
    print(f"{CYAN}By accessing this tool, you acknowledge and agree to the following:{RESET}")
    
    print(f"\n {WHITE}* {RESET}This tool is strictly for {GREEN}Educational{RESET} and {GREEN}Ethical Pentesting{RESET} purposes.")
    print(f" {WHITE}* {RESET}Unauthorized access to systems is {RED}ILLEGAL{RESET} and strictly prohibited.")
    print(f" {WHITE}* {RESET}The developer ({GOLD}Julius{RESET}) assumes {RED}NO LIABILITY{RESET} for any misuse.")
    print(f" {WHITE}* {RESET}You are solely responsible for your actions and their consequences.")
    
    print(f"\n{RED}" + "-" * 60 + f"{RESET}")
    
    # الجملة المطلوبة للموافقة
    agreement_phrase = "I agree to all the terms"
    
    print(f"{CYAN}[?] TO PROCEED, PLEASE TYPE THE FOLLOWING PHRASE:{RESET}")
    print(f"{WHITE}>>> {GREEN}'{agreement_phrase}'{RESET}")
    
    try:
        user_input = input(f"\n{GOLD}PROMPT > {RESET}").strip()
        
        if user_input == agreement_phrase:
            print(f"\n{GREEN}[+] ACCESS GRANTED. INITIALIZING AURA-X ENGINES...{RESET}")
            print(f"{CYAN}" + "=" * 60 + f"{RESET}\n")
            return True
        else:
            print(f"\n{RED}[X] ACCESS DENIED: INVALID AGREEMENT PHRASE.{RESET}")
            print(f"{RED}[!] TERMINATING SESSION...{RESET}\n")
            sys.exit()
            
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] SESSION TERMINATED BY USER.{RESET}")
        sys.exit()

if __name__ == "__main__":
    show_disclaimer()

