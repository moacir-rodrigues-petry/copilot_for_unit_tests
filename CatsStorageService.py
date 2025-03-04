class CatsStorageService:
    def __init__(self):
        """Initialize the storage service."""
        self.cats = []
    
    def store(self, cat_data: dict):
        """
        Store cat information.
        
        Args:
            cat_data: Dictionary containing cat information from a CSV row.
        """
        self.cats.append(cat_data)
        # print(f"Stored cat: {cat_data}")
    
    def get_all_cats(self):
        """Return all stored cats."""
        return self.cats
