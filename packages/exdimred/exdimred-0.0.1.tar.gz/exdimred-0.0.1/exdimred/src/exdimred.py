def warn(*args, **kwargs):
    pass

import warnings
import numpy as np
import matplotlib.pyplot as plt
import itertools
from sklearn.decomposition import *
from sklearn.manifold import *
from umap import UMAP
from tqdm import tqdm


warnings.simplefilter("ignore", UserWarning)
warnings.simplefilter("ignore", FutureWarning)



def face_cube(dim, samples_per_edge, shift=0, size=1):
    """
    Generate points on the faces of a cube
    
    :param dim:               Dimensionality of cube
    :param samples_per_edge:  Number of samples along one edge
    :param shift:             Translation away from origin (applied in each dimension)
    :param size:              Edge length of cube
    :return:                  Numpy array of point coordinates
    """
    
    edge = np.arange(-size, size + (2 * size) / samples_per_edge, step=(2 * size) / samples_per_edge)
    list_list = []
    for idx in range(edge.shape[0]):
        coord = edge[idx]
        point_list = [coord] * dim
        list_list.append(np.around(point_list, decimals=2))

    list_coords = list(itertools.product(*zip(*list_list)))

    good_points = []

    for item in list_coords:
        if size in np.abs(item):

            if shift == 0:

                good_points.append(item)
            else:
                item = list(item)
                for i, element in enumerate(item):
                    item[i] = element + shift

                good_points.append(tuple(item))
    return np.array(good_points).transpose()


def edge_cube(dim, samples_per_edge, shift=0, size=1):
    """
    Generate points on the edges of a cube
    
    :param dim:                 Dimensionality of cube
    :param samples_per_edge:    Number of samples on a cube edge
    :param shift:               Shift away from origin (applied to each dimension)
    :param size:                Size of cube
    :return:                    Numpy array of point coordinates
    """
    edge = np.arange(-size, size + (2 * size) / samples_per_edge, step=(2 * size) / samples_per_edge)
    list_list = []
    for idx in range(edge.shape[0]):
        coord = edge[idx]
        point_list = [coord] * dim
        list_list.append(np.around(point_list, decimals=2))

    list_coords = list(itertools.product(*zip(*list_list)))

    good_points = []

    for item in list_coords:

        index = np.array(np.abs(item))
        index = index[index == size]

        if index.shape[0] >= 2:

            if shift == 0:

                good_points.append(item)
            else:
                item = list(item)
                for i, element in enumerate(item):
                    item[i] = element + shift

                good_points.append(tuple(item))
    return np.array(good_points).transpose()


def draw_gaussian(N=1000, dim=3, r=1, shift=0.):
    """
    Generates a gaussian distribution
    
    :param N:       Number of points in distribution
    :param dim:     Dimensionality of distribution
    :param r:       Deviation of distribution
    :param shift:   Translation from origin (applied in each dimension)
    :return:        Numpy array of point coordinates
    """
    
    # Generate gaussian distribution
    norm = np.random.normal
    normal_deviates = norm(size=(dim, N))
    
    trans = shift * np.ones((dim, N))  # Vector used for translation

    # Scale distribution and translate
    normal_deviates = r * normal_deviates + trans

    return normal_deviates


def true_random(N=1000, dim=3, r=1, shift=0.):
    """
    Generates a random point cloud

    :param N:       Number of points in cloud
    :param dim:     Dimensionality of cloud
    :param r:       Maximum range of cloud from origin
    :param shift:   Translation from origin (applied in each dimension)
    :return:        Numpy array of point coordinates
    """

    # Generate random distribution
    norm = np.random.random
    points = norm(size=(dim, N))

    # Scale and translate
    trans = shift * np.ones((dim, N))
    normal_deviates = r * points + trans

    # Identifiers
    ids = np.ones(N)
    return normal_deviates, ids


def gaussian_overlap(N=500, shift=1.25):
    """
    Generate two overlapping gaussians using draw_gaussian.
    Specific to this work, so fixed at 3D.

    :param N:       Number of points in each gaussian
    :param shift:   Shift of one gaussian from origin
    :return:        Numpy array of point coordinates, IDs for points in each gaussian
    """

    # Generate two gaussians, one shifted and with smaller deviation
    g1 = draw_gaussian(N = N)
    g2 = draw_gaussian(N = N, r=0.5, shift=shift)

    # Create overall array of point coordinates
    g = np.append(g1, g2, axis=1)

    # IDs for points in gaussians for visualisation (modelling two-class problem)
    g_ids = np.append(np.ones(N), 2 * np.ones(N))

    return g, g_ids


def draw_sphere(N=1000, dim=3, r=1, shift=0.):
    """
    Generate point coordinates sampled on the surface of a sphere
    
    :param N:       Number of points generated
    :param dim:     Dimensionality of sphere
    :param r:       Radius of sphere
    :param shift:   Translation from origin (applied in each dimension)
    :return:        Numpy array of point coordinates
    """
    
    # Generate normal distribution in dimensionality D
    norm = np.random.normal
    normal_deviates = norm(size=(dim, N))
    
    # Calculate point displacements from origin
    displacements =  np.sqrt((normal_deviates ** 2).sum(axis=0))
    
    # Normalise each point to displacement r
    points = r * normal_deviates / displacements
    
    # Translation
    trans = shift * np.ones((dim, N))
    points += trans

    return points


def draw_corkscrew(radius=1, n_revs=5, N=5000, theta0=0, height=0, reverse=False):
    """
    Generate a corkscrew centred on the origin
    
    :param r:           Radius of corkscrew
    :param n_revs:      Number of corkscrew rotations
    :param N:           Number of points sampled
    :param theta0:      Starting rotation in radians (0 is along primary axis)
    :param height:      Height of corkscrew
    :param reverse:     Whether to reverse the rotation direction
    :return:            Numpy array of point coordinates
    """

    # Generate angles for each point
    if reverse:
        theta = np.linspace(np.pi * n_revs + theta0, theta0, num=N)
    else:
        theta = np.linspace(theta0, np.pi * n_revs + theta0, num=N)

    # Generate points in corkscrew
    r = radius * np.ones(N)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.linspace(height, radius + height, num=N)

    return np.array([x, y, z])


def corkscrew_in_corkscrew(n_revs=5, N=1000, reverse=False):
    """
    Generate two corkscrews pi radians out of phase

    :param n_revs:   Number of corkscrew revolutions
    :param N:        Number of points per corkscrew
    :param reverse:  Whether to reverse one of the corkscrews
    :return:         Numpy array of point coordinates, numpy array of point identifiers
    """

    # Generate individual corkscrews
    corkscrew_1 = draw_corkscrew(N=N, n_revs=n_revs)
    corkscrew_2 = draw_corkscrew(theta0=np.pi, height=0.05, N=N, reverse=reverse, n_revs=n_revs)

    # Identifiers for each corkscrew
    sp1_ids = 1 * np.ones(N)
    sp2_ids = 2 * np.ones(N)

    # Final point coordinates and identifiers
    corkscrews = np.append(corkscrew_1, corkscrew_2, axis=1)
    sp_ids = np.append(sp1_ids, sp2_ids)

    return corkscrews, sp_ids


def sphere_in_sphere(N=500, inner_r=0.6, outer_r=1, relative_number = True, inner_shift=0, dim=3):
    """
    Generate point coordinates sampled from one sphere surface within another

    :param N:               Number of points in outer sphere
    :param inner_r:         Radius of inner sphere
    :param outer_r:         Radius of outer sphere
    :param relative_number  Whether to scale the number of points in the inner sphere according to surface area
    :param inner_shift:     Translation of inner sphere away from origin (applied in each dimension)
    :param dim:             Dimensionality of spheres
    :return:                Numpy array of point coordinates, numpy array of identifiers for each sphere
    """

    # Calculate number of points in inner sphere if relative_number == True
    if relative_number:
        size_relative = inner_r / outer_r
        samples_difference = size_relative ** (1 / 2)
        inner_samples = int(N * samples_difference)
    else:
        inner_samples = N

    # Generate point coordinates for each sphere
    sphere_1 = draw_sphere(N=N, r=1, dim=dim, shift=0)
    sphere_2 = draw_sphere(N=inner_samples, r=inner_r, dim=dim, shift=inner_shift)

    # Identifiers for each sphere
    sphere_1_ids = np.ones(sphere_1.shape[1])
    sphere_2_ids = 2 * np.ones(sphere_2.shape[1])

    # Final point coordinates and identifiers
    points = np.append(sphere_1, sphere_2, axis=1)
    sphere_ids = np.append(sphere_1_ids, sphere_2_ids)

    return points, sphere_ids

def cube_in_cube(N=40, inner_size = 0.75, outer_size=1, relative_number = True, dim=3):
    """
    Generate points sampled from the edges of two cubes, one inside the other

    :param N:                   Controls number of points to sample in outer cube. Not directly the number of points sampled.
    :param inner_size:          Side length of inner cube
    :param outer_size:          Side length of outer cube
    :param relative_number:     Whether to scale number of points sampled from inner cube according to relative cube sizes
    :param dim:                 Dimensionality of generated cubes
    :return:                    Numpy array of point coordinates and cube identifiers
    """

    #  Compute relative number of points in inner cube
    if relative_number:
        size_relative = inner_size / outer_size
        inner_samples = int(N * size_relative)
    else:
        inner_samples = N

    #  Sample points along the edges of two cubes
    cube_1 = edge_cube(dim, inner_samples, size=inner_size)
    cube_2 = edge_cube(dim, N, size=outer_size)

    #  Identifiers for each cube
    cube_1_ids = np.ones(cube_1.shape[1])
    cube_2_ids = 2 * np.ones(cube_2.shape[1])

    # Final point coordinates and identifiers
    cube = np.append(cube_1, cube_2, axis=1)
    cube_ids = np.append(cube_1_ids, cube_2_ids)

    return cube, cube_ids


def iterate_model(models, data, ids, labels):

    n_samples = len(data)
    n_models = len(models)

    fig = plt.figure(figsize=( 4 * n_samples, 4 * (n_models + 1.1)), constrained_layout = True)
    plt.rcParams["axes.edgecolor"] = "black"
    plt.rcParams["axes.linewidth"] = 2.50

    pbar = tqdm(enumerate(data))
    for i, s in pbar:

        cube = s
        cube_ids = ids[i]

        ax1 = plt.subplot(n_models + 1, n_samples, i + 1, projection = "3d")
        ax1.scatter(*cube[:3, :], c=cube_ids, vmax=3)
        ax1.set_yticklabels([])
        ax1.set_xticklabels([])
        ax1.set_zticklabels([])

        ax1.set_title(labels[i], fontsize=30)

        for n, m in enumerate(models):

            model_string = str(m)
            model_name = model_string.split(".")[-1][:-2]

            ax2 = plt.subplot(n_models+1, n_samples, n_samples*(n+1) + i + 1)

            ax2.set_yticklabels([])
            ax2.set_xticklabels([])
            pbar.set_description(str(m))


            core_models = ["UMAP","TSNE","MDS","Isomap", "LocallyLinearEmbedding","SpectralEmbedding"]
            if model_name in core_models:
                umap = m(n_components=2, n_jobs=6)
            elif model_name == "KernelPCA":
                umap = m(n_components=2, kernel="rbf", gamma=5)
                model_name = "RBF-KernelPCA"

            else:
                umap = m(n_components=2)
            umap_embedding = umap.fit_transform(cube.transpose())

            ax2.scatter(*umap_embedding.transpose(), c=cube_ids, vmax=3)

            if i == 0:

                ax2.set_ylabel(f"{model_name}", fontsize=30)

        del cube, cube_ids, umap_embedding

    try:
        plt.savefig("exdimred.pdf", bbox_inches = "tight")
    except:
        plt.savefig("exdimred.png", bbox_inches="tight")

def run(model = None):
    cube1, cube_ids1 = cube_in_cube()
    sphere1, sphere_ids1 = sphere_in_sphere()
    corkscrew, corkscrew_ids = corkscrew_in_corkscrew()
    gauss, gauss_ids = gaussian_overlap()
    r, r_ids = true_random()

    if model is not None:
        models = [PCA, TruncatedSVD, MDS, SpectralEmbedding, TSNE, UMAP, model]
    else:
        models = [PCA, TruncatedSVD, MDS, SpectralEmbedding, TSNE, UMAP]

    iterate_model(models,
                  [cube1, sphere1, corkscrew, gauss, r],
                  [cube_ids1, sphere_ids1, corkscrew_ids, gauss_ids, r_ids],
                  ["Cube in Cube", "Sphere in Sphere\n(shells)", "Corkscrews",
                   "Intersecting\nGaussians", "Random"])