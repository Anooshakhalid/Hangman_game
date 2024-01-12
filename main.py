import adminfile
import Logininfo
interface = input("Want to Enter as Admin or Player?,(A,P): ").upper()
if interface == "A":
    adminfile.administrator_interface()
elif interface == "P":
    Logininfo.selecting()
else:
    print("Select right choice!")
