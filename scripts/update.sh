#!/usr/bin/env bash
# Temporarily disable history expansion
set +H

# ANSI escape codes for colored output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
# Reset to default color
NC='\033[0m'

colored_output() {
  local color_code="$1"
  local message="$2"
  local no_newline_flag="$3"
  local colored_message="${color_code}${message}${NC}"
  if [ "$no_newline_flag" == "-n" ]; then
    echo -ne "$colored_message"
  else
    echo -e "$colored_message"
  fi
}

abort_update() {
  local message="$1"
  colored_output ${RED} "Aborting update. ${message}"
  # Re-enable history expansion
  set -H
  exit 1
}

# Check for superuser privileges
if [[ $EUID -ne 0 ]]; then
  colored_output ${RED} "This script must be run as root. Attempting to elevate privileges..."
  # Re-run the script as root
  exec sudo bash "$0" "$@"
fi

colored_output ${GREEN} "Fetching updates from GitHub..."

remote_name="origin"
current_branch=$(git symbolic-ref --short HEAD  || abort_update "Failed retrieving currently checked out branch.")
# Fetch the latest changes from the remote
git fetch $remote_name

# Compare the local branch with the remote branch
if [ $(git rev-parse HEAD) != $(git rev-parse $remote_name/$current_branch) ]; then
  colored_output ${GREEN} "Changes are available to pull."
else
  colored_output ${GREEN} "No changes to pull."
  exit 0
fi

git stash || abort_update "Failed stashing local changes."
git pull $remote_name || abort_update "Failed pulling changes."
git stash pop --index || abort_update "Failed applying local changes from stash."

colored_output ${GREEN} "Updating submodules..."

git submodule update --init --recursive || abort_update "Failed updating submodules."
venv/bin/pip3.11 install submodules/* || abort_update "Failed installing submodules."

colored_output ${GREEN} "Restarting service..."

{ systemctl daemon-reload && systemctl restart bluetooth_2_usb.service ; } || abort_update "Failed restarting service."

colored_output ${GREEN} "Update successful. Now running $(venv/bin/python3.11 bluetooth_2_usb.py -v)"

# Re-enable history expansion
set -H
