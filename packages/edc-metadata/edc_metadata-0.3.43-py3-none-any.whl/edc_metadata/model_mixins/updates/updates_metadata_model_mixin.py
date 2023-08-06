from typing import Any, Optional, Protocol

from django.apps import apps as django_apps
from django.db import models
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from ...constants import CRF, NOT_REQUIRED, REQUIRED, REQUISITION


class CrfLikeModelInstance(Protocol):
    subject_visit: Any
    visit: Any
    metadata_query_options: Any
    metadata_visit_object: Any
    metadata_default_entry_status: Any
    metadata_updater_cls: Any
    metadata_category: Any
    metadata_model: Any
    metadata_update: Any
    _meta: Any


class MetadataError(Exception):
    pass


class UpdatesMetadataModelMixin(models.Model):

    metadata_updater_cls = None
    metadata_category = None

    def metadata_update(self: Any, entry_status: Optional[str] = None) -> None:
        """Updates metatadata."""
        self.metadata_updater.update(entry_status=entry_status)

    def run_metadata_rules_for_crf(self: CrfLikeModelInstance) -> None:
        """Runs all the metadata rules."""
        self.related_visit.run_metadata_rules()

    @property
    def metadata_updater(self: CrfLikeModelInstance) -> None:
        """Returns an instance of MetadataUpdater."""
        return self.metadata_updater_cls(
            visit_model_instance=self.related_visit, target_model=self._meta.label_lower
        )

    def metadata_reset_on_delete(self: CrfLikeModelInstance) -> None:
        """Sets this model instance`s metadata model instance
        to its original entry_status.
        """
        obj = self.metadata_model.objects.get(**self.metadata_query_options)
        try:
            obj.entry_status = self.metadata_default_entry_status
        except IndexError:
            # if IndexError, implies CRF is not listed in
            # the visit schedule, so remove it.
            # for example, this is a PRN form
            obj.delete()
        else:
            obj.entry_status = self.metadata_default_entry_status or REQUIRED
            obj.report_datetime = None
            obj.save()

    @property
    def metadata_default_entry_status(self: CrfLikeModelInstance) -> str:
        """Returns a string that represents the default entry status
        of the CRF in the visit schedule.
        """
        crfs_prn = self.metadata_visit_object.crfs_prn
        if self.related_visit.visit_code_sequence != 0:
            crfs = self.metadata_visit_object.crfs_unscheduled + crfs_prn
        else:
            crfs = self.metadata_visit_object.crfs + crfs_prn
        crf = [c for c in crfs if c.model == self._meta.label_lower][0]
        return REQUIRED if crf.required else NOT_REQUIRED

    @property
    def metadata_visit_object(self: CrfLikeModelInstance) -> Any:
        visit_schedule = site_visit_schedules.get_visit_schedule(
            visit_schedule_name=self.related_visit.visit_schedule_name
        )
        schedule = visit_schedule.schedules.get(self.related_visit.schedule_name)
        return schedule.visits.get(self.related_visit.visit_code)

    @property
    def metadata_query_options(self: CrfLikeModelInstance) -> dict:
        options = self.related_visit.metadata_query_options
        options.update(
            {
                "subject_identifier": self.related_visit.subject_identifier,
                "model": self._meta.label_lower,
            }
        )
        return options

    @property
    def metadata_model(self: CrfLikeModelInstance) -> Any:
        """Returns the metadata model associated with self."""
        if self.metadata_category == CRF:
            metadata_model = "edc_metadata.crfmetadata"
        elif self.metadata_category == REQUISITION:
            metadata_model = "edc_metadata.requisitionmetadata"
        else:
            raise MetadataError(f"Unknown metadata catergory. Got {self.metadata_category}")
        return django_apps.get_model(metadata_model)

    class Meta:
        abstract = True
