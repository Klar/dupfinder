#!/usr/bin/python
# deletes or moves duplicate files (via hash) in given $directory

import hashlib
import os

#set directory to check for duplicates
directory = '/home/user/Desktop/folder'
movedir= directory + '/duplicates/'

foldersave = 2 

#get root and filename from given directory
def get_filepath(dir):
  files = []
  print "get_filepath(" + dir + ")" 
  for root, dirs, filenames in os.walk(dir):
      for filename in filenames:
          files.append([root,filename])
  return files

def move():
      rootSplit = root.split("/")
      myList = ""
      for count in range(foldersave + 1):
        if count == 0:
          continue
        myList = rootSplit[-count] + "/" + myList

      movingdir = movedir + myList

      # create new duplicate directory
      try:
        os.makedirs(movingdir)
      except:
        print()

      os.rename(root + "/" + filename, movingdir + filename)
      print "duplicate move to: " + movingdir

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
      move()

    else:
      hashes.append(hash)
  return hashfiles

files = get_filepath(directory)
get_hash_do_action(files)
