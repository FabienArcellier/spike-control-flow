import alfred

@alfred.command("shell", help="execute an interactive shell")
def shell():
    """
    execute the application

    >>> $ alfred shell
    """
    alfred.run("python src/app/shell.py")
