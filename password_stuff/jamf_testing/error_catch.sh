#!/bin/bash
tempssid="hiia"
current_ssid_template_error="Network $tempssid was not found in the preferred networks list"
echo $current_ssid_template_error
printf 'Deleting %s from saved SSIDs... ' $tempssid;
# echo Deleting $SSID
ACDSPW_RM=$(networksetup -removepreferredwirelessnetwork "en0" $tempssid)
if [ "$current_ssid_template_error" == "$ACDSPW_RM" ]; then
    echo "Error!!!"
else
    echo "Success!!!"
fi

# delete it here
printf Done.\\n
printf 'Deleting %s password from keychain... ' $tempssid;
# delete it here
printf Done.\\n