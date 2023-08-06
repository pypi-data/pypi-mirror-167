import re
import json
class Webhook_Handler:
    def __init__(self, webhook, first_choice_model='curie', engine_type='text'):
        self.webhook = json.loads(webhook)
        self.first_choice_model = first_choice_model
        self.engine_type = engine_type
        # as of 9/13/22
        self.engine_versions = {"text": {"ada":"text-ada-001", "babbage": "text-babbage-001", "curie":"text-curie-001", "davinci":"text-davinci-002"},
              "code":{"davinci":"code-davinci-002", "cushman":"code-cushman-001"}
              }
    def get_model_names_list(self):
        return list(self.engine_versions[self.engine_type].keys())
    def get_model_version_list(self):
        return list(self.engine_versions[self.engine_type].values())
    def find_model_index(self, model):
        return self.get_model_names_list().index(model)
    def indices_of_usable_models(self,models_involved_flags):
        return [i for i, model_flag in enumerate(models_involved_flags) if model_flag]
    def choose_backup_model(self, models_involved_flags):
        ideal_index = self.find_model_index(self.first_choice_model)
        good_indices = [i for i in self.indices_of_usable_models(models_involved_flags)]
        diffs = [(i - ideal_index)  for i in good_indices]
        return sorted(diffs, key = abs, reverse=True)[-1] + ideal_index
    def model_finder(self, incident_body):
        search_patterns = [".*" + engine + ".*" for engine in self.engine_versions[self.engine_type].values()]
        return [re.search(patterns, incident_body) is None for patterns in search_patterns]
    def get_status_reports(self, status):
        return [updt for updt in self.webhook["incident"]["incident_updates"] if updt["status"] == status]
    """Assumes that their is only one incident happening at a time"""
    def handle_incident(self):
        #assumes only one investigation incident at a time
        incident_reports = self.get_status_reports("investigating")[0]
        models_involved_flags = self.model_finder(incident_reports["body"])
        print(models_involved_flags)
        # if preffered model is ok to use still use it
        if models_involved_flags[self.find_model_index(self.first_choice_model)]:
             return self.engine_versions[self.engine_type][self.first_choice_model]
        # using orderd dict, python 3.7+?
        return self.get_model_version_list()[self.choose_backup_model(models_involved_flags)]
    def is_resolved(self):
        print(self.webhook)
        return  len(self.get_status_reports("resolved")) > 0
    def handle_webhook(self):
        if self.is_resolved(): self.engine_versions[self.engine_type][self.first_choice_model]
        return self.handle_incident()
