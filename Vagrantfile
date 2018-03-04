# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-14.04"
  config.vm.define "oasisbot"

  config.vm.network "public_network"

  config.vm.synced_folder "./", "/oasisbot"

  config.vm.provider "virtualbox" do |vb|
     vb.gui = false
     vb.memory = "1024"
   end
  
  config.vm.provision "shell", inline: <<-SHELL
     apt-get update
     apt-get install -y python3
     apt-get install -y python3-pip
     pip3 install discord.py
     pip3 install asyncio
     pip3 install shodan
     cd /oasisbot/
     python3 ./bot_main.py &
     SHELL
end
