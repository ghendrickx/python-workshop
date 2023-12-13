#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse

import numpy as np

from inflammation import models, views


def poem(func):

    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
        import this
    return wrapper_func


@poem
def main(p_args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    in_files = p_args.infiles
    if not isinstance(in_files, list):
        in_files = [p_args.infiles]

    # process and view data
    for filename in in_files:
        inflammation_data = models.load_csv(filename)
        if p_args.view == 'visualise':
            view_data = {
                'average': models.daily_mean(inflammation_data),
                'max': models.daily_max(inflammation_data),
                'min': models.daily_min(inflammation_data)
            }

            views.visualize(view_data)

        elif p_args.view == 'record':
            patient_data = inflammation_data[p_args.patient]
            observations = [models.Observation(day, value) for day, value in enumerate(patient_data)]
            patient = models.Patient('UNKNOWN', observations=observations)

            views.display_patient_record(patient)


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
        '--view',
        default='visualise',
        choices=['visualise', 'record'],
        help='Which view should be used?'
    )
    parser.add_argument(
        '--patient',
        type=int,
        default=0,
        help='Which patient should be displayed?'
    )

    args = parser.parse_args()

    main(args)
