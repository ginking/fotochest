Vagrant.configure("2") do |config|
  ## Choose your base box
  config.vm.box = "trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.synced_folder ".", "/home/vagrant/fotochest"

  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 9000, host: 9090
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
