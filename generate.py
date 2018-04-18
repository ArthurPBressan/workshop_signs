from pathlib import Path
import shutil
import json

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

def generate_entity(job):
    job_alias = "stonehearth:jobs:{job}".format(job=job)
    return {
        "components": {
            "stonehearth:workshop": {
                "job_alias": job_alias
            }
        }
    }


def generate_mixinto(entity_pathname, job):
    key = "stonehearth:decoration:wooden_sign_{job}".format(job=job)
    file = "file({entity_pathname}/)".format(entity_pathname=entity_pathname)
    return key, [file]

def generate_filename(job):
    return "wooden_sign_{job}_workshop".format(job=job)

def main():
    _dist = './dist'
    shutil.rmtree(_dist, ignore_errors=True)
    dist = Path(_dist)
    dist.mkdir()

    for job in jobs:
        file_name = generate_filename(job)
        entity_pathname = "entities/{file_name}".format(file_name=file_name)
        mixinto_key, mixinto_files = generate_mixinto(entity_pathname, job)
        manifest['mixintos'][mixinto_key] = mixinto_files

        entity_dir = dist / entity_pathname
        entity_dir.mkdir(parents=True)
        entity_json = entity_dir / '{}.json'.format(file_name)
        entity = generate_entity(job)
        with entity_json.open(mode='w') as entity_file:
            json.dump(entity, entity_file)

    with (dist / 'manifest.json').open(mode='w') as manifest_file:
        json.dump(manifest, manifest_file)

if __name__ == '__main__':
    main()
