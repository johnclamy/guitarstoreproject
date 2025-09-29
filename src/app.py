from guitar import Guitar
from inventory import Inventory


my_inventory = Inventory()
guitar_001 = Guitar("A90X-U234PQR500", 1500.0, "Fender", "Stratocaster", "Electric", "Alder", "Maple")
guitar_002 = Guitar("B21Y-V567STU600", 1200.0, "Gibson", "Les Paul", "Electric", "Mahogany", "Maple")
guitar_003 = Guitar("C34Z-W890VWX700", 800.0, "Yamaha", "FG800", "Acoustic", "Nato", "Spruce")
guitar_004 = Guitar("D45A-X123YZA800", 950.0, "Taylor", "214ce", "Acoustic", "Sapele", "Sitka Spruce")
guitar_005 = Guitar("E56B-Y456ZAB900", 1100.0, "Martin", "D-15M", "Acoustic", "Mahogany", "Mahogany")

my_inventory.add_guitar(guitar_001)
my_inventory.add_guitar(guitar_002)
my_inventory.add_guitar(guitar_003)
my_inventory.add_guitar(guitar_004)
my_inventory.add_guitar(guitar_005)

print(my_inventory.get_guitars())
