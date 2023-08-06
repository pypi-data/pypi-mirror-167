import json
import copy
def get_webhook(model, is_resolved=False):
   webhook_template_c = copy.deepcopy(webhook_template)
   webhook_template_c["incident"]["incident_updates"][-1]["body"] = \
       webhook_template_c["incident"]["incident_updates"][-1]\
    ["body"].replace("<model replacement>", model)

   if is_resolved:
       webhook_template_c["incident"]["incident_updates"].append({"status":"resolved"})
   return json.dumps(webhook_template_c)

webhook_template = {
   "meta":{
      "unsubscribe":"http://statustest.flyingkleinbrothers.com:5000/?unsubscribe=j0vqr9kl3513",
      "documentation":"http://doers.statuspage.io/customer-notifications/webhooks/"
   },
   "page":{
      "id": "j2mfxwj97wnj",
      "status_indicator": "critical",
      "status_description": "Major System Outage"
   },
   "incident":{
      "backfilled":False,
      "created_at":"2013-05-29T15:08:51-06:00",
      "impact":"critical",
      "impact_override":None,
      "monitoring_at":"2013-05-29T16:07:53-06:00",
      "postmortem_body":None,
      "postmortem_body_last_updated_at":None,
      "postmortem_ignored":False,
      "postmortem_notified_subscribers":False,
      "postmortem_notified_twitter":False,
      "postmortem_published_at":None,
      "resolved_at":None,
      "scheduled_auto_transition":False,
      "scheduled_for":None,
      "scheduled_remind_prior":False,
      "scheduled_reminded_at":None,
      "scheduled_until":None,
      "shortlink":"http://j.mp/18zyDQx",
      "status":"monitoring",
      "updated_at":"2013-05-29T16:30:35-06:00",
      "id":"lbkhbwn21v5q",
      "organization_id":"j2mfxwj97wnj",
      "incident_updates":[
         {
            "body":"A fix has been implemented and we are monitoring the results.",
            "created_at":"2013-05-29T16:07:53-06:00",
            "display_at":"2013-05-29T16:07:53-06:00",
            "status":"monitoring",
            "twitter_updated_at":None,
            "updated_at":"2013-05-29T16:09:09-06:00",
            "wants_twitter_update":False,
            "id":"drfcwbnpxnr6",
            "incident_id":"lbkhbwn21v5q"
         },
         {
            "body":"We are waiting for the cloud to come back online and will update when we have further information",
            "created_at":"2013-05-29T15:18:51-06:00",
            "display_at":"2013-05-29T15:18:51-06:00",
            "status":"identified",
            "twitter_updated_at":None,
            "updated_at":"2013-05-29T15:28:51-06:00",
            "wants_twitter_update":False,
            "id":"2rryghr4qgrh",
            "incident_id":"lbkhbwn21v5q"
         },
         {
            "body":"We are experiencing increased latencies for models across the board starting 2pm, leading to increased load & errors in <model replacement> by around 3pm. We have a potential mitigation we are going to try.",
            "created_at":"2013-05-29T15:08:51-06:00",
            "display_at":"2013-05-29T15:08:51-06:00",
            "status":"investigating",
            "twitter_updated_at":None,
            "updated_at":"2013-05-29T15:28:51-06:00",
            "wants_twitter_update":False,
            "id":"qbbsfhy5s9kk",
            "incident_id":"lbkhbwn21v5q"
         }
      ],
      "name":"test"
   }
}