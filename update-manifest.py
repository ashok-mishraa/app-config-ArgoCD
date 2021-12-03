#!/usr/bin/env python3

import argparse
import yaml

def updateManifest(environment, application, no_of_containers, tags):
    fileName = "".join([environment, "/", application, "/deployment.yml"])
    for i in range(no_of_containers):
        with open(fileName) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            image = data['spec']['template']['spec']['containers'][0]['image']
            imageNameSplit = image.split(':')
            application_repository = imageNameSplit[0]
            application_tag = tags[i]
            data['spec']['template']['spec']['containers'][0]['image'] = ":".join([application_repository, application_tag])

    with open(fileName, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
    print("Manifest updated successfully")

def main():
    parser = argparse.ArgumentParser(description='Application for updating the manifest file.')
    parser.add_argument('--e', "--environment", type=str, help='name of the environment', required=True)
    parser.add_argument('--n', "--no_of_containers", type=int, help='name of the environment', required=True)
    parser.add_argument('--a', "--application", type=str, help='name of the application', required=True)
    parser.add_argument('--t', "--tags", type=str, help='Tags of container separated by comma', required=True)
    args = parser.parse_args()
    app_tags = args.t.split(',')
    updateManifest(args.e, args.a, args.n, app_tags)

if __name__ == "__main__":
    main()
