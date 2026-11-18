from rich.console import Console 
from rich.align import Align
from rich.text import Text
import pyfiglet
import time 
import shutil 

console = Console()

def banner():
    width, _ = shutil.get_terminal_size()
    small = pyfiglet.Figlet(font="slant")
    big = pyfiglet.Figlet(font="big")

    title_small = small.renderText("What's my")
    title_big = big.renderText("SESSION")

    console.print(Align.center(Text(title_small, style="bold red")))
    console.print(Align.center(Text(title_big, style="bold purple")))
    time.sleep(2)

def credentials():
    console.print(Align.center(Text("POWERED BY COLLINS TECHNOLOGY.....", style="bold red")))
    time.sleep(2)