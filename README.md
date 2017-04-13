Kanban-Stats
========
Design brief and description of program 
---
The idea is take a picture of your kanban board. The user defines their done column and red-bin stickies and task stickies. Each day the user takes a picture of their board lined up as per the kanban board layout. The software scans for and extracts task and red-bin stickies. A buffer and anti-buffer total is kept. Each task sticky is counted under the buffer with each red-bin sticky counted in the anti-buffer. A red-bin sticky is any piece of work that is technical debt : bug, code refactor, etc. The idea is to provide a low friction technique for managing Agile teams using visual managment. As we all know issue trackers are neat due to their historical analysis, but it is a pain to update both a visual board and issue tracker. Building upon the original code our goal is to provide indicator stats based upon a visual management board. This provides the best of both worlds visual managment with metrics.

**Note** The software is only compatible with blue, green, pink, yellow and purple post-its.

Hardware Required
---
- An android device for the compaion software.

Getting started
---
The following need to be installed

- [OpenCV](http://opencv.org/) version 2.3.1

Configuring config.json
---

- picDirectory:  The directory to where the files are kept. E.g. /home/pi/Post-Its/pi

