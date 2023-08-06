
import sys
import textwrap
import traceback

from colorful_terminal import *


def print_exception_details(exception: Exception):
    """colored_print details of the Exception: "function", "path", "line", "code", "type", "message"

    Args:
        exception (Exception): Your Exception
    """
    tb = sys.exc_info()[-1]
    stk = traceback.extract_tb(tb, 1)
    filepath = stk[0][0]
    line = stk[0][1]
    functionname = stk[0][2]
    traceback_parts = list(traceback.TracebackException.from_exception(exception).format())
    code_teile = traceback_parts[-2].split("\n")[1:-1]
    code_teile = [n.strip() for n in code_teile]
    fehlertyp = traceback_parts[-1].split(": ")[0]
    code = "; ".join(code_teile)

    colored_print(f"Fehler in der Funktion {Fore.BRIGHT_RED}{functionname}{Fore.WHITE}")
    colored_print(f"\tDateipfad: \n\t\t{Fore.MAGENTA}{filepath}{Fore.WHITE}")
    colored_print(f"\tLinie:\n\t\t{Fore.BRIGHT_YELLOW}{line}{Fore.WHITE}")
    colored_print(f"\tCode:\n\t\t{Fore.BRIGHT_BLUE}{code}{Fore.WHITE}")
    colored_print(f"\tArt:\n\t\t{Fore.BRIGHT_RED}{fehlertyp}{Fore.WHITE}")
    colored_print(f"\tNachricht:")    
    wrapper = textwrap.TextWrapper(width=200, initial_indent="\t\t", subsequent_indent="\t\t")
    e_str = str(exception)
    if e_str.isspace() or e_str == "":
        e_str = "<Kein Text verfügbar>"
    word_list = wrapper.wrap(text=e_str)
    # colored_print each line.
    for element in word_list:
        colored_print(Fore.BRIGHT_CYAN + element + Fore.WHITE)



def get_exception_details_dict(exception: Exception):
    """Get a dictionary of the Exception with the keys: "function", "path", "line", "code", "type", "message"

    Args:
        exception (Exception): Your Exception

    Returns:
        dict: keys: "function", "path", "line", "code", "type", "message"
    """
    tb = sys.exc_info()[-1]
    stk = traceback.extract_tb(tb, 1)
    filepath = stk[0][0]
    line = stk[0][1]
    functionname = stk[0][2]
    traceback_parts = list(traceback.TracebackException.from_exception(exception).format())
    code_teile = traceback_parts[-2].split("\n")[1:-1]
    code_teile = [n.strip() for n in code_teile]
    fehlertyp = traceback_parts[-1].split(": ")[0]
    code = "; ".join(code_teile)
    e_str = str(exception)
    if e_str.isspace() or e_str == "":
        e_str = "<Kein Text verfügbar>"

    details = {
        "function": functionname,
        "path": filepath,
        "line": line,
        "code": code,
        "type": fehlertyp,
        "message": e_str
    }
    return details



def get_exception_details_str(exception: Exception, colored=True):
    """colored_print details of the Exception: "function", "path", "line", "code", "type", "message"

    Args:
        exception (Exception): Your Exception
    """
    tb = sys.exc_info()[-1]
    stk = traceback.extract_tb(tb, 1)
    filepath = stk[0][0]
    line = stk[0][1]
    functionname = stk[0][2]
    traceback_parts = list(traceback.TracebackException.from_exception(exception).format())
    code_teile = traceback_parts[-2].split("\n")[1:-1]
    code_teile = [n.strip() for n in code_teile]
    fehlertyp = traceback_parts[-1].split(": ")[0]
    code = "; ".join(code_teile)

    if colored:
        flr = Fore.BRIGHT_RED
        fw = Fore.WHITE
        fm = Fore.MAGENTA
        fly = Fore.BRIGHT_YELLOW
        flb = Fore.BRIGHT_BLUE
        flc = Fore.BRIGHT_CYAN
    else:
        flr = ""
        fw = ""
        fm = ""
        fly = ""
        flb = ""
        flc = ""


    fehler_str = ""

    fehler_str += f"Fehler in der Funktion {flr}{functionname}{fw}" + "\n"
    fehler_str += f"\tDateipfad: \n\t\t{fm}{filepath}{fw}" + "\n"
    fehler_str += f"\tLinie:\n\t\t{fly}{line}{fw}" + "\n"
    fehler_str += f"\tCode:\n\t\t{flb}{code}{fw}" + "\n"
    fehler_str += f"\tArt:\n\t\t{flr}{fehlertyp}{fw}" + "\n"
    fehler_str += f"\tNachricht:" + "\n"
    wrapper = textwrap.TextWrapper(width=200, initial_indent="\t\t", subsequent_indent="\t\t")
    e_str = str(exception)
    if e_str.isspace() or e_str == "":
        e_str = "<Kein Text verfügbar>"
    word_list = wrapper.wrap(text=e_str)
    # colored_print each line.
    for element in word_list:
        fehler_str += flc + element + fw + "\n"
    
    return fehler_str


