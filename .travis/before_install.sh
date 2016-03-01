#!/bin/bash

set -e
set -x

if [ "$TRAVIS_OS_NAME" = osx ]; then
    brew update >/dev/null
    brew tap homebrew/science
    curl -L -O https://bintray.com/artifact/download/casacore/homebrew-bottles/casacore-2.0.3.el_capitan.bottle.tar.gz
    brew install ./casacore-2.0.3.el_capitan.bottle.tar.gz
else
   sudo apt-get update -qq
   sudo apt-get install software-properties-common python-setuptools libboost-python-dev libcfitsio3-dev
   sudo add-apt-repository -y ppa:radio-astro/main
   sudo apt-get update -qq
   sudo apt-get install libcasacore2-dev casacore-data
fi
