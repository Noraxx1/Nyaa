


# - - - - - - * WARNING * - - - - #
# you can change the output in co #
# sole but dont edit the last lin #
# e it should be the runner one!! #
# - - - - - - - - - - - - - - - - - 

function not_found --on-event fish_command_not_found
    set cmd $argv[1] # latest runned command
    set args $argv[2..-1] # latest command args excluded the first

    echo "Command not found: $cmd $args"

    # runner:
    python3 -/./local/share/nyaa/hooks/notfound.py $cmd
end