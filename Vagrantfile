# -*- mode: ruby -*-
# vi: set ft=ruby :

# Global vars
api_version = "2"
box_distribution = "bionic"
vm_name = "jud-in-foco"
sync_dir = "/tmp/" + vm_name + "/"
ansible_dir = "/tmp/" + vm_name + "/ansible/"
is_proxy = false
proxy_dtp = "http://prxdf.prevnet:3128/"


Vagrant.configure(api_version) do |config|
  
  config.vm.box = "ubuntu/bionic64" # server v18.04
  config.vm.define vm_name
  config.vm.hostname = vm_name
  config.vm.box_check_update = false

  # Avaliacao da existencia do proxy
  if (Vagrant.has_plugin?("vagrant-proxyconf")) && is_proxy
    config.proxy.http   = proxy_dtp
    config.proxy.https  = proxy_dtp
  end

  # Mapeamento das portas guest e host
  # Para flask
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  # Mapeamento de sincronismo host e guest  
  config.vm.synced_folder ".", sync_dir
  
  # configuracoes gerais da maquina
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
    vb.name = vm_name
  end
 
  # configuracao para o provisionamento do conteudo da maquina via ansible
  config.vm.provision "ansible_local" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.playbook = "playbook.yml"
    ansible.provisioning_path = ansible_dir
    ansible.extra_vars = {
      ansible_distribution_release: box_distribution,
      app_name: vm_name,
      is_proxy: is_proxy,
      proxy_dtp: proxy_dtp
    }

  end
end