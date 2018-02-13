
# Extracted from be56c439856b6fea21aaabc6144e5ab9ad77ec76 for Rails 4.2.8 compatibility
module ActiveSupport
  class MessageEncryptor
    DEFAULT_CIPHER = "aes-256-cbc"

    # Given a cipher, returns the key length of the cipher to help generate the key of desired size
    def self.key_len(cipher = DEFAULT_CIPHER)
      OpenSSL::Cipher.new(cipher).key_len
    end
  end
end
