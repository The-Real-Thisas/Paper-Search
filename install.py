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

install = Riposte(prompt="Install ? (y/n) ~: ")

@install.command("y")
def installation():
    install.status("◤ Creating Directories ◢")
    os.system("mkdir math" )
    os.system("mkdir physics" )
    os.system("mkdir chem" )
    os.system("mkdir bio" )
    os.system("mkdir em" )
    os.system("mkdir cs" )

    install.status("◤ Downloading Papers ◢")
    install.info(" ")
    print(" ")

    install.status("▷ Downloading Math Papers ")
    install.info(" ")
    print(" ")
    os.system("cd math && wget --recursive --level=1 --no-directories --no-host-directories --accept pdf 'https://papers.gceguide.com/IGCSE/Mathematics%20(0580)/' && cd ..")
    install.info(" ")
    print(" ")

    install.status("▷ Downloading Physics Papers ")
    install.info(" ")
    print(" ")
    os.system("cd physics && wget --recursive --level=1 --no-directories --no-host-directories --accept pdf 'https://papers.gceguide.com/IGCSE/Physics%20(0625)/' && cd ..")
    install.info(" ")
    print(" ")

    install.status("▷ Downloading Chemistry Papers ")
    install.info(" ")
    print(" ")
    os.system("cd chem && wget --recursive --level=1 --no-directories --no-host-directories --accept pdf 'https://papers.gceguide.com/IGCSE/Chemistry%20(0620)/' && cd ..")
    install.info(" ")
    print(" ")

    install.status("▷ Downloading Biology Papers ")
    install.info(" ")
    print(" ")
    os.system("cd bio && wget --recursive --level=1 --no-directories --no-host-directories --accept pdf 'https://papers.gceguide.com/IGCSE/Biology%20(0610)/' && cd ..")
    install.info(" ")
    print(" ")

    install.status("▷ Downloading Environmental Management Papers ")
    install.info(" ")
    print(" ")
    os.system("cd em && wget --recursive --level=1 --no-directories --no-host-directories --accept pdf 'https://papers.gceguide.com/IGCSE/Environmental%20Management%20(0680)/' && cd ..")
    install.info(" ")
    print(" ")

    install.status("▷ Downloading Computer Science Papers ")
    install.info(" ")
    print(" ")
    os.system("cd cs && wget --recursive --level=1 --no-directories --no-host-directories --accept pdf 'https://papers.gceguide.com/IGCSE/Computer%20Science%20(0478)/' && cd ..")
    install.info(" ")
    print(" ")

    install.success("Installation Succesful (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")

    exit()

@install.command("n")
def leave():
    install.status(" Okie, buiiiiiiiiiiii")
    install.status("(~˘▾˘)~")
    exit()

install.run()
