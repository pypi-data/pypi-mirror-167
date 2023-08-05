# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)
import re
from abc import abstractmethod
from typing import Any, Dict

from ..base import Base


class ComponentBase(Base):
    """A base class for all components.

    This class is used to ensure that all derived classes have a sync method as well as shared methods.
    """

    MASKED_VALUE = re.compile(r"^\*{3,}$")

    def _replace(self, component: dict, search_value: str, replace_value: str) -> Dict[str, str]:
        """Recursively replaces any key or values matching a provided value with another one.

        Args:
            component (dict): The given component dictionary object.
            search_value (str): The value to search for.
            replace_value (str): The value to replace any matches found with.

        Returns:
            dict: Returns an updated dictionary with the replaced values.
        """
        if isinstance(component, dict):
            new_dict = {}
            for k, v in component.items():
                key = k
                if k == search_value:
                    key = replace_value
                new_dict[key] = self._replace(v, search_value, replace_value)
            return new_dict
        elif isinstance(component, list):
            new_list = []
            for v in component:
                new_list.append(self._replace(v, search_value, replace_value))
            return new_list
        else:
            if component == search_value:
                return replace_value
            else:
                return component

    def _set_unneeded_keys_to_empty_dict(self, component, keys=["createdByUser", "modifiedByUser", "permissions"]):
        """A component object to remove defined keys from.

        Args:
            component (dict or attrs): A Swimlane component object to clean.
            keys (list): A list of keys to set as empty dictionaries.

        Returns:
            dict or attrs: Returns an updated component with the values set as empty dictionaries.
        """
        for key in keys:
            if isinstance(component, dict):
                if component.get(key):
                    component[key] = {}
        return component

    def _get_field_by_type(self, field_list: list, field_type: str = "tracking") -> dict:
        """Returns a field dictionary by its defined type.

        Args:
            field_list (list): A list of application fields.
            field_type (str, optional): The fieldType value of the field. Defaults to "tracking".

        Returns:
            dict: A swimlane application field dictionary.
        """
        for field in field_list:
            if field.get("fieldType") and field["fieldType"] == field_type:
                return field

    def is_masked(self, value: Any) -> bool:
        """Returns true or false if the provided value is masked.

        Args:
            value (Any): A value to check if it is masked with ***.

        Returns:
            bool: Returns True if the value is masked. False if not.
        """
        if isinstance(value, str):
            return self.MASKED_VALUE.match(value)
        return False

    @abstractmethod
    def sync(self):
        """Every component must have a defined sync method.

        Raises:
            NotImplementedError: Raises when a component does not have a sync method defined.
        """
        raise NotImplementedError("The class does not have a sync method.")
