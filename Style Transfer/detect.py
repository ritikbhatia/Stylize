from detecto import core, utils, visualize
from torchvision.utils import save_image


def run_detect(image_name):
    image = utils.read_image(image_name)
    model = core.Model()
    labels, boxes, scores = model.predict_top(image)
    return visualize.show_labeled_image(image, boxes, labels)
