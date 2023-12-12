#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse

import numpy as np

from inflammation import models, views


def main(p_args: argparse.Namespace):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    in_files = p_args.infiles
    if not isinstance(in_files, list):
        in_files = [p_args.infiles]

    on_screen: bool = p_args.onscreen

    for filename in in_files:
        inflammation_data = models.load_csv(filename)

        view_data = {
            'average': models.daily_mean(inflammation_data),
            'std': models.daily_std(inflammation_data),
            'max': models.daily_max(inflammation_data),
            'min': models.daily_min(inflammation_data)
        }

        if on_screen:
            print(f'\n{filename}:\n-------------------------')
            print('\t'.join(view_data.keys()))
            for v in zip(*view_data.values()):
                print('\t'.join(map(str, np.round(v, 4))))

        # views.visualize(view_data)


if __name__ == "__main__":
    def str2bool(s: str) -> bool:
        if not isinstance(s, str):
            msg = f'Argument should be a string; {type(s)} given'
            raise TypeError(msg)

        s = s.lower()
        if s in ('1', 't', 'y', 'true', 'yes', 'on'):
            return True
        elif s in ('0', 'f', 'n', 'false', 'no', 'off'):
            return False

        msg = 'Invalid truth value'
        raise ValueError(msg)

    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system'
    )

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient'
    )
    parser.add_argument(
        '--onscreen',
        default=False,
        type=str2bool,
        help='Output statistics on screen'
    )

    args = parser.parse_args()

    main(args)
