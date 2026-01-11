from src.maps.map import Map
from src.config import map_mapping
import pickle

class Saver:
    @staticmethod
    def save(map: Map) -> None:
        map = map
        with open('save.dat', 'wb') as f:
            pickle.dump(map.map_id, f)


    @staticmethod
    def load() -> Map:
        try:
            with open('save.dat', 'rb') as f:
                map_id = pickle.load(f)
        except FileNotFoundError:
            map_id = 'Home'

        return map_mapping.get(map_id)
