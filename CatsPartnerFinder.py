class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __repr__(self):
        return f"Cat({self.name}, {self.color})"



class CatsPartnerFinder:
    def __init__(self, cats_list: list[Cat]):
        """
        Initialize the CatsPartnerFinder with a list of cats.

        Args:
            cats_list (list): List of Cat objects
        """
        self.cats = cats_list

    def find_best_match(self, person_favorite_color: str, person_favorite_animals: list[str], person_age: int):
        """
        Find the best matching cat based on the person's preferences.

        Match rules:
            - If the person is older than 90, they are considered too old for a cat.
            - If the person's favorite color is the same as the cat's color, it's a match.
            - If the person's favorite animals include felines like cats, lions, or tigers, it's a match.


        Args:
                person_favorite_color (str): The person's favorite color.
                person_favorite_animals (list[str]): The person's favorite animals.
                person_age (int): The person's age.

        Returns:
                Cat: The best matching cat, or None if no matches are found.
        """
        if person_age > 90:
            return None

        for cat in self.cats:
            if cat.color == person_favorite_color:
                return cat

            # animals accepted: "lion", "tiger", "cat"
            if any(animal in person_favorite_animals for animal in ["lion", "tiger", "cat"]):
                return cat

        return None
