# Copyright (c) OpenMMLab. All rights reserved.

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class CracksDataset(CustomDataset):
    """Cracks dataset.

    In segmentation map annotation , 0 stands for background,
    which is included in 7 categories. ``reduce_zero_label`` is fixed to
    False. The ``img_suffix`` is fixed to '.jpg' and ``seg_map_suffix`` is
    fixed to '.png'.

    """

    CLASSES = ('Background', 'Arrachement_pelade', 'Faiencage', 'Nid_de_poule',
                 'Transversale', 'Longitudinale', 'Reparation')

    PALETTE = [[120, 120, 120], [220, 10, 50], [6, 230, 230], [20, 10, 10],
               [220, 130, 30], [240, 240, 70], [60, 220, 30]]

    def __init__(self, **kwargs):
        super(CracksDataset, self).__init__(
            img_suffix='.jpg',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)
        
