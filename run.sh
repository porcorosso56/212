#!/usr/bin/env bash

sudo pacman -S --needed docker
sudo systemctl start docker

cd dumper
sudo docker build . -t dumper
sudo docker run -it dumper