from colorama import Fore, Style, Back

class log:
    """A class made to help logging."""
    def warning(text: str) -> None:
        """Log given text to a WARNING level"""
        print(f"{Fore.LIGHTYELLOW_EX}[WARNING] {Fore.YELLOW}{text}{Style.RESET_ALL}")

    def critical(text: str) -> None:
        """Log given text to a CRITICAL level"""
        print(f"{Fore.LIGHTRED_EX}[CRITICAL] {Fore.RED}{text}{Style.RESET_ALL}")

    def important(text: str) -> None:
        """Log given text to an IMPORTANT level"""
        print(f"{Fore.RED}[!] {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}")

    def info(text: str) -> None:
        """Log given text to an INFO level"""
        print(f"{Fore.LIGHTBLUE_EX}[INFO] {Fore.BLUE}{text}{Style.RESET_ALL}")

    def success(text: str) -> None:
        """Log given text to a SUCCESS level"""
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}{text}{Style.RESET_ALL}")

    def fail(text: str) -> None:
        """Log given text to a FAIL level"""
        print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}")

    def start(text: str) -> None:
        """Log given text to a START level (?)"""
        print(f"{Fore.LIGHTYELLOW_EX}[#] {Fore.YELLOW}{text}{Style.RESET_ALL}")

    def separate_yellow() -> None:
        """Separate with yellow"""
        print(f"{Fore.YELLOW}------------------{Style.RESET_ALL}")

    def separate_magenta() -> None:
        """Separate with magenta"""
        print(f"{Fore.MAGENTA}------------------{Style.RESET_ALL}")