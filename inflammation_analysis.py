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
    # positional arguments
    in_files = p_args.infiles
    if not isinstance(in_files, list):
        in_files = [p_args.infiles]

    # optional arguments
    on_screen: bool = p_args.onscreen
    as_graph: bool = p_args.graph

    # skip if no view is required
    if (not on_screen) and (not as_graph):
        print(f'Data not processed: Both visualisations disabled.')
        return

    # process and view data
    for filename in in_files:
        inflammation_data = models.load_csv(filename)

        view_data = {
            'average': models.daily_mean(inflammation_data),
            'std': models.daily_std(inflammation_data),
            'max': models.daily_max(inflammation_data),
            'min': models.daily_min(inflammation_data)
        }

        if on_screen:
            views.on_screen(view_data)

        if as_graph:
            views.visualize(view_data)


if __name__ == "__main__":


    def str2bool(s: str) -> bool:
        """Convert string-value to boolean:
         -  True:   {'1', 't', 'y', 'true', 'yes', 'on'}
         -  False:  {'0', 'f', 'n', 'false', 'no', 'off'}

        :param s: string-representation
        :type s: str

        :return: boolean representation
        :rtype: bool

        :raises TypeError: if `s` is not a string
        :raises ValueError: if `s` cannot be represented as a boolean
        """
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
        '--graph',
        default=True,
        type=str2bool,
        help='Output statistics as graph'
    )
    parser.add_argument(
        '--onscreen',
        default=False,
        type=str2bool,
        help='Output statistics on screen'
    )

    args = parser.parse_args()

    main(args)
