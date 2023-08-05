"""openalpr class Alpr implementation
"""
from openalpr import Alpr
import cv2
import json
import numpy as np
import re


class NumberPlateRecognizer:
    """Class implementation of openalpr python bindings

    Parameters
    __________
    region : str
        region configuration to use
    config_dir : str
        openalpr configuration directory
    runtime_dir : str
        openalpr runtime directory

    Attributes
    __________
    region : str
        region configuration to use

    config_dir : str
        openalpr configuration directory

    runtime_dir : str
        openalpr runtime directory

    alpr : object
        Alpr class instance

    alpr.set_detect_region(True) : bool
        auto detect region

    alpr.set_top_n(10) : int
        number of results to return

    Methods
    _______
    get_output([array]) -> json array object

    extract_number_plate([array]) -> [str, str, array, list]

    plate_confidence([json]) -> str

    unload -> None

    set_region(str) -> None

    """

    def __init__(
        self,
        region="us, vn2, eu",
        config_dir="/etc/openalpr/openalpr.conf",
        runtime_dir="/usr/share/openalpr/runtime_data",
    ):
        self.region = region
        self.config_dir = config_dir
        self.runtime_dir = runtime_dir
        self.alpr = Alpr(self.region, self.config_dir, self.runtime_dir)
        self.alpr.set_detect_region(True)
        self.alpr.set_top_n(10)

    def get_output(self, frame):
        """
        :param frame: from cv2.VideoCapture.read()/ cv2.imread()
        :return: json array object of possible characters in detected region
        """

        results = self.alpr.recognize_ndarray(frame)

        return results

    def extract_number_plate(
        self,
        frame,
        regex=None,
    ):
        """function takes an input in the form of an array

        :param regex: code for matching OCR results with plate configuration
        :param frame: from cv2.VideoCapture().read()

        :returns: recognized plate, confidence value, detection points, regex plate results
        :rtype: [str, str, array, list]

        """

        results = self.alpr.recognize_ndarray(frame)

        if regex is None:
            regex = re.compile("[KG][A-Z][A-Z][0-9][0-9][0-9][A-Z]")
        candidates = list()

        for i, plate in enumerate(results["results"]):

            best_candidate = plate["candidates"][0]

            for p in plate["candidates"]:
                if len(p["plate"]) == 7:
                    candidates.append(p["plate"])

            confidence = "{:.2f}".format(best_candidate["confidence"])
            plate = best_candidate["plate"]

            points = []
            for k in range(4):
                cor1x = json.dumps(results["results"][i]["coordinates"][k]["x"])
                cor1y = json.dumps(results["results"][i]["coordinates"][k]["y"])

                points.append([cor1x, cor1y])
            points = np.array(points)

            lps = list(filter(regex.match, candidates))
            return plate, confidence, points, lps

    @staticmethod
    def plate_confidence(alpr_output):
        """plate number and confidence value

        :param alpr_output: array input from self.alpr.recognize_ndarray(frame)
        :returns: plate number and confidence value
        """

        for i, plate in enumerate(alpr_output["results"]):

            best_candidate = plate["candidates"][0]

            plate = "{:7s} ({:.2f}%) ".format(
                best_candidate["plate"].upper(), best_candidate["confidence"]
            )

            return plate

    def unload(self):
        """call function after completion of processing using Alpr class

        :returns: None
        """
        self.alpr.unload()

    def set_region(self, plt_region):
        """set region configuration to use

        :param plt_region: accepts country as a string e.g us, br which can have multiple values seperated by a comma
        used to set the region param of alpr
        :returns: None
        """
        self.region = self.alpr.set_country(plt_region)
