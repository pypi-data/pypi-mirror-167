# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)
from .base import ComponentBase


class Applets(ComponentBase):

    """Used to sync applets from a source instance to a destination instance of Swimlane."""

    def _update_reference_field_columns(self, applet: dict) -> None:
        """Checks and updates reference fields with the correct tracking-id in the provided applet.

        Args:
            applet (dict): A Swimlane applet dictionary.
        """
        needs_update = False
        for field in applet["fields"]:
            column_list = []
            if field.get("columns") and field.get("targetId"):
                # checking to see if the application referenced in this reference field exists
                # on the destination instance
                target = None
                if field["targetId"] in self.destination_instance.application_id_list:
                    # The targetId exists on the destination instance.
                    # Now we get the source application first
                    # We use that applications trackingFieldId as a our match criteria
                    source_app = self.source_instance.get_application(field["targetId"])
                    if source_app:
                        target = source_app["trackingFieldId"]
                if target:
                    column_list = []
                    for column in field["columns"]:
                        # If one of the columns in our reference field matches our source applications
                        # trackingFieldId (e.g. target) then we know the application now
                        if column == target:
                            needs_update = True
                            # We grab the new trackingFieldId from the destination instance application
                            dest_app = self.destination_instance.get_application(field["targetId"])
                            if dest_app:
                                column_list.append(dest_app["trackingFieldId"])
                        else:
                            # If that column does not match what we are looking for then just add it back into our
                            # column list
                            column_list.append(column)
                    field["columns"] = column_list
        if needs_update:
            if not ComponentBase.dry_run:
                self.log(f"Updating applet '{applet['name']}' on destination with correct tracking-ids.")
                self.destination_instance.update_applet(applet)
                self.log(f"Successfully updated applet '{applet['name']}' on destination with correct tracking-ids.")
            else:
                self.add_to_diff_log(applet["name"], "updated")

    def sync_applet(self, applet: dict) -> None:
        """Migrates a single applet to a destination instance.

        Args:
            applet (dict): An applet dictionary to migrate to a destination instance.
        """
        self.log(f"Processing source instance applet '{applet['name']}'.")
        self.scrub(applet)
        if not self._is_in_include_exclude_lists(applet["name"], "applets"):
            dest_applet = self.destination_instance.get_applet(applet["id"])
            if not dest_applet:
                if not ComponentBase.dry_run:
                    self.log(f"Adding applet '{applet['name']}' on destination.")
                    dest_applet = self.destination_instance.add_applet(applet=applet)
                    self.log(f"Successfully added applet '{applet['name']}' on destination.")
                    self._update_reference_field_columns(applet=dest_applet)
                else:
                    self.add_to_diff_log(applet["name"], "added")
            else:
                # removing these keys since they are not needed and only cause issues.
                dest_applet = self._set_unneeded_keys_to_empty_dict(component=dest_applet)
                if not ComponentBase.dry_run:
                    self.log(f"Updating applet '{dest_applet['name']}' on destination.")
                    dest_applet = self.destination_instance.update_applet(applet=applet)
                    self._update_reference_field_columns(applet=dest_applet)
                    self.log(f"Successfully updated applet '{dest_applet['name']}' on destination.")
                else:
                    self.add_to_diff_log(applet["name"], "updated")
        else:
            self.log(f"Skipping applet '{applet['name']}' since it is excluded.")

    def sync(self) -> None:
        """This method will sync all applets on a source instance with a destination instance."""
        self.log(f"Starting to sync 'Applets' from '{self.source_host}' to '{self.dest_host}'")
        for applet in self.source_instance.get_applets():
            self.sync_applet(applet=applet)
