class Product:
    
    def __init__(self, productName, productPrice):
        self.__productName = productName
        self.__productPrice = productPrice

    
    def setProductName(self, productName):
        self.__productName = productName

    def setProductPrice(self, productPrice):
        self.__productPrice = productPrice

    def getProductName(self):
        return self.__productName

    def getProductPrice(self):
        return self.__productPrice

    def calculateTax(self):
        
        return self.__productPrice * 0.0825

    def getTotalPrice(self):
        return self.__productPrice + self.calculateTax()
