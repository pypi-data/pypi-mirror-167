"""
pixels2svg Copyright © 2022 Valentin François

Dependencies:

The Python Imaging Library (PIL) is

    Copyright © 1997-2011 by Secret Labs AB
    Copyright © 1995-2011 by Fredrik Lundh

Pillow is the friendly PIL fork. It is

    Copyright © 2010-2022 by Alex Clark and contributors

cc3d is

    Copyright © 2021 by William Silversmith

svgwrite

    Copyright © 2012 by Manfred Moitzi


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse

from pixels2svg.main import pixels2svg


def run_command():
    parser = argparse.ArgumentParser(description='pixels2svg CLI')
    parser.add_argument('input',
                        metavar='path',
                        type=str,
                        nargs=1,
                        help='input path of the bitmap image. If not '
                             'passed, will print the output in the terminal.')
    parser.add_argument('--output', '-o',
                        metavar='path',
                        type=str,
                        nargs=1,
                        help='output path of the bitmap image',
                        required=False)
    parser.add_argument('--no_group_by_color',
                        action='store_true',
                        help='do not group shapes of same color together '
                             'inside <g> tags ')
    parser.add_argument('--no_pretty',
                        action='store_true',
                        help='do not pretty-write the SVG code')

    args = parser.parse_args()

    output_str = pixels2svg(args.input[0],
                           output_path=args.output[0] if args.output else None,
                           group_by_color=not args.no_group_by_color,
                           as_string=not args.output,
                           pretty=not args.no_pretty)
    if output_str:
        print(output_str)
