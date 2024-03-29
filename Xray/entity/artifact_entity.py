from datclasses import dataclass 
from torch.util.data.dataloader import DataLoader 

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str