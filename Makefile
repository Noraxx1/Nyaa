help:
	@echo "make fishy [for fish shell]"
	@echo "make bash [for bash shell]"
	@echo "make uninstall [to remove nyaa~ from your system]"
	@echo "make help [to show this help menu]"

fishy:
	@command -v python3 >/dev/null 2>&1 || { echo >&2 "Python 3 is not installed or not in PATH. Aborting."; exit 1; }
	@echo "Installing for fish..."

	mkdir -p ~/.local/share/nyaa
	cp -r src/* ~/.local/share/nyaa
	@echo "Installation complete"

bash:
	@echo "currently bash is not implemented yet.."

uninstall:
	@echo "why you awe wefting us,me sad :( now"
	@echo "oh yeah i also edited your fish config sowwy"

	rm -r ~/.local/share/nyaa
install:
	@echo "you shouldnt use make install instead use:"
	@echo "make fishy [for fish shell]"
	@echo "make bash [for bash shell]"


