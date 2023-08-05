# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)
from typing import Union

from deepdiff import DeepDiff

from ..base import Base


class Differ(Base):
    """Identifies the differences between two components."""

    def __init__(self, source: Union[dict, list], destination: Union[dict, list]) -> None:
        """Checks the difference between two components.

        Args:
            source (Union[dict, list]): The source instance component.
            destination (Union[dict, list]): The destination instance component.
        """
        self.source = source
        self.destination = destination

    def check(self) -> bool:
        """Checks whether the two provided objects are different or not.

        Args:
            source (list or dict): The source object.
            destination (list or dict): The destination object.

        Returns:
            bool: Returns True if the two objects are different, False is the same.
        """
        if isinstance(self.source, dict) and isinstance(self.destination, dict):
            if self.source.get("id") and self.destination.get("id"):
                self.source["id"] = self.destination["id"]
            for key in ["createdDate", "modifiedDate"]:
                if self.source.get(key):
                    self.source[key] = ""
                if self.destination.get(key):
                    self.destination[key] = ""
            for key in ["createdByUser", "modifiedByUser"]:
                if self.source.get(key):
                    self.source[key] = {}
                if self.destination.get(key):
                    self.destination[key] = {}
            if DeepDiff(self.source, self.destination, ignore_order=True):
                return True
            return False
        elif isinstance(self.source, list) and isinstance(self.destination, list):
            if DeepDiff(self.source, self.destination, ignore_order=True):
                return True
            return False
