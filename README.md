# CamJam-Edukit3
Test software for CamJam EduKit3 robot

The robot is controlled remotely through SSH, with a wifi adapter.

The keyboard handling is done with pygame, which need an active window to be fucntionnal.
So the SSH session has to be opened with X support (using -X option), then focus has to be set on the window at startup.

Then following keys are handled:
- up, down, left, right arrows for direction
- 'v' and 'b' keys for fast turning
- SPACE for stopping
- ESCAPE to exit the application
