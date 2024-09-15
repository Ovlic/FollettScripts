#!/bin/bash
# string='My long string'
# if [[ $string == *"hi"* ]]; then
#   echo "It's there!"
# fi

# networksetup -setairportpower en0 off # turn off device en0
# networksetup -setairportpower en0 on  # turn on device en0

UUID=$(system_profiler SPHardwareDataType | grep 'Hardware UUID' | awk '{print $3}')
localkeychain="/Users/$(id -un)/Library/Keychains/$UUID"
echo $localkeychain