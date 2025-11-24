class Upload < ApplicationRecord
  mount_uploader :file, ChunkUploader
end