# small-toys

some simple things for playing

## happy_birthday

### introduction

a simple music player and turtle drawing of happy birthday
**This repository provides a wrapper for a program[https://pythondex.com/python-program-to-wish-happy-birthday-with-code]**

![effect](https://s2.loli.net/2022/05/18/OKczTYmHoiwdbrG.png)

you may could download your music in https://www.1happybirthday.com/ which could giving you a music with a name

### Play turtorial

download and run happy.exe

### Custom tutorial

#### change other

{speed of drawing}: You need to change turtle.speed(0.51) in the code      [https://www.geeksforgeeks.org/turtle-speed-function-in-python/]



#### change music and mark

##### way 1: 
1. clone warehouse
2. adding your custom music to /res
3. A quick change to the music related part of the code
4. `pyinstaller -D/F[choice one in two] -w happy.py`  package code file only
5. delete folders(dist, build) in the root directory of this program
6. change `happy.spec' line 11 -> datas=[('res', 'res')],
7. `pyinstaller happy.spec`

##### way 2:
only do step 1, 2, 7 in way 1

### Appendix

@Reference:

    code                https://pythondex.com/python-program-to-wish-happy-birthday-with-code
    
    import mp3 media    https://blog.csdn.net/weixin_42581655/article/details/124789762
    
@source:

    birthday song       https://www.1happybirthday.com/; https://music.163.com/
