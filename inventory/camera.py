class Camera():

    def __init__(self, assetTag, description, opticalZoom):
        self._assetTag = assetTag
        self._description = description
        self._dueDate = ""
        self._isAvailable = True
        self._opticalZoom = opticalZoom

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