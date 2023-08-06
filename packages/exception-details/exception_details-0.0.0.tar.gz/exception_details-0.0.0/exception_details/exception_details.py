
import sys
import textwrap
import traceback

from colorful_terminal import *


def print_exception_details(exception: Exception):
    """Print the exception details.\n
    Usage:\n
        `try:`\n
        `    ... `\n
        `except Exception as e: `\n
        `    print_exception_details(e)`\n

    Contains:
    - function name
    - filepath
    - line
    - code snippet
    - species of the exception
    - message

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

    colored_print(f"Exception in the function {Fore.BRIGHT_RED}{functionname}{Fore.WHITE}")
    colored_print(f"\tFilepath: \n\t\t{Fore.MAGENTA}{filepath}{Fore.WHITE}")
    colored_print(f"\tLine:\n\t\t{Fore.BRIGHT_YELLOW}{line}{Fore.WHITE}")
    colored_print(f"\tCode:\n\t\t{Fore.BRIGHT_BLUE}{code}{Fore.WHITE}")
    colored_print(f"\tSpecies:\n\t\t{Fore.BRIGHT_RED}{fehlertyp}{Fore.WHITE}")
    colored_print(f"\tMessage:")    
    wrapper = textwrap.TextWrapper(width=200, initial_indent="\t\t", subsequent_indent="\t\t")
    e_str = str(exception)
    if e_str.isspace() or e_str == "":
        e_str = "<Kein Text verfügbar>"
    word_list = wrapper.wrap(text=e_str)
    # colored_print each line.
    for element in word_list:
        colored_print(Fore.BRIGHT_CYAN + element + Fore.WHITE)



def get_exception_details_dict(exception: Exception):
    """Get the exception details as a dictionary.\n
    Usage:\n
        `try:`\n
        `    ... `\n
        `except Exception as e: `\n
        `    details = get_exception_details_dict(e)`\n
        
    Contains:
    - 'function' -> function name
    - 'path' -> filepath
    - 'line' -> line
    - 'code' -> code snippet
    - 'species' -> species of the exception
    - 'message' -> message

    Args:
        exception (Exception): Your Exception

    Returns:
        dict: Exception details as a dictionary with the keys: "function", "path", "line", "code", "species", "message"
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
        "species": fehlertyp,
        "message": e_str
    }
    return details



def get_exception_details_str(exception: Exception, colored:bool=True):
    """Print the exception details.\n
    Usage:\n
        `try:`\n
        `    ... `\n
        `except Exception as e: `\n
        `    details = get_exception_details_str(e)`\n

    Contains:
    - function name
    - filepath
    - line
    - code snippet
    - species of the exception
    - message

    Args:
        exception (Exception): Your Exception
        colored (boolean): The string has coloreds parts if True.
    
    Returns:
        str: Exception details as a string."
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

    fehler_str += f"Exception in the function {flr}{functionname}{fw}" + "\n"
    fehler_str += f"\tFilepath: \n\t\t{fm}{filepath}{fw}" + "\n"
    fehler_str += f"\tLine:\n\t\t{fly}{line}{fw}" + "\n"
    fehler_str += f"\tCode:\n\t\t{flb}{code}{fw}" + "\n"
    fehler_str += f"\tSpecies:\n\t\t{flr}{fehlertyp}{fw}" + "\n"
    fehler_str += f"\tMessage:" + "\n"
    wrapper = textwrap.TextWrapper(width=200, initial_indent="\t\t", subsequent_indent="\t\t")
    e_str = str(exception)
    if e_str.isspace() or e_str == "":
        e_str = "<Kein Text verfügbar>"
    word_list = wrapper.wrap(text=e_str)
    len_word_list = len(word_list)
    for i, element in enumerate(word_list):
        fehler_str += flc + element + fw 
        if i != len_word_list-1: fehler_str += "\n"
    
    return fehler_str


