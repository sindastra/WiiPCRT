## The tool to generate a master key to unlock your parental controls on your Wii!

##### (...Inspired by a Wii I bought second-hand which had a parental-control pin set...)

# How it works:
1. Navigate to the Wii Menu by pressing the HOME button on a Wii Remote and selecting "Wii Menu."
2. Look at the date and time displayed on the Wii Menu and ensure they are correct. If incorrect, they will need to be changed in order for you to complete the PIN reset process. You will not be able to reset the PIN until the date is correct. [[HOW TO]](https://tinyurl.com/ybq5md73)
3. Select the Wii Options icon in the lower-left corner of the Wii Channel Menu.
4. Select "Wii Settings."
5. Click on the blue arrow to reach the Wii System Settings 2 menu options.
6. Select "Parental Controls," then "Yes."
7. Select "I forgot."
8. Select "I forgot." again.
9. A screen (as pictured below) with an 8 digit request code will appear, write it down!
10. Download the latest release of WiiPCRT [[HERE]](https://github.com/sindastra/WiiPCRT/releases).
11. Run the "reset_tool" which you just downloaded.
12. Enter the request code which you have written down earlier.
13. Choose the master key based on your time zone (date) from the output.
14. Enter the master key into your Wii.

### Enjoy your unlocked Wii!

# Additional notes:

* If you get any errors about missing DLLs, try installing the vcredist files (all of them) from [[HERE (vcrun2008)]](https://www.microsoft.com/en-us/download/details.aspx?id=29) and [[HERE (vcrun2010)]](https://www.microsoft.com/en-us/download/details.aspx?id=5555).
* The button at the top leads to the GitHub page... You can report bugs/issues there!
* Yes, this runs under wine, if you must...
* This is what a request code screen looks like on your Wii:

![sample-screen](request_sample.png "Screen on your Wii")

### You can also pass the request code as argument:
#### Windows CMD (Command Prompt):
```
> reset_tool.exe 12345678
```
#### On BSD, Darwin, Linux, Unix, etc. (requires Python, duh):
```
$ ./reset_tool.py 12345678
```

# Supporting this project:
* Report bugs/issues on the GitHub page.
* Share good ideas for interesting features.
* Donate Bitcoin to [1P5c5zrgAawGAKqQaN9fMeY13vG9AEcjy6](https://blockchain.info/payment_request?address=1P5c5zrgAawGAKqQaN9fMeY13vG9AEcjy6)

###### Copyright (C) 2018 Sindastra. All rights reserved. This site is not affiliated with Nintendo.
