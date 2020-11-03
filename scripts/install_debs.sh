#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path"

bash ./build_debs.sh

dpkg -i ../dist/*.deb