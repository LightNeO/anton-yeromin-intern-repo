import os
import time
from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto import timings

APP_PATH = r"C:\Program Files (x86)\Focus Bear\Focus Bear.exe"
timings.Timings.window_find_timeout = 10


def click_input_with_retry(element, max_retries=3, wait_time=2):
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt} to click...")
            element.click_input()
            return True
        except Exception as e:
            print(f"Click failed: {e}")
            if attempt < max_retries:
                print(f"Waiting {wait_time}s before retrying...")
                time.sleep(wait_time)
            else:
                print("❌ Max retries reached. Failing test.")
                raise


def main():
    print("=== Start ===")

    print("Killing old Focus Bear processes...")
    os.system('taskkill /f /im "Focus Bear.exe" >nul 2>&1')

    os.environ["WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS"] = "--remote-debugging-port=9222"

    print("🚀 Launching app with debug port 9222...")

    app = Application(backend="uia").start(APP_PATH)

    print("Waiting for the app to launch...")
    main_window = app.window(title_re="Focus Bear")
    # main_window.wait("visible", timeout=15) - this was replased with a click_input_with_retry function
    print("Clicking 'Continue' button...")
    continue_btn = main_window.child_window(
        auto_id="buttonContinueText", control_type="Text"
    )
    click_input_with_retry(continue_btn)

    print("Opening System Tray...")
    desktop = Desktop(backend="uia")
    taskbar = desktop.window(class_name="Shell_TrayWnd")

    chevron = taskbar.child_window(title="Show Hidden Icons", control_type="Button")
    chevron.click_input()

    overflow_window = desktop.window(class_name="TopLevelWindowForOverflowXamlIsland")

    print("Clicking Tray Icon...")
    tray_icon = overflow_window.child_window(title="Focus Bear", control_type="Button")
    tray_icon.click_input()

    print("Waiting for menu to appear...")

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
