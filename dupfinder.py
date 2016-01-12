#!/usr/bin/python
# deletes or moves duplicate files (via hash) in given $directory

import hashlib
import os

#set directory to check for duplicates
directory = '/run/media/extHD/media/music/'
movedir = '/run/media/extHD/media/music/dups/'


#get root and filename from given directory
def get_filepath(dir):
  files = []
  print "get_filepath(" + dir + ")" 
  for root, dirs, filenames in os.walk(dir):
      for filename in filenames:
          files.append([root,filename])
  return files


#get root, filename and hash from given directory
def get_hash_do_action(files):
  hashfiles = []
  hashes = []
  print "get_hash()" 
  for root,filename in files:
    image_file = open(root + "/" + filename).read()
    hash = hashlib.md5(image_file).hexdigest()
    hashfiles.append([root,filename,hash])
    if hash in hashes:
      #os.remove(root + "/" + filename)
      os.rename(root + "/" + filename,movedir + filename)
      print "moved: " + root + "/" + filename
    else:
      hashes.append(hash)
  del files
  return hashfiles

files = get_filepath(directory)
get_hash_do_action(files)