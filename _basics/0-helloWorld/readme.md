#Kivy needs

Install Cython and Kivy

- sudo pip install Cython
- sudo pip install Kivy 
- go to hiKivy

Manual installation (On Raspbian Jessie/Stretch)
https://kivy.org/docs/installation/installation-rpi.html

Install the dependencies:

    sudo apt-get update
    sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
       pkg-config libgl1-mesa-dev libgles2-mesa-dev \
       python-setuptools libgstreamer1.0-dev git-core \
       gstreamer1.0-plugins-{bad,base,good,ugly} \
       gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
       xclip xsel

Install a new enough version of Cython:

    sudo pip install -U Cython==0.27.3

Install Kivy globally on your system:

    sudo pip install git+https://github.com/kivy/kivy.git@master

Or build and use kivy inplace (best for development):

    git clone https://github.com/kivy/kivy
    cd kivy

    make
    echo "export PYTHONPATH=$(pwd):\$PYTHONPATH" >> ~/.profile
    source ~/.profile


https://github.com/mrichardson23/rpi-kivy-screen
http://mattrichardson.com/kivy-gpio-raspberry-pi-touch/index.html