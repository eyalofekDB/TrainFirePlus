import os


# change labels
label_dirs = ['/DATA/TRAIN/TrainFirePlus/datasets/BarrelFire/train/labels',
              '/DATA/TRAIN/TrainFirePlus/datasets/BarrelFire/val/labels']


original_tag = '3'
new_tag = '0'
for directory in label_dirs:
    print(f'process directory {directory}')
    files = os.listdir(directory)
    for filename in files:
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            with open(f, "r") as fid:
                d = fid.readlines()
                newlines = []
                for line in d:
                    newlines.append(line.replace(original_tag, new_tag, 1))

            with open(f, 'w') as f:
                for line in newlines:
                    f.write(line)


# delete labels
# labels_to_save = ['0', '1', '10', '11']
#
# label_dirs = ['datasets/VisDrone/VisDrone2019-DET-train/labels',
#               'datasets/VisDrone/VisDrone2019-DET-val/labels']
# image_dirs = ['datasets/VisDrone/VisDrone2019-DET-train/images',
#               'datasets/VisDrone/VisDrone2019-DET-val/images']
#
# for i, directory in enumerate(label_dirs):
#     for filename in os.listdir(directory):
#         f = os.path.join(directory, filename)
#         # checking if it is a file
#         if os.path.isfile(f):
#             with open(f, "r") as fid:
#                 d = fid.readlines()
#                 newlines = []
#                 for line in d:
#                     if line.split()[0] in labels_to_save:
#                         newlines.append(line)
#
#             if line:
#                 with open(f, 'w') as f:
#                     for line in newlines:
#                         f.write(line)
#             else:
#                 os.remove(f)
#                 os.remove(os.path.join(image_dirs[i], os.path.split(f)[1][:-4]+'.jpg'))







