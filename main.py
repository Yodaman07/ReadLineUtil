from InputHandler import InputHandler
from LineUtil import LineUtil

util = LineUtil(".", 7, 25)
handler = InputHandler(util)

while True:
    cmd = input(">>> ")
    if cmd is not "":
        handler.handleInput(cmd)
