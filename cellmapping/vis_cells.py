import random
import numpy as np

from brainrender import Scene
from brainrender.actors import Points

from rich import print
from myterial import orange
from pathlib import Path

print(f"[{orange}]Running example: {Path(__file__).name}")


def get_n_random_points_in_region(region, N):
    """
    Gets N random points inside (or on the surface) of a mes
    """

    region_bounds = region.mesh.bounds()
    X = np.random.randint(region_bounds[0], region_bounds[1], size=10000)
    Y = np.random.randint(region_bounds[2], region_bounds[3], size=10000)
    Z = np.random.randint(region_bounds[4], region_bounds[5], size=10000)
    pts = [[x, y, z] for x, y, z in zip(X, Y, Z)]

    ipts = region.mesh.insidePoints(pts).points()
    return np.vstack(random.choices(ipts, k=N))


scene = Scene(title="Labelled cells")

# Get a numpy array with (fake) coordinates of some labelled cells
mob = scene.add_brain_region("MOB", alpha=0.15)
#olf = scene.add_brain_region("OLF", alpha=0.16)
pir = scene.add_brain_region("PIR", alpha=0.16)
th = scene.add_brain_region("TH", alpha=0.16)
scene.add_label(mob,"Main Olfactory bulb")
scene.add_label(th, "Thalamus")
scene.add_label(pir,'Piriform')
#scene.add_label(olf,'Olfactory')
coordinates = get_n_random_points_in_region(mob, 2000)
#olf_coords = get_n_random_points_in_region(olf,1000)
pir_coords = get_n_random_points_in_region(pir,1000)
th_coords = get_n_random_points_in_region(th,1000)
# Add to scene
scene.add(Points(coordinates, name="CELLS", colors="steelblue"))
#scene.add(Points(olf_coords, name="OLF_CELLS", colors="red"))
scene.add(Points(pir_coords, name="Piriform area CELLS", colors="green"))
scene.add(Points(th_coords, name="Thalamus area CELLS", colors="black"))
# render
scene.content
scene.render()
