from bg_atlasapi import show_atlases
from bg_atlasapi.bg_atlas import BrainGlobeAtlas

show_atlases()


def get_atlas(atlas_name="allen_mouse_25um"):
    """Get the atlas with atlas name

    Args:
        atlas_name (str, optional): atlas name. Defaults to "allen_mouse_25um".

    Return: 
        atlas with atlas.referee for reference image
                   atlas.annotation image 
                   atlas.shape = (528, 320, 456)
                   atlas.hemispheres (value 1 in left hemisphere
                   2, in right
                   )
    """
    atlas = BrainGlobeAtlas(atlas_name)
    return atlas
