class FixCaseAzureRm < ActiveRecord::Migration[5.2]
  def change
    ComputeResource.where(type: 'ForemanAzureRM::AzureRM').update_all(type: 'ForemanAzureRm::AzureRm')
  end
end
