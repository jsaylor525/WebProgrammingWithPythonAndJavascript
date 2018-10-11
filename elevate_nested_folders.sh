#!/bin/bash

folders=$(find . -maxdepth 2 -type d)

for folder in $folders; do
    parent_folder=$(echo "$folder" | awk -F"/" '{print $2}')
    child_folder=$(echo "$folder" | awk -F"/" '{print $3}')
    if [[ ! -z $parent_folder ]]; then
        if [[ $parent_folder == $child_folder ]]; then
            echo "Found match $parent_folder and $child_folder"
            mv "$parent_folder/$child_folder/"* "$parent_folder/."
            rm -rf "./$parent_folder/$child_folder/"
        fi
    fi
done