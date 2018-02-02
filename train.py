# Launch training
from lucanode import loader
from lucanode import dataset
from lucanode.training import detection

LUNA_DATASET_PATH = "/home/ofont/DATASETS/LUNA/"
LUNA_CT_SCAN_GLOB = LUNA_DATASET_PATH + "subset*/*.mhd"
LUNA_LUNG_MASK_GLOB = LUNA_DATASET_PATH + "seg-lungs-LUNA16/*.mhd"
LUNA_NODULE_MASK_GLOB = LUNA_DATASET_PATH + "seg-nodules-LUNA16/*.nii.gz"

# Test training
detection.train(
    None,
    "unet.h5",
    (512, 512),
    (LUNA_CT_SCAN_GLOB, dataset.id_ct_scan_luna),
    (LUNA_LUNG_MASK_GLOB, dataset.id_lung_mask_luna),
    (LUNA_NODULE_MASK_GLOB, dataset.id_nodule_mask_luna),
)
