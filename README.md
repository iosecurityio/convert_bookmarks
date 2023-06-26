# convert_bookmarks

ChatGPT's rendition of converting a 'Bookmarks' json configuration file into an HTML export file allowing Import into Browsers.

## Use case:

- A coworkers laptop crashed, however they were still able to recover files from the hard drive

- Coworker wanted to recover what they could from their stored Browser configurations

- With no GUI, they were not able to Export their Bookmarks into the required HTML format for future imports

- The `Bookmarks` file recovered from the Browser's saved files is a .json configuration

- In this scenario, a browser will only allow you to Import a `Bookmarks.html` file

- The script will poorly mimic the Browser's Export as HTML functionality to convert .json to .html

- Import your new `Bookmarks.html` to recover bookmarks. (Disclaimer: You will still be upset that your computer crashed no matter how many bookmarks you recover)

- Describing the scenario to ChatGPT basically one-shot output this script, and with a tweak to one line of code, it ran successfully on first attempt

- Also note that nowadays, if you login to the Browser itself and sync a profile, this can largely be avoided altogether
