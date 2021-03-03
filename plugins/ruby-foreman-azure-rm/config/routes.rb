Rails.application.routes.draw do
  scope :azure_rm, :path => '/azure_rm' do
    get :sizes, :controller => :hosts
    get :subnets, :controller => :hosts
    get :storage_accts, :controller => :hosts
    get :vnets, :controller => :hosts
  end
  namespace :api, :defaults => { :format => 'json' } do
    scope "(:apiv)", :module => :v2, :defaults => { :apiv => 'v2' }, :apiv => /v1|v2/, :constraints => ApiConstraints.new(:version => 2, :default => true) do
      resources :compute_resources, :except => [:new, :edit] do
        get :available_resource_groups, :on => :member
        get :available_subnets, :on => :member
        get :available_vnets, :on => :member
        get '(:region_id)/available_sizes', :to => 'compute_resources#available_sizes', :on => :member
      end
    end
  end
end