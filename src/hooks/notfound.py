import sys, subprocess, os

# we import settings,and useful scripts
sys.path.append(os.path.expanduser('~/.local/share/nyaa'))
from api import models, utils
import main

# we get the similar command to the one provided as the laucnh arg. #
similar=models.get_similar(input_word=sys.argv[1], database=utils.make_base(), similarity_type=main.find_type)


# we also get the input based on the similar word that we got before #
choose=input(f"Did you mean: {similar}[{main.prompt}]:")


# simple function to run a comand like a normal terminal user would #
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, _ = process.communicate()
    return output.decode('utf-8')




if choose != main.prompt_accept and not choose.strip().isspace() and choose:
    print("cancelled...")
    sys.exit()



# here we check if theres any additional arg. to the command and we also run that,if found #
if len(sys.argv) < 2:
    command = similar
else:
    command = similar + " " + sys.argv[2]

print(run_command(command))
sys.exit()