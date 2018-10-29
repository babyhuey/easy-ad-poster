import yaml

def create_config_file(config):
    with open('config.yaml', 'w+') as f:
        f.write(yaml.safe_dump(config, default_flow_style=False))