from dataclasses import dataclass
from pathlib  import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    URL: str
    locat_data_path:Path
    unzip_dir:Path
    
class BaseMModelConfig:
    root_dir:Path
    vgg_model:Path    
    
