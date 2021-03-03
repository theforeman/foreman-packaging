module ForemanAzureRm
  class AzureRmCompute
    attr_accessor :sdk
    attr_accessor :azure_vm
    attr_accessor :resource_group
    attr_accessor :nics
    attr_accessor :script_command, :script_uris
    attr_accessor :volumes

    delegate :name, to: :azure_vm, allow_nil: true

    def initialize(azure_vm: ComputeModels::VirtualMachine.new,
                   sdk: sdk,
                   resource_group: azure_vm.resource_group,
                   nics: [],
                   volumes: [],
                   script_command: nil,
                   script_uris: nil)

      @azure_vm = azure_vm
      @sdk = sdk
      @resource_group ||= resource_group
      @nics ||= nics
      @volumes ||= volumes
      @script_command ||= script_command
      @script_uris ||= script_uris
      @azure_vm.hardware_profile ||= ComputeModels::HardwareProfile.new
      @azure_vm.os_profile ||= ComputeModels::OSProfile.new
      @azure_vm.os_profile.linux_configuration ||= ComputeModels::LinuxConfiguration.new
      @azure_vm.os_profile.linux_configuration.ssh ||= ComputeModels::SshConfiguration.new
      @azure_vm.os_profile.linux_configuration.ssh.public_keys ||= [ComputeModels::SshPublicKey.new]
      @azure_vm.storage_profile ||= ComputeModels::StorageProfile.new
      @azure_vm.storage_profile.os_disk ||= ComputeModels::OSDisk.new
      @azure_vm.storage_profile.os_disk.managed_disk ||= ComputeModels::ManagedDiskParameters.new
    end

    def id
      @azure_vm.id
    end

    def persisted?
      !!identity && !!id
    end

    def wait_for(_timeout = 0, _interval = 0, &block)
      instance_eval(&block)
      return true
    end

    def ready?
      vm_status == 'running'
    end

    def reload
    end

    def state
      vm_status
    end

    def start
      sdk.start_vm(@azure_vm.resource_group, name)
      true
    end

    def stop
      sdk.stop_vm(@azure_vm.resource_group, name)
      true
    end

    def to_s
      name
    end

    def vm_status
      sdk.check_vm_status(@azure_vm.resource_group, name)
    end

    def network_interface_card_ids
      return nil unless @azure_vm.network_profile
      nics = @azure_vm.network_profile.network_interfaces
      nics.map(&:id)
    end

    def provisioning_ip_address
      public_ip_address || private_ip_address
    end

    def public_ip_address
      interfaces.each do |nic|
        nic.ip_configurations.each do |configuration|
          next unless configuration.primary
          return nil if configuration.public_ipaddress.blank?
          ip_id     = configuration.public_ipaddress.id
          ip_rg     = ip_id.split('/')[4]
          ip_name   = ip_id.split('/')[-1]
          public_ip = sdk.public_ip(ip_rg, ip_name)
          return public_ip.ip_address
        end
      end
    end

    def private_ip_address
      interfaces.each do |nic|
        nic.ip_configurations.each do |configuration|
          next unless configuration.primary
          if configuration.private_ipaddress.present?
            return private_ip_address = configuration.private_ipaddress
          end
        end
      end
    end

    def interfaces
      nics
    end

    def interfaces_attributes=(attrs)
    end

    def ip_addresses
      []
    end

    def data_disks
      @data_disks ||= @azure_vm.storage_profile.data_disks || []
    end

    def volumes
      return @volumes if data_disks.empty?
      volumes = data_disks.map do |disk|
        OpenStruct.new(:disk => disk, :persisted? => true)
      end
    end

    def volumes_attributes=(attrs)
    end

    def identity
      @azure_vm.name
    end

    def identity=(setuuid)
      @azure_vm.name = setuuid
    end

    def vm_description
        _("%{vm_size} VM Size") % {:vm_size => vm_size}
    end

    # Following properties are for AzureRm
    # These are not part of Foreman's interface

    def vm_size
      @azure_vm.hardware_profile.vm_size
    end

    def platform
      @azure_vm.storage_profile.os_disk.os_type
    end

    def username
      @azure_vm.os_profile.admin_username
    end

    def password
      @azure_vm.os_profile.admin_password
    end

    def ssh_key_data
      # since you can only give one additional
      # sshkey through foreman's UI
      sshkey = @azure_vm.os_profile.linux_configuration.ssh.public_keys[1]
      return unless sshkey.present?
      sshkey.key_data
    end

    def premium_os_disk
      @azure_vm.storage_profile.os_disk.managed_disk.storage_account_type
    end

    def os_disk_caching
      @azure_vm.storage_profile.os_disk.caching
    end

    def image_uuid
      image = @azure_vm.storage_profile.image_reference
      return nil unless image
      if image.id.nil?
        return "marketplace://#{image.publisher}:#{image.offer}:#{image.sku}:#{image.version}"
      else
        image_rg = image.id.split('/')[4]
        image_name = image.id.split('/')[-1]
        if sdk.list_custom_images.find { |custom_img| custom_img.name == image_name }
          return "custom://#{image_name}"
        elsif sdk.fetch_gallery_image_id(image_rg, image_name)
          return "gallery://#{image_name}"
        end
      end
    end

    alias_method :image_id, :image_uuid

    def vm_extension
      return nil unless @azure_vm.resources
      @vm_extension ||= begin
        ext_name = @azure_vm.resources.first.id.split('/')[-1]
        sdk.get_vm_extension(@azure_vm.resource_group, name, ext_name)
      end
    end

    def script_command
      if vm_extension.present?
        return @script_command if vm_extension.settings["commandToExecute"].ends_with?("waagent")
        # Index is based on script_command that is being injected
        # from the code in #create_vm. It can be partly hard-coded
        # since the command shall no change frequently.
        if ssh_key_data.nil?
          user_cmd_index = (vm_extension.settings["commandToExecute"].index("-c"))+ 4
          script_command = vm_extension.settings["commandToExecute"][user_cmd_index..-2]
        else
          vm_extension.settings["commandToExecute"]
        end
      else
        @script_command
      end
    end

    def script_uris
      if vm_extension.present?
        return @script_uris unless vm_extension.settings["fileUris"]
        script_uris = vm_extension.settings["fileUris"]
      else
        @script_uris
      end
    end
  end
end
