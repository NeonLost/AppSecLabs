# Simple RCE example

This lab shows how to easy exploit python deserialization with vulnerable library. 

If you want to have relax - just build main `Dockerfile`

If you want to have geek porn - build `Dockerfile-LPE`

If you are using ubuntu and do know nothing about docker - run `sudo sh build.sh`

Be carefull and do not run build.sh, if you are using docker for any other purposes (it removes all containers and images)

## Core idea
You have an application with 2 methods:
- */*
with parameter `name`
- */log*
with parameter `some`

You need to:
1. Became root on host machine and create new sudo user

2. Combine founded vulnerability with some old attack to hide yourself
