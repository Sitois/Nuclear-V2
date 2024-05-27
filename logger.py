from colorama import Fore, Style, Back

class log:
    """A simple class made to help logging."""
    def warning(text: str) -> str:
        """Log given text to a WARNING level. Returns the logged version of the given text"""
        log_message = f"{Fore.LIGHTYELLOW_EX}[WARNING] {Fore.YELLOW}{text}{Style.RESET_ALL}"
        print(log_message)

        return log_message

    def critical(text: str) -> str:
        """Log given text to a CRITICAL level. Returns the logged version of the given text"""
        log_message = f"{Fore.LIGHTRED_EX}[CRITICAL] {Fore.RED}{text}{Style.RESET_ALL}"
        print(log_message)

        return log_message

    def important(text: str) -> str:
        """Log given text to an IMPORTANT level. Returns the logged version of the given text"""
        log_message = f"{Fore.RED}[!] {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"
        print(log_message)
        
        return log_message

    def info(text: str) -> str:
        """Log given text to an INFO level. Returns the logged version of the given text"""
        log_message = f"{Fore.LIGHTBLUE_EX}[INFO] {Fore.BLUE}{text}{Style.RESET_ALL}"
        print(log_message)

        return log_message

    def success(text: str) -> str:
        """Log given text to a SUCCESS level. Returns the logged version of the given text"""
        log_message = f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}{text}{Style.RESET_ALL}"
        print(log_message)

        return log_message

    def fail(text: str) -> str:
        """Log given text to a FAIL level. Returns the logged version of the given text"""
        log_message = f"{Fore.RED}[-] {Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"
        print(log_message)

        return log_message

    def start(text: str) -> str:
        """Log given text to a START level (?). Returns the logged version of the given text"""
        log_message = f"{Fore.LIGHTYELLOW_EX}[#] {Fore.YELLOW}{text}{Style.RESET_ALL}"
        print(log_message)

        return log_message

    def separate_yellow() -> str:
        """Separate with yellow. Returns the separated text"""
        log_message = f"{Fore.YELLOW}------------------{Style.RESET_ALL}"
        print(log_message)

        return log_message

    def separate_magenta() -> str:
        """Separate with magenta. Returns the separated text"""
        log_message = f"{Fore.MAGENTA}------------------{Style.RESET_ALL}"
        print(log_message)

        return log_message

    def separate_text(text: str) -> str:
        """Separate with "=". Returns the separated text"""
        log_message = f"{Fore.YELLOW}========={text}========={Style.RESET_ALL}"
        print(log_message)

        return log_message

    def separate(text: str) -> str:
        """The given text of `separated_text` is required. Returns the separated text"""
        log_message = f"{Fore.YELLOW}=================={"=" * len(text)}{Style.RESET_ALL}"
        print(log_message)

        return log_message