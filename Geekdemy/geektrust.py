import sys
from src.programmes import ManagementSystem, ProgrammeDetails
from src.coupons import *
from src.constants import *
from src.core import *


def getInput(input_file_name=None):
    """
        Reads inputs from commandline argument or 
        optionally from an file(for testing)

        Args:
            input_file_name(str, optional): input file name
            Default is none
    """
    if input_file_name is None:
        input_file_name = sys.argv[-1]

    # user = User()
    management_system = ManagementSystem()
    programmes_list = []
    coupons_list = []
    b4g1 = Coupon_B4G1("B4G1")
    coupons_list.append(b4g1)

    with open(input_file_name, 'r') as file:
        for _line in file.readlines():
            _line = _line.replace('\n', '')
            _line = _line.rstrip()
            _list = _line.split(' ')

            if _list[0].startswith(InputFormat.ADD_PROGRAMME.value):
                programme = ProgrammeDetails(_list[1], float(_list[2]))
                programmes_list.append(programme)
                # user.addProgramme(_list[1], float(_list[2]))

            elif _list[0].startswith(InputFormat.APPLY_COUPON.value):
                if _list[1] == CouponsEnum.DEAL_G20.value:
                    deal_20 = Coupon_G20(_list[1])
                    coupons_list.append(deal_20)
                else:
                    deal_5 = Coupon_G5(_list[1])
                    coupons_list.append(deal_5)
                # user.addCoupon(_list[1])

            elif _line.startswith(InputFormat.ADD_PRO_MEMBERSHIP.value):
                management_system.add_promembership(programmes_list)

            elif _line.startswith(InputFormat.PRINT_BILL.value):
                # management_system.apply_coupons(programmes_list, coupons_list)
                management_system.print_bill(programmes_list, coupons_list)

            else:
                pass


if __name__ == "__main__":
    getInput()
