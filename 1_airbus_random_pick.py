import os, shutil, random
from tqdm import tqdm

dataset_train = './train_v2'
dataset_test = './test_v2'

DATA_DIR = dataset_train
DATA_PICK_NUMS = 10
DATA_PICK_DIR = dataset_test + '_pick'

def _os_chk(src, dst):
  if not os.path.isfile(src):
      print("file {} not exist!".format(src))
  else:
      fpath, fname = os.path.split(dst)
      if not os.path.exists(fpath):
          os.makedirs(fpath)

def os_mv(src, dst):
  _os_chk(src, dst)
  shutil.move(src, dst)

def os_cp(src, dst):
  _os_chk(src, dst)
  shutil.copyfile(src, dst)

def pick_img(num):
  total_choice = os.listdir(DATA_DIR)
  random_pick = random.sample(total_choice, num)
  return random_pick

def copy_img(pick_item):
  if len(os.listdir(DATA_PICK_DIR)):
    print("Delete previous images first...")
    for im in tqdm(os.listdir(DATA_PICK_DIR)):
      os.remove(os.path.join(DATA_PICK_DIR, im))

  for im in tqdm(pick_item):
    f_src = os.path.join(DATA_DIR, im)
    f_dst = os.path.join(DATA_PICK_DIR, im)
    os_cp(f_src, f_dst)

if __name__ == "__main__":
  copy_img(pick_img(DATA_PICK_NUMS))