require 'carrierwave/chunker'

class ChunkUploader < CarrierWave::Uploader::Base
  include CarrierWave::Chunker

  def store_dir
    "uploads/#{model.class.to_s.underscore}/#{mounted_as}/#{model.id}"
  end
end