from guitar import Guitar
from inventory import Inventory
from builder import Builder
from guitar_type import GuitarType
from wood import Wood


my_inventory = Inventory()
guitar_001 = Guitar("A90X-U234PQR500", 1499.99, Builder.FENDER, "Stratocaster", GuitarType.ELECTRIC, Wood.ALDER, Wood.MAPLE)
guitar_002 = Guitar("B21Y-V567STU600", 1199.99, Builder.GIBSON, "Les Paul", GuitarType.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE)
guitar_003 = Guitar("C34Z-W890VWX700", 799.99, Builder.YAMAHA, "FG800", GuitarType.ACOUSTIC, Wood.NATO, Wood.SPRUCE)
guitar_004 = Guitar("D45A-X123YZA800", 949.99, Builder.TAYLOR, "214ce", GuitarType.ACOUSTIC, Wood.SAPELE, Wood.SITKA_SPRUCE)
guitar_005 = Guitar("E56B-Y456ZAB900", 1099.99, Builder.MARTIN, "D-15M", GuitarType.ACOUSTIC, Wood.MAHOGANY, Wood.MAHOGANY)
guitar_006 = Guitar("F67C-Z789ABC100", 1449.99, Builder.FENDER, "Stratocaster", GuitarType.ELECTRIC, Wood.ALDER, Wood.MAPLE)

my_inventory.add_guitar(guitar_001)
my_inventory.add_guitar(guitar_002)
my_inventory.add_guitar(guitar_003)
my_inventory.add_guitar(guitar_004)
my_inventory.add_guitar(guitar_005)
my_inventory.add_guitar(guitar_006)

search_rslt = my_inventory.search_guitar(Builder.FENDER, "Stratocaster", GuitarType.ELECTRIC, Wood.ALDER, Wood.MAPLE)
print(search_rslt if search_rslt else "Guitar not found")
