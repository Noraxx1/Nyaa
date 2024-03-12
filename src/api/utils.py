#---- OTHERS ----#

def make_base():
    paths = os.getenv("PATH").split(os.pathsep)
    commands = []
    for path in paths:
        try:
            for entry in os.listdir(path):
                full_path = os.path.join(path, entry)
                if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                    commands.append(entry)
        except FileNotFoundError:
            pass 
    return commands

def append_to_fish_config(content):
    with open('~/.config/fish/config.fish', 'a') as config_file:
        config_file.write(content)


