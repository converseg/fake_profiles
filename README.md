# Fake Browsing History

- We have 5 fake profiles who each have a distinct and niche interest (see https://trackthis.link). After browsing for a while and building up a history (which includes searching for new homes and mortgage loans), we want to observe the loan-related ads presented to each profile. Are they targeted at their specific interests? 

- Using: Python, Selenium

## Setup
- `pip install selenium`
- To create FireFox profiles on Windows, go to Win --> Run --> firefox.exe -p --> Create Profile --> Choose Folder
- Note that the profile directories in profile.py will need to be edited to match the above profile destination

## Building Browsing history
Simply run `python script_browse.py --num_profiles 5 --save_history -t` from the terminal to have all profiles browse and save history.

## Manual Exploration
You can also browse on your own from the python terminal:
```python
from profile import Profile
p = Profile(0) # test profile
firefox_version = p.ff_version
firefox_install_path = p.ff_bin_path
profile_path = p.ff_profile_dir # browsing history saved here
persona = p.personality # using this alter ego on trackthis.link
p.start_browser()
p.driver.get('https://google.com')
p.save_browsing_history() # nothing will be saved unless this method is called
p.end_session() # closes all associated FireFox windows
```

## Testing
At test-time (after browsing history has been build up):
- Win --> Run --> path\_to\_ff\_installation -p --> select profile --> manually browse, observe ads
- Or load a `Profile(i)` similar to above
