#!/usr/bin/env bash

# Define variables for use
ZMQ_GIT_PROJECT=$1  # Path to libzmq git project
ZMQ_OUT_FILE=$2     # Path to output file

# Save all contributors to a file
cd ${ZMQ_GIT_PROJECT}
git shortlog -sne > ${ZMQ_OUT_FILE}

# Add GitHub checkbox prefix
sed -i -e 's/^/- [ ]/' ${ZMQ_OUT_FILE}

echo "Finished!"
