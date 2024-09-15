#!/bin/bash

# Get all the Wifi SSIDs saved to the computer
SSIDS=$(networksetup -listpreferredwirelessnetworks "en0" | sed '1d')
# Get the network that the computer is currently connected to
CURRENTSSID=$(networksetup -getairportnetwork "en0" | sed 's/^Current Wi-Fi Network: //')

# loop through all preferred networks (varname = SSID)
while read -r SSID; do
    # If the current SSID is ACDSParentWiFi
  if [ "$SSID" == "ACDSParentWiFi" ]; then
    # Make a template error message to compare with the actual output error message (since success and errors both have exit code 0)
    current_ssid_template_error="Network $SSID was not found in the preferred networks list"
    # echo $current_ssid_template_error

    printf 'Deleting %s from saved SSIDs... ' $SSID;
    # Remove the SSID from the preferred networks list
    ACDSPW_RM=$(networksetup -removepreferredwirelessnetwork "en0" $SSID)
    printf $ACDSPW_RM
    # If the template error message matches the actual output error message, then there was an error.
    if [ "$current_ssid_template_error" == "$ACDSPW_RM" ]; then
      printf 'Error: %s, moving on.\\n' $ACDSPW_RM
    else
        printf Done.\\n
    fi

    # Remove the password from the keychain
    printf 'Deleting %s password from keychain... ' $SSID;

    UUID=$(system_profiler SPHardwareDataType | grep 'Hardware UUID' | awk '{print $3}')
    localkeychain="/Users/$(whoami)/Library/Keychains/$UUID"
    rm -rf $localkeychain
    

    keychain_delete="$(security delete-generic-password -l $SSID '/Library/Keychains/System.keychain')"
    
    # COMMENTED BECAUSE THE KEYCHAIN COMMAND DUMPS ALL THE KEYCHAIN DATA AND CAUSES IT TO BUG OUT. THIS ISN'T NEEDED ANYWAY, JUST A NICE ERROR HANDLER.

    # Check if the keychain item was deleted by checking if the exit co
    #if [[ $keychain_delete == *"password has been deleted."* ]]; then
      printf Done.\\n
    #else
    #  printf 'Error: %s, moving on.\\n' $keychain_delete
    #fi

    # If the current SSID is apple
  elif [ "$SSID" == "apple" ]; then
    # Make a template error message to compare with the actual output error message (since success and errors both have exit code 0)
    current_ssid_template_error="Network $SSID was not found in the preferred networks list"
    # echo $current_ssid_template_error
    printf 'Deleting %s from saved SSIDs... ' $SSID;

    # Remove the SSID from the preferred networks list
    APPLE_RM=$(networksetup -removepreferredwirelessnetwork "en0" $SSID)
    # If the template error message matches the actual output error message, then there was an error.
    if [ "$current_ssid_template_error" == "$APPLE_RM" ]; then
      printf 'Error: %s, moving on.\\n' $APPLE_RM
    else
        printf Done.\\n
    fi
  #else
    # echo Deleting $SSID
    # networksetup -removepreferredwirelessnetwork "en0" "$SSID"
  fi
done <<< "$SSIDS"

if [ "$CURRENTSSID" == "ACDSParentWiFi" ]; then
# Reconnect to ensure that the computer is disconnected, should reconnect to AlmadenCountryDaySchool instead.
  echo "Disconnecting from $CURRENTSSID"
  networksetup -setairportpower en0 off
  networksetup -setairportpower en0 on
  echo All Done!
fi




# Remove ACDSParentWifi credentials:
# sudo security delete-generic-password -l ACDSParentWiFi "/Library/Keychains/System.keychain"