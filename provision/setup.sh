#!/bin/bash

echo "Provisioning additional packages..."
sudo apt-get update -y

echo "Installing additional requirements"
sudo apt-get install curl build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties python python-pip libffi-dev libmysqlclient-dev lxc debootstrap bridge-utils -y

echo "Installing Flask 0.9"
pip install flask==0.9
