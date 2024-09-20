#!/bin/bash
FILE=install.log
if [ -f "$FILE" ]; then
    echo "$FILE is already exist" >> ${FILE}
    rm ${FILE}
fi

echo "Pip version..." >> ${FILE}
pip --version >> ${FILE}
echo "Create local_lib directory" >> ${FILE}
mkdir -p "local_lib"
if [ ! -d "local_lib/path" ]; then
    echo "Move to local_lib..." >> ${FILE}
    cd local_lib
    echo "Cloning the repository..." >> ../${FILE}
    git clone git@github.com:jaraco/path.git
    echo "The repository is cloned" >> ../${FILE}
    cd ..
else
    echo "Repository is already cloned..." >> ${FILE}
fi
echo "Finish" >> ${FILE}