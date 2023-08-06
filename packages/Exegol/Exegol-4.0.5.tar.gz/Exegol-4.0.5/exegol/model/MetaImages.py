from typing import List


class MetaImages:
    """Meta model to store and organise multi-arch images"""

    def __int__(self, dockerhub_data):
        self.__images = None
        self.__multi_arch = True
        self.__meta_id = None

    def listArch(self) -> List[str]:
        pass
