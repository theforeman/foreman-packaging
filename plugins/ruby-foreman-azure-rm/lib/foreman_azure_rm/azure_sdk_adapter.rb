module ForemanAzureRm
  class AzureSdkAdapter
    def initialize(tenant, app_ident, secret_key, sub_id)
      @tenant           = tenant
      @app_ident        = app_ident
      @secret_key       = secret_key
      @sub_id           = sub_id
    end

    def resource_client
      @resource_client ||= Resources::Client.new(azure_credentials)
    end

    def compute_client
      @compute_client ||= Compute::Client.new(azure_credentials)
    end

    def network_client
      @network_client ||= Network::Client.new(azure_credentials)
    end

    def storage_client
      @storage_client ||= Storage::Client.new(azure_credentials)
    end

    def subscription_client
      @subscription_client ||= Subscriptions::Client.new(azure_credentials)
    end

    def azure_credentials
      provider = MsRestAzure::ApplicationTokenProvider.new(
      @tenant,
      @app_ident,
      @secret_key)
      
      credentials = MsRest::TokenCredentials.new(provider)

      {
        credentials: credentials,
        subscription_id: @sub_id
      }
    end

    def list_regions(subscription_id)
      subscription_client.subscriptions.list_locations(subscription_id)
    end

    def list_resources(filter)
      resource_client.resources.list(filter)
    end

    def rgs
      rgs      = resource_client.resource_groups.list
      rgs.map(&:name)
    end

    def vnets
      network_client.virtual_networks.list_all
    end

    def subnets(rg_name, vnet_name)
      network_client.subnets.list(rg_name, vnet_name)
    end

    def public_ip(rg_name, pip_name)
      network_client.public_ipaddresses.get(rg_name, pip_name)
    end

    def vm_nic(rg_name,nic_name)
      network_client.network_interfaces.get(rg_name, nic_name)
    end

    def vm_disk(rg_name, disk_name)
      compute_client.disks.get(rg_name, disk_name)
    end

    def get_vm_extension(rg_name, vm_name, vm_extension_name)
      compute_client.virtual_machine_extensions.get(rg_name, vm_name, vm_extension_name)
    end

    def list_vm_sizes(region)
      return [] unless region.present?
      stripped_region = region.gsub(/\s+/, '').downcase
      compute_client.virtual_machine_sizes.list(stripped_region).value()
    end

    def list_vms(region)
      # List all VMs in a resource group
      virtual_machines = compute_client.virtual_machines.list_by_location(region)
    end

    def get_vm(rg_name, vm_name)
      compute_client.virtual_machines.get(rg_name, vm_name)
    end

    def get_marketplace_image(location, publisher_name, offer, skus, version)
      compute_client.virtual_machine_images.get(location, publisher_name, offer, skus, version)
    end

    def list_versions(location, publisher_name, offer, skus)
      compute_client.virtual_machine_images.list(location, publisher_name, offer, skus)
    end

    def list_custom_images
      compute_client.images.list
    end

    def get_custom_image(rg_name, image_name)
      compute_client.images.get(rg_name, image_name)
    end

    def list_galleries
      compute_client.galleries.list
    end

    def list_gallery_images(rg_name, gallery_name)
      compute_client.gallery_images.list_by_gallery(rg_name, gallery_name)
    end

    def get_gallery_image(rg_name, gallery_name, gallery_image_name)
      compute_client.gallery_images.get(rg_name, gallery_name, gallery_image_name)
    end

    def list_gallery_image_versions(rg_name, gallery_name, gallery_image_name)
      compute_client.gallery_image_versions.list_by_gallery_image(rg_name, gallery_name, gallery_image_name)
    end

    def get_storage_accts
      result = storage_client.storage_accounts.list
      result.value
    end

    def create_or_update_vm(rg_name, vm_name, parameters)
      compute_client.virtual_machines.create_or_update(rg_name, vm_name, parameters)
    end

    def create_or_update_vm_extensions(rg_name, vm_name, vm_extension_name, extension_params)
      compute_client.virtual_machine_extensions.create_or_update(rg_name,
                                                          vm_name,
                                                          vm_extension_name,
                                                          extension_params) 
    end

    def create_or_update_pip(rg_name, pip_name, parameters)
      network_client.public_ipaddresses.create_or_update(rg_name, pip_name, parameters)
    end

    def create_or_update_nic(rg_name, nic_name, parameters)
      network_client.network_interfaces.create_or_update(rg_name, nic_name, parameters)
    end

    def delete_pip(rg_name, pip_name)
      network_client.public_ipaddresses.delete(rg_name, pip_name)
    end

    def delete_nic(rg_name, nic_name)
      network_client.network_interfaces.delete(rg_name, nic_name)
    end

    def delete_vm(rg_name, vm_name)
      compute_client.virtual_machines.delete(rg_name, vm_name)
    end

    def delete_disk(rg_name, disk_name)
      compute_client.disks.delete(rg_name, disk_name)
    end

    def check_vm_status(rg_name, vm_name)
      virtual_machine = compute_client.virtual_machines.get(rg_name, vm_name, expand:'instanceView')
      get_status(virtual_machine)
    end

    def get_status(virtual_machine)
      vm_statuses = virtual_machine.instance_view.statuses
      vm_status = nil
      vm_statuses.each do |status|
        if status.code.include? 'PowerState'
          vm_status = status.code.split('/')[1]
        end
      end
      vm_status
    end

    def start_vm(rg_name, vm_name)
      compute_client.virtual_machines.start(rg_name, vm_name)
    end

    def stop_vm(rg_name, vm_name)
      compute_client.virtual_machines.power_off(rg_name, vm_name)
      compute_client.virtual_machines.deallocate(rg_name, vm_name)
    end

    def self.gallery_caching(rg_name)
      @gallery_caching ||= {}
      @gallery_caching[rg_name] ||= {}
    end

    def actual_gallery_image_id(rg_name, image_id)
      gallery_names = list_galleries.map(&:name)
      gallery_names.each do |gallery|
        gallery_image = list_gallery_images(rg_name, gallery).detect { |image| image.name == image_id }
        return gallery_image&.id
      end
      nil
    end

    def fetch_gallery_image_id(rg_name, image_id)
      AzureSdkAdapter.gallery_caching(rg_name)[image_id] ||= actual_gallery_image_id(rg_name, image_id)
    end
  end
end
