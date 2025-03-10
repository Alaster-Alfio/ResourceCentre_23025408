from inventory.item import Item

class Camera(Item):

    def __init__(self, assetTag, description, opticalZoom):
        super().__init__(assetTag, description)
        self._opticalZoom = opticalZoom

    def __str__(self):
        return "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            self.getAssetTag(), self.getDescription(),
            self.getIsAvailable(), self.getDueDate(), self.getOpticalZoom())

    def getAssetTag(self):
        return self._assetTag

    def getDescription(self):
        return self._description

    def getDueDate(self):
        return self._dueDate

    def getIsAvailable(self):
        if self._isAvailable == True:
            return "Yes"
        else:
            return "No"

    def getOpticalZoom(self):
        return self._opticalZoom

    def setDueDate(self, dueDate):
        self._dueDate = dueDate

    def setIsAvailable(self, isAvailable):
        self._isAvailable = isAvailable