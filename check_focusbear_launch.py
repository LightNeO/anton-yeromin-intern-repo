import time
import os
from pywinauto.application import Application
from pywinauto import Desktop

APP_PATH = r"C:\Program Files (x86)\Focus Bear\Focus Bear.exe"


def main():
    print("=== Start ===")

    print("🔪 Killing old Focus Bear processes...")
    os.system('taskkill /f /im "Focus Bear.exe" >nul 2>&1')
    time.sleep(2)  # Даємо час на закриття

    os.environ["WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS"] = "--remote-debugging-port=9222"

    print("🚀 Launching app with debug port 9222...")

    # Важливо: Програма має запускатися ПІСЛЯ встановлення змінної
    # Також переконайся, що Focus Bear повністю закритий перед запуском!
    app = Application(backend="uia").start(APP_PATH)

    ####

    print("Waiting for the app to launch...")
    main_window = app.window(title_re="Focus Bear")
    main_window.wait("visible", timeout=15)

    print("Clicking 'Continue' button...")
    main_window.child_window(
        auto_id="buttonContinueText", control_type="Text"
    ).click_input()

    time.sleep(2)

    print("Opening System Tray...")
    desktop = Desktop(backend="uia")
    taskbar = desktop.window(class_name="Shell_TrayWnd")

    chevron = taskbar.child_window(title="Show Hidden Icons", control_type="Button")
    chevron.click_input()

    time.sleep(10)

    overflow_window = desktop.window(class_name="TopLevelWindowForOverflowXamlIsland")

    print("Clicking Tray Icon...")
    tray_icon = overflow_window.child_window(title="Focus Bear", control_type="Button")
    tray_icon.click_input()

    print("Waiting for menu to appear...")
    time.sleep(2)

    menu_window = desktop.window(
        title="Focus Bear", control_type="Window", found_index=0
    )
    menu_window.wait("visible", timeout=5)

    print("Clicking 'To Do List' button...")

    todo_btn = menu_window.child_window(auto_id="btnToDoPlayer")
    todo_btn.click_input()

    print("=== Finished ===")


if __name__ == "__main__":
    main()
