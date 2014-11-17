Vagrant.configure("2") do |config|
  ## Choose your base box
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.synced_folder ".", "/home/vagrant/fotochest"

  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 6379, host: 6379
  config.ssh.forward_agent = true

  config.vm.host_name = 'fotochest-dev'

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "developer.yml"
    ansible.host_key_checking = false
    #ansible.verbose = 'v'

    ansible.groups = {
          "developer" => ["default"],
        }
  end
end
