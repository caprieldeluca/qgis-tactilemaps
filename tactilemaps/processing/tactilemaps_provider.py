# -*- coding: utf-8 -*-
""" Tactile Maps Processing provider.

************************************************************************
    Name                : tactilemaps_provider.py
    Date                : March 2023
    Copyright           : (C) 2023-2025 by Laboratorio de Geociencias - FIE
    Email               : geociencias@fie.undef.edu.ar
************************************************************************
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
************************************************************************
"""

from pathlib import Path

from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsProcessingProvider

from tactilemaps.processing.algorithms import (
    computescale_algorithm,
    extractedges_algorithm,
    rasterize_algorithm,
    scalevectorlayer_algorithm,
    writebraille_algorithm
)


class TactileMapsProvider(QgsProcessingProvider):
    """Tactile Maps provider class."""

    def tr(self, string):
        """Return a localized string."""
        return QCoreApplication.translate('TactileMapsProvider', string)

    def loadAlgorithms(self, *args, **kwargs):
        """Load the algorithms of the provider."""
        self.addAlgorithm(computescale_algorithm.ComputeScale())
        self.addAlgorithm(extractedges_algorithm.ExtractEdges())
        self.addAlgorithm(rasterize_algorithm.RasterizeMap())
        self.addAlgorithm(scalevectorlayer_algorithm.ScaleVectorLayer())
        self.addAlgorithm(writebraille_algorithm.WriteBraille())

    def id(self, *args, **kwargs):
        """Return the id of the provider."""
        return 'tactilemaps'

    def name(self, *args, **kwargs):
        """Return the display name of the provider."""
        return self.tr('Tactile maps')

    def icon(self):
        """Return the icon of the provider."""
        icon = QIcon(str(Path(__file__).parent.parent / "icon.png"))
        return icon
