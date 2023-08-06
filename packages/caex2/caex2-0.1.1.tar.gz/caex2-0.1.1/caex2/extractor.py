#!/usr/bin/env python
# coding: utf-8
import logging
import tempfile
from pathlib import Path

import click
from git import Repo

logging.basicConfig(format='%(message)s', level=logging.INFO)


def get_indented_blocks(episode_lines):
    indented_blocks = []
    block = []
    for line in episode_lines:
        if line.startswith('>'):
            block.append(line.strip())
        elif len(block) > 0:
            if line.startswith('{'):
                block.append(line.strip())
            indented_blocks.append(block)
            block = []
    return indented_blocks


def strip_challenge(block):
    stripped_block = []
    for line in block:
        if not line.startswith('> >'):
            line_stripped = line[1:].strip()
            if not line_stripped.startswith('{:'):
                stripped_block.append(line_stripped)
    return stripped_block


def extract_challenges_from_blocks(indented_blocks):
    challenges = [block[:-1] for block in indented_blocks if 'challenge' in block[-1]]
    stripped_challenges = ['\n'.join(strip_challenge(c)) for c in challenges]
    return stripped_challenges


def extract_episode(episode_lines):
    indented_blocks = get_indented_blocks(episode_lines)
    challenges = extract_challenges_from_blocks(indented_blocks)
    return challenges


def extract_challenges(episode_filepath, output_file):
    with open(episode_filepath) as fin:
        episode_lines = fin.readlines()
    challenges = extract_episode(episode_lines)

    # Write to output file
    with open(output_file, 'a') as fout:
        fout.write(f'# Episode {episode_filepath.name} \n\n')
        for block in challenges:
            fout.write(block)
            fout.write('\n\n')


def get_episode_paths(repo_dir: Path):
    episode_dir = repo_dir / '_episodes'
    episode_paths = sorted([path for path in episode_dir.iterdir() if path.name not in ['.gitkeep']])

    if len(episode_paths) == 0:
        episode_dir = repo_dir / '_episodes_rmd'
        episode_paths = sorted([path for path in episode_dir.iterdir() if path.name not in ['.gitkeep']])
    return episode_paths

@click.command()
@click.argument('lesson_url')
@click.option('--output', default='exercises-document.md', help='Name of output file to write to')
def main(lesson_url, output):
    """
    Extract exercises from LESSON_URL

    LESSON_URL is a carpentries lesson's Github page
    """
    open(output, 'w').close()  # Wipe output file content
    with Path(tempfile.TemporaryDirectory().name) as temp_dir:
        logging.info(f'Cloning {lesson_url} in temporary directory')
        repo_dir = temp_dir / 'repo'
        Repo.clone_from(lesson_url, repo_dir)
        episode_paths = get_episode_paths(repo_dir)
        logging.info(f'Found {len(episode_paths)} episodes')
        for episode_path in episode_paths:
            extract_challenges(episode_path, output)
            logging.info(f'Extracted exercises from {episode_path.name}')


if __name__ == '__main__':
    main()
