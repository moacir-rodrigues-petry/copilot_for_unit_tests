import csv
from typing import TextIO, Union

class CatsFileProcessor:
    def __init__(self, storage_service):
        """Initialize with a CatsStorageService dependency."""
        self.storage_service = storage_service
    
    def process(self, file_obj: Union[str, TextIO]):
        """
        Process a CSV file containing cat information.
        
        Args:
            file_obj: Either a file path string or a file object already opened for reading
        """
        # Handle both file path strings and file objects
        close_file = False
        if isinstance(file_obj, str):
            file_obj = open(file_obj, 'r')
            close_file = True
            
        try:
            csv_reader = csv.DictReader(file_obj)
            for row in csv_reader:
                # Send each row to the storage service
                self.storage_service.store(row)
        finally:
            # Close the file if we opened it
            if close_file and file_obj:
                file_obj.close()


if __name__ == '__main__':
    from CatsStorageService import CatsStorageService
    import pprint
    storage_service = CatsStorageService()
    processor = CatsFileProcessor(storage_service)
    processor.process('cats.csv')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(storage_service.get_all_cats())