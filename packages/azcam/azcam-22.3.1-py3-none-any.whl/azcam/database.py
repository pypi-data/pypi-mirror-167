"""
*azcam.database* contains the main azcam database class.

There is only one instance of this class which is referenced as `azcam.db` and contains
temporary data for this current process.
"""

from typing import Any, Union, List, Dict

from azcam.logger import Logger


class AzcamDatabase(object):
    """
    The azcam database class.
    """

    _instance = None

    _errorstatus = ["OK", "errorstatus is depricated"]

    #: the current working directory
    wd: Union[str, None] = None
    #: verbosity level for messages
    verbosity: int = 1
    #: operating mode (server or console)
    mode: str = ""
    #: abort flag, 1 (true) if an abort has occurred
    abortflag: int = 0
    #: system datafolder
    datafolder: str = ""

    #: dict of tools
    tools: dict = {}
    #: name of default tool
    default_tool = None

    #: dict of shortcuts
    shortcuts: dict = {}

    #: dict of scripts
    scripts: dict = {}

    #: header objects
    headers: dict = {}
    #: header order in image header
    headerorder: list = []
    #: logger object
    logger: Logger = Logger()

    #: dict of general parameters
    pardict: dict = {
        # exposure
        "autotitle": "exposure.auto_title",
        "imagetype": "exposure.image_type",
        "exposureflag": "exposure.exposure_flag",
        "exposuresequencedelay": "exposure.exposure_sequence_delay",
        "exposuresequencetotal": "exposure.exposure_sequence_total",
        "exposuresequencenumber": "exposure.exposure_sequence_number",
        "exposuresequenceflush": "exposure.exposure_sequence_flush",
        "exposureupdatingheader": "exposure.updating_header",
        "isexposuresequence": "exposure.is_exposure_sequence",
        "displayimage": "exposure.display_image",
        "sendimage": "exposure.send_image",
        "savefile": "exposure.save_file",
        "flusharray": "exposure.flush_array",
        "tdidelay": "exposure.tdi_delay",
        "tdimode": "exposure.tdi_mode",
        "pardelay": "exposure.par_delay",
        "exposureguidemode": "exposure.guide_mode",
        "exposureguidestatus": "exposure.guide_status",
        "lastfilename": "exposure.last_filename",
        "imagefiletype": "exposure.filetype",
        "imageheaderfile": "exposure.imageheaderfile",
        "imagetest": "exposure.test_image",
        "imagesequencenumber": "exposure.sequence_number",
        "imageautoincrementsequencenumber": "exposure.auto_increment_sequence_number",
        "imageincludesequencenumber": "exposure.include_sequence_number",
        "imageautoname": "exposure.autoname",
        "imageoverwrite": "exposure.overwrite",
        "imageroot": "exposure.root",
        "imagefolder": "exposure.folder",
        "remote_imageserver_host": "sendimage.remote_imageserver_host",
        "remote_imageserver_port": "sendimage.remote_imageserver_port",
        # image
        "imagesizex": "exposure.image.focalplane.numcols_image",
        "imagesizey": "exposure.image.focalplane.numrows_image",
        "numpiximage": "exposure.image.focalplane.numpix_image",
        "colbin": "exposure.image.focalplane.col_bin",
        "rowbin": "exposure.image.focalplane.row_bin",
        "firstcol": "exposure.image.focalplane.first_col",
        "firstrow": "exposure.image.focalplane.first_row",
        "lastcol": "exposure.image.focalplane.last_col",
        "lastrow": "exposure.image.focalplane.last_row",
        # instrument
        "instrumentenabled": "instrument.enabled",
        "instrumentfocus": "instrument.focus_position",
        # telescope
        "telescopeenabled": "telescope.enabled",
        "telescopefocus": "telescope.focus_position",
        # tempcon
        "controltemperature": "tempcon.control_temperature",
        "camtemp": "tempcon.temperatures[0]",
        "dewtemp": "tempcon.temperatures[1]",
        # controller
        "utilityboardinstalled": "controller.utility_board_installed",
        "pciboardinstalled": "controller.pci_board_installed",
        "timingboardinstalled": "controller.timing_board_installed",
        "videogain": "controller.video_gain",
        "videospeed": "controller.video_speed",
        "usereadlock": "controller.use_read_lock",
        "pcifile": "controller.pci_file",
        "timingfile": "controller.timing_file",
        "utilityfile": "controller.utility_file",
        "timingboard": "controller.timing_board",
        "videoboards": "controller.video_boards",
        "clockboards": "controller.clock_boards",
        # database
        "systemname": "db.systemname",
        "abortflag": "db.abortflag",
        "errorstatus": "db._errorstatus",
        "verbosity": "db.verbosity",
        "hostname": "db.hostname",
    }

    #: image parameters
    imageparnames: List[str] = [
        "imageroot",
        "imageincludesequencenumber",
        "imageautoname",
        "imageautoincrementsequencenumber",
        "imagetest",
        "imagetype",
        "imagetitle",
        "imageoverwrite",
        "imagefolder",
    ]

    #: exposure flags
    exposureflags: Dict[str, int] = {
        "NONE": 0,
        "EXPOSING": 1,
        "ABORT": 2,
        "PAUSE": 3,
        "RESUME": 4,
        "READ": 5,
        "PAUSED": 6,
        "READOUT": 7,
        "SETUP": 8,
        "WRITING": 9,
        "GUIDEERROR": 10,
        "ERROR": 11,
    }

    # *************************************************************************
    # db methods
    # *************************************************************************

    def __init__(self) -> None:

        if 0:
            if AzcamDatabase._instance is None:
                AzcamDatabase._instance = self
            else:
                raise Exception("AzcamDatabase instance already exists")

    def get(self, name: str) -> Any:
        """
        Returns a database attribute by name.
        Args:
          name: name of attribute to return
        Returns:
          value or None if *name* is not defined
        """

        try:
            obj = getattr(self, name)
        except AttributeError:
            obj = None

        return obj

    def set(self, name: str, value: Any) -> None:
        """
        Sets a database attribute value.
        Args:
          name: name of attribute to set
          value: value of attribute to set
        """

        # if not hasattr(self, name):
        #    return

        setattr(self, name, value)

        return
