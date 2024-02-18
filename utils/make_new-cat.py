import os
import yaml

def parse_yaml_file(file_path):
    """
    Read a YAML file and parse it into a dictionary.

    Parameters:
        file_path (str): The path to the YAML file.

    Returns:
        dict: A dictionary containing the parsed YAML content.
    """
    with open(file_path, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    return yaml_content

def create_markdown_file(directory, filename, content):
    """
    Creates a Markdown file with the specified content in the given directory.
    
    Parameters:
        directory (str): The directory where the Markdown file will be created.
        filename (str): The name of the Markdown file.
        content (str): The content to be written to the Markdown file.
    """
    # Create the full file path
    filepath = os.path.join(directory, filename)
    
    # Write content to the file
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Markdown file '{filename}' created successfully in '{directory}'.")


content = '''---
# Featured tags need to have either the `list` or `grid` layout (PRO only).
layout: list

# The title of the tag's page.
title: {}

# The name of the tag, used in a post's front matter (e.g. tags: [<slug>]).
slug: {}

# (Optional) Write a short (~150 characters) description of this featured tag.
description: >
  

# (Optional) You can disable grouping posts by date.
no_groups: true

# Exclude this example category from the sitemap.
# DON'T USE THIS SETTING IN YOUR CATEGORIES!
sitemap: false
---
'''

if __name__=='__main__':
    # Example usage:
    yaml_file_path = "../_config.yml"  # Specify the path to your YAML file
    parsed_yaml = parse_yaml_file(yaml_file_path)
    for cat in parsed_yaml['menu']:
        if cat['title'] in ['About', 'Documentation']:
            continue
        title = cat['title']
        slug = cat['url'].strip('/')
        new_category_md = content.format(title, slug)
        directory = '../_featured_categories'
        filename = f'{slug}.md'

        # Create markdown file in _featured_categories
        create_markdown_file(directory, filename, new_category_md)

        # Create new directoyr that stores new cateogory's post directory 
        new_directory_path = f'../{slug}/_posts'
        if not os.path.exists(new_directory_path):
            os.mkdir(new_directory_path)
            print(f'{new_directory_path} created successfully')
        print('=======================')
