from dataclasses import dataclass
from pathlib  import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    URL: str
    locat_data_path:Path
    unzip_dir:Path
    
@dataclass    
class BaseModelConfig:
    root_dir:Path
    vgg_model:Path    
    
@dataclass
class Trainconfig:
    root_dir:Path
    vgg_model:Path
    final_model:Path
    train_data:Path
    test_data:Path
    val_data:Path    
        
    
