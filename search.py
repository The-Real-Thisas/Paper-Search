from riposte import Riposte
import os

print(r"""
 ________  ___  ___       ________  ___        _______      ________
|\   __  \|\  \|\  \     |\   __  \|\  \      /  ___  \    |\   __  \
\ \  \|\ /\ \  \ \  \    \ \  \|\  \ \  \    /__/|_/  /|   \ \  \|\  \
 \ \   __  \ \  \ \  \    \ \   __  \ \  \   |__|//  / /    \ \  \\\  \
  \ \  \|\  \ \  \ \  \____\ \  \ \  \ \  \____  /  /_/__  __\ \  \\\  \
   \ \_______\ \__\ \_______\ \__\ \__\ \_______\\________\\__\ \_______\
    \|_______|\|__|\|_______|\|__|\|__|\|_______|\|_______\|__|\|_______|

""")

print("VERSION: 1.1")
print("Author: Thisas")
print("""
NOTE: Type help for help.
""")

papersearch = Riposte(prompt="Subject:~$ ")

@papersearch.command("help")
def search():
    print("""
    ◤ Subjects Avalible ◢
    ▷ math (Maths)
    ▷ physics (Physics)
    ▷ chem (Chemistery)
    ▷ bio (Biology)
    ▷ em (Environmental management)
    ▷ cs (Computer Science)

    ◤ NOTE ◢
    ▷ Type 'exit' to leave.
    ▷ DO NOT USE ' IN YOUR SEARCH.
    """)

@papersearch.command("version")
def search():
    print("""
    ◤ VERSION: 1.1 ◢

    """)

@papersearch.command("math")
def search():
    term = input("Search: ")
    os.system("cd math" )
    os.system("pdfgrep -n '" + term + "' *.pdf" )

@papersearch.command("physics")
def search():
    term = input("Search: ")
    os.system("cd physics" )
    os.system("pdfgrep -n '" + term + "' *.pdf" )

@papersearch.command("chem")
def search():
    term = input("Search: ")
    os.system("cd chem" )
    os.system("pdfgrep -n '" + term + "' *.pdf" )

@papersearch.command("bio")
def search():
    term = input("Search: ")
    os.system("cd chem" )
    os.system("pdfgrep -n '" + term + "' *.pdf" )

@papersearch.command("em")
def search():
    term = input("Search: ")
    os.system("cd em" )
    os.system("pdfgrep -n '" + term + "' *.pdf" )

@papersearch.command("cs")
def search():
    term = input("Search: ")
    os.system("cd cs" )
    os.system("pdfgrep -n '" + term + "' *.pdf" )

@papersearch.command("exit")
def leave():
    exit()

papersearch.run()
