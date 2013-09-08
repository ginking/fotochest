Vagrant::Config.run do |config|
  config.vm.box = "django"
  # Build the Django box by visiting https://github.com/dstegelman/vagrant-django-chef
  config.vm.box_url = "http://whereeveryourcustombuiltboxlivesontheinternets/box.box"
  config.vm.host_name = 'fotochest'
  config.vm.share_folder "fotochest", "/home/vagrant/fotochest", "../fotochest"
end