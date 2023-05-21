import torch
from data_utils import generate_input_img, extract_trimesh
from model import VNet
from torchvision.transforms import ToPILImage
import argparse
import numpy as np
# from matplotlib.pyplot import imshow

parser = argparse.ArgumentParser()
parser.add_argument('--input_rgb', required=True, type=str, help='input rgb image')
parser.add_argument('--input_mask', required=True, type=str, help='input mask image')
parser.add_argument('--output_dir', required=True, type=str, help='output directory')
args = parser.parse_args()

def normalize(mesh):
    rescale = max(mesh.extents)
    tform = [
    -(mesh.bounds[1][i] + mesh.bounds[0][i])/2.
    for i in range(3)
    ]
    matrix = np.eye(4)
    matrix[:3, 3] = tform
    mesh.apply_transform(matrix)
    matrix = np.eye(4)
    matrix[:3, :3] /= rescale
    mesh.apply_transform(matrix)

    return mesh

def main():
    # 1. Load the pre-trained checkpoint
    model_3d = VNet()
    model_3d.load_state_dict(torch.load("distilled_model.torch"))
    model_3d.eval()

    # 2. Preprocess an RGB image with associated object mask according to our model's input interface
    inp_img = generate_input_img(
        args.input_rgb,
        args.input_mask,
    )

    # 3. Obtain 3D prediction!
    out_mesh = extract_trimesh(model_3d, inp_img, "cuda")

    out_mesh = normalize(out_mesh)
    # To save the mesh
    out_mesh.export(args.output_dir + "/mesh.obj")
    # To visualize the mesh
    # out_mesh.show()

if __name__=="__main__":
    main()
