📱 LumiaSend
Bridge the gap between your PC and your Windows Phone.

LumiaSend is a lightweight local server designed to make transferring text, links, and files to legacy Windows Phone 8.1 and Windows 10 Mobile devices effortless. No cloud, no account—just pure local network speed.

🚀 Features
Instant Text/Link Sharing: Send URLs or snippets from your PC to your phone's clipboard.

File Transfers: Push photos, documents, and installers (.appx/.xap) directly to your device.

Low Overhead: Runs on a tiny Python backend that doesn't slow down your PC.

Privacy Focused: Everything stays on your local Wi-Fi.

🛠️ Requirements
On your PC:
Python 3.10+ (Ensure you check "Add to PATH" during installation)

Local Network: Both PC and Lumia must be on the same Wi-Fi.

On your Lumia:
InterOp Unlocked or Developer Mode enabled.

Wi-Fi Connectivity.

📥 Getting Started
1. Installation
The easiest way to set up the environment is to use the included batch script:

Download this repository as a ZIP and extract it.

Double-click Setup_LumiaSend.bat.

If Python is missing, it will open the download page for you.

Once the setup is complete, you are ready to go.

2. Launching the Server
Double-click LumiaSend_Launcher.exe (or run python server.py).

A command window will open showing your Local IP Address (e.g., 192.168.0.167).

3. Connect your Phone
Open the LumiaSend app on your Windows Phone.

Enter the IP Address shown on your PC screen into the app settings.

Tap Connect.

📂 Repository Structure
/app: Contains the .appx / .xap files for the Lumia.

/server: The Python backend files.

Setup_LumiaSend.bat: One-click requirement installer.

LumiaSend_Launcher.exe: The easy-start executable.

server.py: The core server logic.

⚖️ License
This project is open-source and shared with the Lumia community. Feel free to modify and improve it!

Pro-Tip for GitHub:
When you upload your files, make sure to go to the "Releases" section on the right side of the GitHub page. Upload your LumiaSend_Launcher.exe and the .appx file there so people can find them easily without digging through the source code.

Would you like me to write a short "Community Post" for Telegram or Reddit that links to this repository?
