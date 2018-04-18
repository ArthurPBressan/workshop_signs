jobs = ["blacksmith", "carpenter", "cook", "engineer", "herbalist", "mason", "potter", "weaver"]

manifest = {
   "info" : {
      "name" : "Open Workshop With Signs",
      "namespace" : "workshop_signs",
      "version" : 3,
      "steam_file_id" : "1364538366"
   },
   "aliases" : {},
   "overrides" : {},
   "components" : {},
   "controllers" : {},

   "mixintos": {},
}

entity = {
   "components": {
      "stonehearth:workshop": {
         "job_alias": "stonehearth:jobs:blacksmith"
      }
   }
}

mixinto = {
    "stonehearth:decoration:wooden_sign_blacksmith": [
        "file(entities/wooden_sign_blacksmith_workshop/)"
    ]
}
