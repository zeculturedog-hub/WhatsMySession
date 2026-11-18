from ui import banner, credentials
from data import SESSIONS 
from rich.console import Console 
from rich.align import Align 
from rich.text  import Text 
import datetime
import os, time
import pyfiglet

console = Console()

while True:
    os.system("clear")

    def ask_yes_no(question):
        while True:
            console.print("\n")
            console.print(Align.center(Text(question, style="bold red")))

            answer = input("\n>").strip().lower()

            if answer in ["y", "yes"]:
                return True
            elif answer in ["n", "no"]:
                return False
            else:
                console.print(Align.center(Text("INVALID INPUT. PLEASE ENTER y OR n ONLY.", style="bold red")))
            

    def ask_choice(question, options):
        while True:     
            console.print("\n")
            console.print(Align.center(Text(question, style="bold red")))

            for key, value in options.items():
                line = f" {key}.{value}"
                console.print(Align.center(line))
            
            choice = input("\n>").strip()
            if choice in options:
                return choice
            else:
                console.print(Align.center(Text("INVALID INPUT. PLEASE CHOOSE A VALID OPTION.", style="bold red")))


    def get_today():
        return datetime.datetime.today().strftime("%A").lower()

    banner()
    credentials()

    year_choice = ask_choice(
        "WHAT YEAR ARE YOU?",
        {
            "1": "FIRST YEAR ",
            "2": "SECOND YEAR",
            "3": "THIRD YEAR ",
            "4": "FOURTH YEAR"
        }
    )
    YEAR_MAP = {
        "1": "year1",
        "2": "year2",
        "3": "year3",
        "4": "year4"
    }
    year = YEAR_MAP.get(year_choice)

    course_choice = ask_choice(
        "WHAT COURSE DO YOU TAKE?",
        {
            "1": "BIT ",
            "2": "BBA ",
            "3": "COET"
        }
    )
    COURSE_MAP = {
        "1": "bit",
        "2": "bba",
        "3": "coet"
    }
    course = COURSE_MAP.get(course_choice)

    today = get_today()

    confirm = ask_yes_no(f"DETECTED TODAY AS {today.capitalize()}. IS THIS CORRECT? (y/n)")

    if confirm:
        day = today
    else:
        day_choice = ask_choice(
            "SELECT THE DAY:",
            {
                "1": "MONDAY   ",
                "2": "TUESDAY  ",
                "3": "WEDNESDAY",
                "4": "THURSDAY ",
                "5": "FRIDAY   "
            }
        )
        DAY_MAP = {
            "1": "monday",
            "2": "tuesday",
            "3": "wednesday",
            "4": "thursday",
            "5": "friday"
        }
        day = DAY_MAP.get(day_choice)

    sessions = SESSIONS.get(year, {}).get(course, {}).get(day, {})
    morning = sessions.get("morning", [])
    lunch = sessions.get("lunch", [])

    console.print("\n")
    console.print(Align.center(
        Text(f"IT'S {day.upper()} AND YOU HAVE", style="bold red")
    ))

    def show(period, items):
        if items:
            return ", ".join(items)
        return "NO SESSION"

    console.print(Align.center(f"MORNING: {show('morning', morning)}"))
    console.print(Align.center(f"LUNCH  : {show('lunch', lunch)}"))

    def restart_or_quit():
        while True:
            console.print("\n")
            console.print(Align.center(Text("WHAT WOULD YOU LIKE TO DO NEXT?", style="bold red")))
            console.print(Align.center("1. CHECK AGAIN"))
            console.print(Align.center("2. QUIT       "))

            choice = input("\n> ").strip()

            if choice == "1":
                os.system("clear")
                return True
            elif choice == "2":
                smol = pyfiglet.Figlet(font="slant")
                tet = smol.renderText("BYE CHAMP!")
                console.print(Align.center(Text(tet, style="bold purple")))
                time.sleep(2)
                os.system("clear")
                exit()
            else:
                console.print(Text("INVALID CHOICE. PLEASE SELECT 1 OR 2.", style="bold red"))

    if not restart_or_quit():
        break
