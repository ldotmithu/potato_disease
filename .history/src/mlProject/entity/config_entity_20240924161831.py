from dataclasses import dataclass
from pathlib  import Path


@dataclass
class DataIngestionConfig:
    roo_dir: Path
    URL: str
    locat_data_path:Path
    unzip_dir:Path
    
