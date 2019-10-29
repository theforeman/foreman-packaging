# coding: utf-8
require 'rbnacl/libsodium/version'

Gem::Specification.new do |spec|
  spec.name          = "rbnacl-libsodium"
  spec.version       = RbNaCl::Libsodium::VERSION
  spec.date          = Time.now.strftime('%Y-%m-%d')
  spec.summary       = %q{rbnacl with libsodium}

  spec.add_runtime_dependency "rbnacl", ">= 3.0.1"

  spec.add_development_dependency "bundler", "~> 1.5"
  spec.add_development_dependency "rake", ">= 10"
end
