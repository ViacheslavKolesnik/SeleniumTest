# Getting facebook friends with Selenium
## Description
Opens web browser with chrome web driver.

Navigates to facebook login page.

Fills login and password fields.

Clicks submit button.

Closes overlay popup.

Navigates to profile.

Navigates to friends tab.

Counting friends.

Gets friends names if friends present.

Report with friends names.
## Requirements
- python 3.7:
    - libraries: `requirements.txt`
- google chrome
- chrome driver
## Run steps(Linux)
Install google chrome and chrome driver:
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb
LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip
unzip chromedriver_linux64.zip && sudo ln -s $PWD/chromedriver /usr/local/bin/chromedriver
```
Install python.

Install additional modules: `python -m pip install -r ./requirements.txt`

Edit configs if needed.

Browse to root project directory and run following in command line: `python launcher.py`.
## Run example
Log:
```
2019-04-29 20:17:55,252 [INFO]: Logger successfully set up.
2019-04-29 20:17:55,252 [INFO]: Creating web driver.
2019-04-29 20:17:56,476 [INFO]: Opening https://www.facebook.com/.
2019-04-29 20:18:04,170 [INFO]: Waiting for email field to be clickable.
2019-04-29 20:18:04,227 [INFO]: Writing email.
2019-04-29 20:18:04,444 [INFO]: Waiting for password field to be clickable.
2019-04-29 20:18:04,488 [INFO]: Writing password.
2019-04-29 20:18:04,869 [INFO]: Waiting for login button to be clickable.
2019-04-29 20:18:05,175 [INFO]: Clicking login button.
2019-04-29 20:18:14,293 [INFO]: Closing popup.
2019-04-29 20:18:14,392 [INFO]: Waiting for profile to be clickable.
2019-04-29 20:18:14,573 [INFO]: Clicking profile.
2019-04-29 20:18:14,974 [INFO]: Waiting for friends tab to be clickable.
2019-04-29 20:18:19,177 [INFO]: Clicking friends tab.
2019-04-29 20:18:19,329 [INFO]: Counting friends.
2019-04-29 20:18:21,954 [INFO]: You have 4 friends.
2019-04-29 20:18:21,954 [INFO]: Getting friends names.
2019-04-29 20:18:22,050 [INFO]: Reporting.
2019-04-29 20:18:22,050 [INFO]: Finishing Selenium test.
2019-04-29 20:18:22,050 [INFO]: Closing driver.
```
Report:
```
Report:
-Friends:
--Дмитрий Солонцевой
--Kostya Panchenko
--Artem Sysa
--Dmitry Shekhovtsov
```