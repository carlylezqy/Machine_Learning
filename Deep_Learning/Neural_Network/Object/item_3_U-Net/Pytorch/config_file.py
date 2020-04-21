# [data_paths]
path_local = "/Volumes/TimeMachine/Github/_Exclude_Items_/DRIVE_datasets_training_testing/"
train_imgs_original = "DRIVE_dataset_imgs_train.hdf5"
train_groundTruth = "DRIVE_dataset_groundTruth_train.hdf5"
train_border_masks = "DRIVE_dataset_borderMasks_train.hdf5"
test_imgs_original = "DRIVE_dataset_imgs_test.hdf5"
test_groundTruth = "DRIVE_dataset_groundTruth_test.hdf5"
test_border_masks = "DRIVE_dataset_borderMasks_test.hdf5"


# [experiment_name]
name = "test"


# [data_attributes]
# Dimensions of the patches extracted from the full images
patch_height = 48
patch_width = 48


# [training_settings]
# number of total patches:
N_subimgs = 190000
# if patches are extracted only inside the field of view:
inside_FOV = False
# Number of training epochs
N_epochs = 150
batch_size = 32
#if running with nohup
nohup = True


# [testing_settings]
# Choose the model to test: best==epoch with min loss, last==last epoch
best_last = "best"
#number of full images for the test (max 20)
full_images_to_test = 20
#How many original-groundTruth-prediction images are visualized in each image
N_group_visual = 1
#Compute average in the prediction, improve results but require more patches to be predicted
average_mode = True
#Only if average_mode==True. Stride for patch extraction, lower value require more patches to be predicted
stride_height = 5
stride_width = 5
#if running with nohup
nohup = False