# This concern has the methods to be called inside azure_rm.rb
module ForemanAzureRm
  module VMExtensions
    module ManagedVM
      extend ActiveSupport::Concern

      def define_managed_storage_profile(vm_name, os_disk_caching, platform, premium_os_disk)
        storage_profile = ComputeModels::StorageProfile.new
        os_disk = ComputeModels::OSDisk.new
        managed_disk_params = ComputeModels::ManagedDiskParameters.new

        # Create OS disk
        os_disk.name = "#{vm_name}-osdisk"
        os_disk.os_type = platform
        os_disk.create_option = ComputeModels::DiskCreateOptionTypes::FromImage
        os_disk.caching = disk_caching(os_disk_caching)
        managed_disk_params.storage_account_type = if premium_os_disk == 'true'
                                                     ComputeModels::StorageAccountTypes::PremiumLRS
                                                   else
                                                     ComputeModels::StorageAccountTypes::StandardLRS
                                                   end
        os_disk.managed_disk = managed_disk_params
        storage_profile.os_disk = os_disk
        storage_profile
      end

      def disk_caching(disk_type_caching)
        case disk_type_caching
        when 'None'
          ComputeModels::CachingTypes::None
        when 'ReadOnly'
          ComputeModels::CachingTypes::ReadOnly
        when 'ReadWrite'
          ComputeModels::CachingTypes::ReadWrite
        when nil, ""
          nil
        else
          raise RuntimeError, "Disk caching value must be either 'None', 'ReadOnly' or 'ReadWrite'."
        end
      end

      def define_data_disks(vm_name, data_disks)
        unless data_disks.nil?
          disks = []
          disk_count = 0
          data_disks.each do |disk_num, attrs|
            managed_data_disk = ComputeModels::ManagedDiskParameters.new
            disk = ComputeModels::DataDisk.new
            disk.name = "#{vm_name}-data-disk#{disk_count}"
            disk.caching  = disk_caching(attrs[:data_disk_caching])
            disk.disk_size_gb = attrs[:disk_size_gb]
            disk.create_option = ComputeModels::DiskCreateOption::Empty
            disk.lun = disk_count + 1
            disk.managed_disk = managed_data_disk
            disk_count += 1
            disks << disk
          end
          disks
        end
      end

      def marketplace_image_plan(image)
        image_type, image_id = image.split('://')
        return nil unless image_type == 'marketplace' && image_id.include?('byos')
        urn = image_id.split(':')
        publisher = urn[0]
        offer     = urn[1]
        sku       = urn[2]
        version   = urn[3]
        image_plan = ComputeModels::PurchasePlan.new
        image_plan.publisher = publisher.downcase
        image_plan.name = sku.downcase
        image_plan.product = offer.downcase
        image_plan
      end

      def marketplace_image_reference(publisher, offer, sku, version)
        image_reference = ComputeModels::ImageReference.new
        image_reference.publisher = publisher
        image_reference.offer = offer
        image_reference.sku = sku
        image_reference.version = version
        image_reference
      end

      def define_image(rg_name, image)
        image_type, image_id = image.split('://')
        case image_type
        when 'marketplace'
          urn = image_id.split(':')
          publisher = urn[0]
          offer     = urn[1]
          sku       = urn[2]
          version   = urn[3]
          image_reference = marketplace_image_reference(publisher, offer, sku, version)
        when 'custom'
          custom_image = sdk.get_custom_image(rg_name, image_id)
          image_reference = ComputeModels::ImageReference.new
          image_reference.id = custom_image.id
        when 'gallery'
          image_reference = ComputeModels::ImageReference.new
          image_reference.id = sdk.fetch_gallery_image_id(rg_name, image_id)
        else
          image_reference = nil
        end
        image_reference
      end

      def define_network_profile(network_interface_card_ids)
        network_interface_cards = []
        network_interface_card_ids.each_with_index do |id, index|
          nic = ComputeModels::NetworkInterfaceReference.new
          nic.id = id
          nic.primary = true
          network_interface_cards << nic
        end
        network_profile = ComputeModels::NetworkProfile.new
        network_profile.network_interfaces = network_interface_cards
        network_profile
      end

      def create_nics(region, args = {})
        nics               = []
        args[:interfaces_attributes].each do |nic, attrs|
          private_ip = (attrs[:private_ip] == 'false') ? false : true
          priv_ip_alloc       = if private_ip
                                  NetworkModels::IPAllocationMethod::Static
                                else
                                  NetworkModels::IPAllocationMethod::Dynamic
                                end
          pub_ip_alloc        = case attrs[:public_ip]
                                when 'Static'
                                  NetworkModels::IPAllocationMethod::Static
                                when 'Dynamic'
                                  NetworkModels::IPAllocationMethod::Dynamic
                                when 'None'
                                  nil
                                else
                                    raise RuntimeError, "Public IP value must be either 'Dynamic', 'Static' or 'None'"
                                end
          if pub_ip_alloc.present?
            public_ip_params = NetworkModels::PublicIPAddress.new.tap do |ip|
              ip.location = region
              ip.public_ipallocation_method = pub_ip_alloc
            end

            pip = sdk.create_or_update_pip(args[:resource_group],
                                           "#{args[:vm_name]}-pip#{nic}",
                                           public_ip_params)
          end
          new_nic = sdk.create_or_update_nic(
            args[:resource_group],
            "#{args[:vm_name]}-nic#{nic}",
            NetworkModels::NetworkInterface.new.tap do |interface|
              interface.location = region
              interface.ip_configurations = [
                NetworkModels::NetworkInterfaceIPConfiguration.new.tap do |nic_conf|
                  nic_conf.name = "#{args[:vm_name]}-nic#{nic}"
                  nic_conf.private_ipallocation_method = priv_ip_alloc
                  nic_conf.private_ipaddress = attrs[:ip] if priv_ip_alloc == "Static"
                  nic_conf.subnet = subnets.select{ |subnet| subnet.id == attrs[:network] }.first
                  nic_conf.public_ipaddress = pip
                end
              ]
            end
          )
          nics << new_nic
        end
        nics
      end

      def initialize_vm(vm_hash)
        custom_data = vm_hash[:custom_data]
        msg = "Creating Virtual Machine #{vm_hash[:name]} in Resource Group #{vm_hash[:resource_group]}."
        logger.debug msg
        vm_create_params = ComputeModels::VirtualMachine.new.tap do |vm|
          vm.location = vm_hash[:location]
          unless vm_hash[:availability_set_id].nil?
            sub_resource = MsRestAzure::SubResource.new
            sub_resource.id = vm_hash[:availability_set_id]
            vm.availability_set = sub_resource
          end

          vm.os_profile = ComputeModels::OSProfile.new.tap do |os_profile|
            os_profile.computer_name  = vm_hash[:name]
            os_profile.admin_username = vm_hash[:username]
            os_profile.admin_password = vm_hash[:password]

            # Adding the ssh-key support for authentication
            os_profile.linux_configuration = ComputeModels::LinuxConfiguration.new.tap do |linux|
              linux.disable_password_authentication = vm_hash[:disable_password_authentication]
              linux.ssh = ComputeModels::SshConfiguration.new.tap do |ssh_config|
                ssh_config.public_keys = [
                  ComputeModels::SshPublicKey.new.tap do |foreman_key|
                    foreman_key.key_data = key_pair.public
                    foreman_key.path = "/home/#{vm_hash[:username]}/.ssh/authorized_keys"
                  end
                ]
                if vm_hash[:ssh_key_data].present?
                  key_data = vm_hash[:ssh_key_data]
                  pub_key = ComputeModels::SshPublicKey.new
                  pub_key.key_data = key_data
                  pub_key.path = "/home/#{vm_hash[:username]}/.ssh/authorized_keys"
                  ssh_config.public_keys << pub_key
                end
              end
            end
            # added custom_data here so that azure's vm gets this
            os_profile.custom_data    = Base64.strict_encode64(custom_data) unless vm_hash[:custom_data].nil?
          end
          vm.storage_profile = define_managed_storage_profile(
                                                                vm_hash[:name],
                                                                vm_hash[:os_disk_caching],
                                                                vm_hash[:platform],
                                                                vm_hash[:premium_os_disk]
                                                              )
          vm.hardware_profile = ComputeModels::HardwareProfile.new.tap do |hw_profile|
            hw_profile.vm_size = vm_hash[:vm_size]
          end
        end

        vm_create_params
      end

      def create_managed_virtual_machine(vm_hash)
        vm_params = initialize_vm(vm_hash)
        vm_params.plan = marketplace_image_plan(vm_hash[:image_id])
        vm_params.network_profile = define_network_profile(vm_hash[:network_interface_card_ids])
        vm_params.storage_profile.image_reference = define_image(vm_hash[:resource_group], vm_hash[:image_id])
        vm_params.storage_profile.data_disks = define_data_disks(vm_hash[:name], vm_hash[:data_disks])
        sdk.create_or_update_vm(vm_hash[:resource_group], vm_hash[:name], vm_params)
      end

      def create_vm_extension(region, args = {})
        if args[:script_command].present? || args[:script_uris].present?
          args[:script_uris] ||=  args[:script_uris].to_s
          extension = ComputeModels::VirtualMachineExtension.new
          if args[:platform] == 'Linux'
            extension.publisher = 'Microsoft.Azure.Extensions'
            extension.virtual_machine_extension_type = 'CustomScript'
            extension.type_handler_version = '2.0'
          end
          extension.auto_upgrade_minor_version = true
          extension.location = region
          extension.settings = {
                'commandToExecute' => args[:script_command],
                'fileUris'         => args[:script_uris].split(',')
          }
          sdk.create_or_update_vm_extensions(args[:resource_group],
                                             args[:vm_name],
                                             'ForemanCustomScript',
                                             extension)
        end
      end
    end
  end
end
