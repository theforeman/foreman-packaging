class FixImageUuidPrefix < ActiveRecord::Migration[5.2]
  def up
    Image.where(compute_resource: ForemanAzureRm::AzureRm.unscoped.all).update_all("uuid = concat('marketplace://', uuid)")
  end

  def down
  end
end
