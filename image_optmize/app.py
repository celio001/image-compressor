from abc import ABC, abstractmethod
from PIL import ImageFile, Image
from pathlib import Path
from exceptions import NotImage
class ImageOptimizerTypesStrategy(ABC):

    @abstractmethod
    def optmize(self, img: ImageFile, output_path: str, quality: int) -> None:
        pass

class WebpPilOptimizer(ImageOptimizerTypesStrategy):

    def optmize(self, img, output_path, quality):
        print('Estou otimizando')

class WebpCVOptimizer(ImageOptimizerTypesStrategy):
    def optmize(self, img, output_path, quality):
        print('Estou otimizando com opencv')

#Strategy
class ImageOptimizer:
    def __init__(self, inpuy_path: str, ouytput_path: str, compression: int, optimizer: ImageOptimizerTypesStrategy):
        self.inpuy_path = inpuy_path
        self.ouytput_path = ouytput_path

        if not Path(self.ouytput_path).exists():
            raise ModuleNotFoundError()
        
        self.compression = compression 
        self.optimizer = optimizer
    
    def optimize(self):
        self.optimizer.optmize('', '', '')

    def _open_image(self):
        try:
            img = Image.open(self.inpuy_path)
            img.verify()
        except:
            raise NotImage(self.inpuy_path)
        

x = ImageOptimizer('', '', 0, WebpCVOptimizer())
x.optimize()