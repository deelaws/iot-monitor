import enum

class SwitchType(enum.Enum):
    CeilingLight  = "ceiling-light"
    CeilingFan = "ceiling-fan"
    DeskFan    = "desk-fan"
    DeskLamp   = "desk-lamp"
    GenericSwitch = "gen-switch"
    

    @staticmethod
    def get_type_from_string(stype):
        if "ceiling-light" == mtype:
            return SwitchType.CeilingLight
        elif "ceiling-fan" == stype:
            return SwitchType.CeilingFan
        elif "desk-fan" == stype:
            return SwitchType.DeskFan
        elif "desk-lamp" == stype:
            return SwitchType.DeskLamp
        elif "gen-switch" == stype:
            return SwitchType.GenericSwitch
        else:
            return None
        