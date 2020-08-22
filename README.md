#Gnome Wallpaper Updater
Simple Python3 script that takes in a file path or url of an image and sets it as a wallpaper for GNOME. My specific use 
case is to poll a URI that dynamically updates so I can have a ever changing wallpaper of a satellite image inspired by 
the macOS [Downlinkapp](https://downlinkapp.com/). By default the wallpaper is downloaded to /tmp/latest_wallpaper and 
set to there.

##Usage
####Basic Usage (Works in crontab)
```
$ python -m venv env
$ source ./env/bin/activate 
$ pip install -r requirements.txt
$ ./gnome_wallpaper_updater.py https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png
```
####Other Options (WIP doesn't work in crontab)
Choosing the picture option to use, the default will be scaled. To find your available options execute (output is an example)
```
$ gsettings range org.gnome.desktop.background picture-options
enum
'none'
'wallpaper'
'centered'
'scaled'
'stretched'
'zoom'
'spanned'

$ ./gnome_wallpaper_updater.py https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png zoom
```
##Cron
This is mostly for my use case but maybe someone else may find it useful
```
$ crontab -e
# poll this url every 20 minutes
*/20 * * * * /path/to/gnome_wallpaper_updater.py https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/latest.jpg
```