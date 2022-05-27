import webbrowser
import subprocess
import Devlog

def parse_command(command_action, argument=""):


  if command_action[0:3]=="web":
    open_link(command_action[4:], argument)
    Devlog.speak("Pesquisando " + argument)
  elif command_action[0:4]=="path":
    open_program(command_action[5:])
    Devlog.speak("Abrindo " + argument)
  elif command_action=='commands':
    reload_commands()
    Devlog.speak("Atualizado")


def open_link(link, argument=""):
  print(f'{link}/search?q={argument}')
  webbrowser.get('windows-default').open_new(f'{link}/search?q={argument}')

def open_program(path):
  subprocess.Popen([path, '-new-tab'])

def reload_commands():
  Devlog.read_commands_file()