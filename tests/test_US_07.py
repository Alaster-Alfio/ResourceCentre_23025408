import pytest
from inventory.inventory import Inventory

class Test_US_07:
    ############### Test return camera ######################
    def test_return_camera_onLoan(self):
        test_inventory = Inventory()
        test_inventory.addCamera("C001", "Test camera 1", 5)
        tested_camera = test_inventory.cameraList[0]
        test_inventory.loanCamera(tested_camera.getAssetTag(), "08-08-2030")
        
        result = test_inventory.returnCamera(tested_camera.getAssetTag())

        assert result == True
        assert tested_camera.getDueDate() == ""
        assert tested_camera.getIsAvailable() == "No"

    def test_return_camera_not_onLoan(self):
        test_inventory = Inventory()
        test_inventory.addCamera("C001", "Test camera 1", 5)
        tested_camera = test_inventory.cameraList[0]

        result = test_inventory.returnCamera(tested_camera.getAssetTag())

        assert result == False
        assert tested_camera.getDueDate() == ""
        assert tested_camera.getIsAvailable() == "Yes"

    def test_return_camera_not_exists(self):
        test_inventory = Inventory()
        test_inventory.addCamera("C001", "Test camera 1", 5)
        
        result = test_inventory.returnCamera("C003")
        
        assert result == False

    ############### Test return laptop ######################
    def test_return_laptop_onLoan(self):
        test_inventory = Inventory()
        test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        tested_laptop = test_inventory.laptopList[0]
        test_inventory.loanLaptop(tested_laptop.getAssetTag(), "08-08-2030")

        result = test_inventory.returnLaptop(tested_laptop.getAssetTag())
        assert result == True
        assert tested_laptop.getDueDate() == ""
        assert tested_laptop.getIsAvailable() == "Yes"

    def test_return_laptop_not_onLoan(self):
        test_inventory = Inventory()
        test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        tested_laptop = test_inventory.laptopList[0]

        result = test_inventory.returnLaptop(tested_laptop.getAssetTag())
        
        assert result == False
        assert tested_laptop.getDueDate() == ""
        assert tested_laptop.getIsAvailable() == "Yes"

    def test_return_laptop_not_exists(self):
        test_inventory = Inventory()
        test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        
        result = test_inventory.returnLaptop("L003")
        
        assert result == False 
