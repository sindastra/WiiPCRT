#### Inspired by a Wii I bought second-hand which had a parental-control pin set...

### I present to you, **WiiPCRT!** The tool to generate a master key to unlock your parental-control on your Wii!

# How it works:
1. Navigate to the Wii Menu by pressing the HOME button on a Wii Remote and selecting "Wii Menu."
2. Look at the date and time displayed on the Wii Menu and ensure they are correct. If incorrect, they will need to be changed in order for you to complete the PIN reset process. You will not be able to reset the PIN until the date is correct.
3. Select the Wii Options icon in the lower-left corner of the Wii Channel Menu.
4. Select "Wii Settings."
5. Click on the blue arrow to reach the Wii System Settings 2 menu options.
6. Select "Parental Controls," then "Yes."
7. Select "I forgot."
8. Select "I forgot." again.
9. A screen with an 8 digit request code will appear, write it down!
10. Download the latest release of WiiPCRT [HERE](https://github.com/sindastra/WiiPCRT/releases).
11. Open a CMD (Command Prompt) and navigate to the folder where you downloaded the reset_tool to.
12. Run the reset_tool and pass the request code you wrote down as argument.

### Example (in CMD):
```
reset_tool.exe 12345678
```

13. Choose the master key based on your time zone (date) from the output.
14. Enter the master key into your Wii.

### Enjoy your unlocked Wii!

###### Copyright (C) 2018 Sindastra. All rights reserved. This site is not affiliated with Nintendo.
