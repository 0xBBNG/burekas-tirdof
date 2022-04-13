# burekas_tirdof
Web scanner for finding vulnerabilities and information leakage in Israeli sites, inspired by Cyber-Cyber podcast.

Key notes:
1. If you want to add your own searches you will need to update "search_db.py" and maybe also the "search Parameters" section.
2. You'll need to change the variable "driver_path_win"/"driver_path_mac" to your chrome driver full path.

Requirements:
1. MacOS / Windows
2. python3
3. selenium (pip/pip3 install selenium)
4. chromedriver (I've used version 99.0.4844.51, https://chromedriver.storage.googleapis.com/index.html)
-- In MacOS you'll need to give access to web driver: System Preferences > Security & Privacy
5. fake-useragent (pip install fake-useragent)
6. Disable Protected content: Go to the Setting in Chrome and write “site settings” in the search bar > Move into the Site settings And search for the “Protected content IDs” > Move into the protected content and disable it.
7. Beautiful Soup (pip install beautifulsoup4)