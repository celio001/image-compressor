from abc import ABC, abstractmethod
from PIL import ImageFile, Image
from pathlib import Path
from io import BytesIO
from exceptions import NotImage

class ImageOptimizerTypesStrategy(ABC):

    @abstractmethod
    def optmize(self, img: ImageFile, quality: int) -> None:
        pass

class WebpPilOptimizer(ImageOptimizerTypesStrategy):

    def optmize(self, img: ImageFile, quality: int):
        output_path = BytesIO()
        img.save(output_path, 'webp', optimize=True, quality=quality)
        return output_path

#Strategy
class ImageOptimizer:
    def __init__(self, inpuy_path: str, compression: int, optimizer: ImageOptimizerTypesStrategy):
        self.inpuy_path = inpuy_path

        if not Path(self.output_path).exists():
            raise ModuleNotFoundError()
        
        self.compression = compression 
        self.optimizer = optimizer
        self.img = self._open_image()
    
    def optimize(self):
        return self.optimizer.optmize(img=self.img, quality=self.quality)

    def _open_image(self):
        try:
            img = Image.open(self.inpuy_path)
            img.verify()
            return Image.open(self.inpuy_path)
        except:
            raise NotImage(self.inpuy_path)

    @property
    def quality(self):
        return 1 if (100 - self.compression) == 0 else (100 - self.compression)
    
    