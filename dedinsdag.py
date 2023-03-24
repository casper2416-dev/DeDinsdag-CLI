from click import group

from programs.list import *

@group
def commands():
    pass

commands.add_command(list)

if __name__ == "__main__":
    commands()
