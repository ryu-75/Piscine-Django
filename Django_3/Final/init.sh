#!/bin/bash

# Définir des couleurs
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
CYAN='\e[36m'
RESET='\e[0m'

echo -e "🛠️ Creating a virtualenv... 🛠️"
python3 -m venv django_venv

if [ -d "django_venv" ]; then
    echo -e "✅ ${GREEN}Django_venv is created !${RESET}"
else
    echo -e "❌ ${RED}Failed to create django_venv${RESET}"
    exit 1
fi

echo "================================================================"
echo "Activate virtualenv..."
source django_venv/bin/activate

if [ "$VIRTUAL_ENV" != "" ]; then
    echo -e "✅ ${GREEN}Django_venv is activated!${RESET}"
else
    echo -e "❌ ${RED}Failed to activate django_venv${RESET}"
    exit 1
fi

echo "================================================================"
echo "🔄 Verifying if pip is updated... 🔄"

current_pip_version=$(pip --version | awk '{print $2}')
updated_pip_version=$(pip install --upgrade pip | grep "Requirement already satisfied: pip in" | awk '{print $7}' | tr -d '()')

if [ $current_pip_version = $updated_pip_version ]; then
    echo -e "✅ ${GREEN}Pip is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}Pip is outdated! Updating...${RESET}"
    pip install --upgrade pip
    echo -e "🚀 ${YELLOW}Pip updated to $updated_pip_version!${RESET}"
fi

echo "================================================================"
echo "🚀 Installing Django..."
pip install django

if pip show django > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}Django is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install Django${RESET}"
    exit 1
fi

# Get the installed version of Django
installed_version=$(pip show django | grep Version | awk '{print $2}')
# Get the latest version of Django from PyPI
latest_version=$(pip install django --upgrade | grep "Requirement already satisfied: django in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}Django is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}Django is outdated! Updating...${RESET}"
    pip install --upgrade django
    echo -e "🚀 ${YELLOW}Django updated to $latest_version!${RESET}"
fi

echo "================================================================"
echo "🚀 Installing psycopg2..."
pip install psycopg2-binary

test=$(pip show psycopg2-binary > /dev/null 2>&1)
echo $test

if pip show psycopg2-binary > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}psycopg2 is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install psycopg2${RESET}"
    exit 1
fi

# Get the installed version of psycopg2
installed_version=$(pip show psycopg2-binary | grep Version | awk '{print $2}')
# Get the latest version of psycopg2 from PyPI
latest_version=$(pip install psycopg2-binary --upgrade | grep "Requirement already satisfied: psycopg2-binary in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}psycopg2 is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}psycopg2 is outdated! Updating...${RESET}"
    pip install --upgrade psycopg2
    echo -e "🚀 ${YELLOW}psycopg2 updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing markdown..."
pip install markdown

test=$(pip show markdown > /dev/null 2>&1)
echo $test

if pip show markdown > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}markdown is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install markdown${RESET}"
    exit 1
fi

# Get the installed version of Markdown
installed_version=$(pip show markdown | grep Version | awk '{print $2}')
# Get the latest version of Markdown from PyPI
latest_version=$(pip install markdown --upgrade | grep "Requirement already satisfied: markdown in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}markdown is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}markdown is outdated! Updating...${RESET}"
    pip install --upgrade markdown
    echo -e "🚀 ${YELLOW}markdown updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing python-dotenv..."
pip install python-dotenv

test=$(pip show python-dotenv > /dev/null 2>&1)
echo $test

if pip show python-dotenv > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}python-dotenv is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install python-dotenv${RESET}"
    exit 1
fi

# Get the installed version of Dotenv
installed_version=$(pip show python-dotenv | grep Version | awk '{print $2}')
# Get the latest version of Dotenv from PyPI
latest_version=$(pip install python-dotenv --upgrade | grep "Requirement already satisfied: python-dotenv in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}python-dotenv is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}python-dotenv is outdated! Updating...${RESET}"
    pip install --upgrade python-dotenv
    echo -e "🚀 ${YELLOW}python-dotenv updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing csvfile..."
pip install csvfile

test=$(pip show csvfile > /dev/null 2>&1)
echo $test

if pip show csvfile > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}csvfile is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install csvfile${RESET}"
    exit 1
fi
# Get the installed version of csvfile
installed_version=$(pip show csvfile | grep Version | awk '{print $2}')
# Get the latest version of csvfile from PyPI
latest_version=$(pip install csvfile --upgrade | grep "Requirement already satisfied: csvfile in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}csvfile is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}csvfile is outdated! Updating...${RESET}"
    pip install --upgrade csvfile
    echo -e "🚀 ${YELLOW}csvfile updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing django-bootstrap-v5..."
pip install django-bootstrap-v5

test=$(pip show django-bootstrap-v5 > /dev/null 2>&1)
echo $test

if pip show django-bootstrap-v5 > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}django-bootstrap-v5 is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install django-bootstrap-v5${RESET}"
    exit 1
fi
# Get the installed version of django-bootstrap-v5
installed_version=$(pip show django-bootstrap-v5 | grep Version | awk '{print $2}')
# Get the latest version of django-bootstrap-v5 from PyPI
latest_version=$(pip install django-bootstrap-v5 --upgrade | grep "Requirement already satisfied: django-bootstrap-v5 in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}django-bootstrap-v5 is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}django-bootstrap-v5 is outdated! Updating...${RESET}"
    pip install --upgrade django-bootstrap-v5
    echo -e "🚀 ${YELLOW}django-bootstrap-v5 updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing pillow..."
pip install pillow

test=$(pip show pillow > /dev/null 2>&1)
echo $test

if pip show pillow > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}pillow is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install pillow${RESET}"
    exit 1
fi
# Get the installed version of pillow
installed_version=$(pip show pillow | grep Version | awk '{print $2}')
# Get the latest version of pillow from PyPI
latest_version=$(pip install pillow --upgrade | grep "Requirement already satisfied: pillow in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}pillow is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}pillow is outdated! Updating...${RESET}"
    pip install --upgrade pillow
    echo -e "🚀 ${YELLOW}pillow updated to $latest_version!${RESET}"
fi
echo "================================================================"

echo "🚀 Installing django-jquery..."
pip install django-jquery

test=$(pip show django-jquery > /dev/null 2>&1)
echo $test

if pip show django-jquery > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}django-jquery is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install django-jquery${RESET}"
    exit 1
fi
# Get the installed version of django-jquery
installed_version=$(pip show django-jquery | grep Version | awk '{print $2}')
# Get the latest version of django-jquery from PyPI
latest_version=$(pip install django-jquery --upgrade | grep "Requirement already satisfied: django-jquery in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}django-jquery is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}django-jquery is outdated! Updating...${RESET}"
    pip install --upgrade django-jquery
    echo -e "🚀 ${YELLOW}django-jquery updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing channels..."
pip install channels

test=$(pip show channels > /dev/null 2>&1)
echo $test

if pip show channels > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}channels is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install channels${RESET}"
    exit 1
fi
# Get the installed version of channels
installed_version=$(pip show channels | grep Version | awk '{print $2}')
# Get the latest version of channels from PyPI
latest_version=$(pip install channels --upgrade | grep "Requirement already satisfied: channels in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}channels is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}channels is outdated! Updating...${RESET}"
    pip install --upgrade channels
    echo -e "🚀 ${YELLOW}channels updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing daphne..."
pip install daphne

test=$(pip show daphne > /dev/null 2>&1)
echo $test

if pip show daphne > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}daphne is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install daphne${RESET}"
    exit 1
fi
# Get the installed version of daphne
installed_version=$(pip show daphne | grep Version | awk '{print $2}')
# Get the latest version of daphne from PyPI
latest_version=$(pip install daphne --upgrade | grep "Requirement already satisfied: daphne in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}daphne is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}daphne is outdated! Updating...${RESET}"
    pip install --upgrade daphne
    echo -e "🚀 ${YELLOW}daphne updated to $latest_version!${RESET}"
fi
echo "================================================================"
echo "🚀 Installing djangorestframework..."
pip install djangorestframework

test=$(pip show djangorestframework > /dev/null 2>&1)
echo $test

if pip show djangorestframework > /dev/null 2>&1; then
    echo -e "✅ ${GREEN}djangorestframework is installed!${RESET}"
else
    echo -e "❌ ${RED}Failed to install djangorestframework${RESET}"
    exit 1
fi
# Get the installed version of djangorestframework
installed_version=$(pip show djangorestframework | grep Version | awk '{print $2}')
# Get the latest version of djangorestframework from PyPI
latest_version=$(pip install djangorestframework --upgrade | grep "Requirement already satisfied: djangorestframework in" | awk '{print $7}' | tr -d '()')

if [ $latest_version = $installed_version ]; then
    echo -e "✅ ${GREEN}djangorestframework is already up to date!${RESET}"
else
    echo -e "🔄 ${YELLOW}djangorestframework is outdated! Updating...${RESET}"
    pip install --upgrade djangorestframework
    echo -e "🚀 ${YELLOW}djangorestframework updated to $latest_version!${RESET}"
fi
echo "================================================================"

echo "📝 Creating a requirements.txt..."
pip freeze > requirements.txt
echo -e "✅ ${GREEN}requirements.txt is created!${RESET}"
echo "================================================================"

echo "🎉 All tasks completed successfully! 🎉"