import subprocess

def install_package(package):
    subprocess.check_call(["python", "-m", "pip", "install", package])

def show_message():
    message = """
    *************************************
    *                                   *
    *  Welcome! Check out our services  *
    *     at Fiverr or on Telegram     *
    *                                   *
    *************************************
    """

    print(message)

def redirect_to_link(link):
    import webbrowser
    webbrowser.open_new_tab(link)

if __name__ == "__main__":
    try:
        import webbrowser
    except ImportError:
        print("webbrowser module not found. Installing...")
        install_package("webbrowser")
        import webbrowser
    
    show_message()
    choice = input("Press 1 to visit Fiverr, 2 to visit Telegram: ")

    if choice == "1":
        redirect_to_link("https://www.fiverr.com/s/b4k1lN")
    elif choice == "2":
        redirect_to_link("https://telegram.me/tradingbot_developer")
    else:
        print("Invalid choice. Exiting...")
