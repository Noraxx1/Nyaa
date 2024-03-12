import subprocess
import os

def fish_setup():
    append_to_fish_config(f'''
function fish_command_not_found --on-event fish_command_not_found
    set cmd $argv[1]
    echo "Command not found: $cmd"
    python3 ~/.local/share/nyaa/call_notfound.py $cmd
end
''')