module ForemanAzureRm
  module Concerns
    module HostsControllerExtensions
      extend ActiveSupport::Concern

      def sizes
        azure_rm_resource = ComputeResource.unscoped.find_by_id(params[:compute_resource_id])
        if azure_rm_resource.present?
          render :json => azure_rm_resource.vm_sizes.map { |size| size.name }
        else
          no_sizes = _('The region you selected has no sizes associated with it')
          render :json => "[\"#{no_sizes}\"]"
        end
      end

      def subnets
        azure_rm_resource = ComputeResource.unscoped.find_by_id(params[:compute_resource_id])
        if azure_rm_resource.present?
          subnets = azure_rm_resource.subnets
          if subnets.present?
            render :json => subnets
          else
            no_subnets = _('The selected region has no subnets')
            render :json => "[\"#{no_subnets}\"]"
          end
        else
          no_compute = _('The selected image has no associated compute resource')
          render :json => "[\"#{no_compute}\"]"
        end
      end
    end
  end
end
