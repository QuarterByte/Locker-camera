# Locker-camera
A Raspberry Pi-powered camera system that fits right in your locker! The device starts recording whenever the locker is opened.

For my senior year of high school, I wanted a way to document some of my daily life without it feeling too intrusive or forced. I came up with the idea of having a camera in my locker that records whenever the door opens. That way, the locker captures moments from my day-to-day life and is out of the way enough so that it doesn't feel intentional.

The project used an Arducam 5 and Raspberry Pi 3B+, alongside an extra power bank I had lying around. A PIR sensor was added to detect when there was movement, and would trigger the camera to start recording. The setup would run for about a week without recharging the power bank. Additionally, I 3D printed a case that I found on Thingiverse that would cover both the camera and the Raspberry Pi. The case was made by ksamuelsen, and it can be found here: https://www.thingiverse.com/thing:3079477

Python was the language used to code this project to bring all of the hardware together. However, the code did not encode the video, which i chose to do seperately on a computer after transferring the videos from the Pi's SD card. This is because I found the process much quicker on a computer with a stronger graphics card than the Pi.
