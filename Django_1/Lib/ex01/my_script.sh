#!/bin/bash

FILE=install.log

if [ -f ${FILE} ]; then
    rm ${FILE}
fi

touch install.log

echo "[SCRIPT EXECUTED]" >> ${FILE}
echo "Pip version..." >> ${FILE}
pip --version >> ${FILE}
echo "Create local_lib directory..." >> ${FILE}
mkdir -p local_lib

if [ -d "local_lib/path" ]; then
    rm -rf local_lib/path
fi

echo "Clone path.py library..." >> ${FILE}
cd local_lib
git clone git@github.com:jaraco/path.git 
cd ..
echo "Path.py was clone..." >> ${FILE}
echo "Install is over !" >> ${FILE}

echo "Launch the program..." >> ${FILE}
./my_program.py

