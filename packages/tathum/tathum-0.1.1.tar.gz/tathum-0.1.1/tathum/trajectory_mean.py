from .trajectory import Trajectory
from .coord import Coord

import numpy as np
from scipy import interpolate


class TrajectoryMean:
    """
    A collection of individual trajectories and can be used to derive characteristics of the mean trajectories.
    """
    x = Coord()
    y = Coord()
    z = Coord()
    time = Coord()

    def __init__(self, exp_condition: dict):  # x, y, z, x_sd, y_sd, z_sd,
        self.all_trajectories = []
        self.exp_condition = exp_condition
        self.x_mean = None
        self.y_mean = None
        self.z_mean = None
        self.x_sd = None
        self.y_sd = None
        self.z_sd = None
        self.x_spline = None
        self.y_spline = None
        self.z_spline = None

    def add_trajectory(self, traj: Trajectory):
        self.all_trajectories.append(traj)

    def compute_mean_trajectory(self,
                                traj_names=('x_movement_fit', 'y_movement_fit', 'z_movement_fit')):
        for name in traj_names:
            coord_name = name[0]
            mean_name = f'{coord_name}_mean'
            sd_name = f'{coord_name}_sd'

            temp = None
            for traj in self.all_trajectories:
                temp_coord = traj.__getattribute__(name)

                # center the coordinate's starting position
                temp_coord -= temp_coord[0]

                if len(temp_coord.shape) < 2:
                    temp_coord = np.expand_dims(temp_coord, 1)

                if temp is None:
                    temp = temp_coord.copy()
                else:
                    temp = np.append(temp, temp_coord, axis=1)

            mean = np.mean(temp, axis=1)
            sd = np.std(temp, axis=1)   # / np.sqrt(temp.shape[1])
            self.__setattr__(mean_name, mean)
            self.__setattr__(sd_name, sd)

    def compute_bspline(self, smooth=0):
        ax_all = ('x', 'y', 'z')
        for ax in ax_all:
            mean_name = f'{ax}_mean'
            spline_name = f'{ax}_spline'
            temp_coord = self.__getattribute__(mean_name)
            time_vec = np.arange(len(temp_coord))
            tck = interpolate.splrep(time_vec, temp_coord,
                                     s=smooth,  # smoothing factor
                                     k=3,  # degree of the spline fit. Scipy recommends using cubic splines.
                                     )
            spline = interpolate.BSpline(tck[0], tck[1], tck[2])

            self.__setattr__(spline_name, spline)

    def debug_traj_2d_mean(self, x_axis, y_axis, var='', ax=None, center=True):
        def check_axis(axis_name, _var):
            axis_name = axis_name.lower()

            if _var != '':
                _var = f'_{_var}'

            if (axis_name == 'x') | (axis_name == 'y') | (axis_name == 'z'):
                pos = getattr(self, f'{axis_name}{_var}')
            elif axis_name == 'xy':
                pos = np.sqrt((getattr(self, f'x{_var}') ** 2 +
                               getattr(self, f'y{_var}') ** 2))
            elif axis_name == 'xz':
                pos = np.sqrt((getattr(self, f'x{_var}') ** 2 +
                               getattr(self, f'z{_var}') ** 2))
            elif axis_name == 'yz':
                pos = np.sqrt((getattr(self, f'y{_var}') ** 2 +
                               getattr(self, f'z{_var}') ** 2))
            else:
                raise ValueError("Unrecognized trajectory axis name! Only support 1D or 2D axes!")
            return pos - pos[0] if center else pos

        def check_axis_sd(axis_name):
            if (axis_name == 'x') | (axis_name == 'y') | (axis_name == 'z'):
                _sd = getattr(self, f'{axis_name}_sd')
            elif axis_name == 'xy':
                _sd = np.sqrt((getattr(self, 'x_sd') ** 2 +
                               getattr(self, 'y_sd') ** 2))
            elif axis_name == 'xz':
                _sd = np.sqrt((getattr(self, 'x_sd') ** 2 +
                               getattr(self, 'z_sd') ** 2))
            elif axis_name == 'yz':
                _sd = np.sqrt((getattr(self, 'y_sd') ** 2 +
                               getattr(self, 'z_sd') ** 2))
            else:
                raise ValueError("Unrecognized trajectory axis name! Only support 1D or 2D axes!")
            return _sd

        plot_x = check_axis(x_axis, var)
        plot_y = check_axis(y_axis, var)
        sd = check_axis_sd(y_axis)

        line = ax.plot(plot_x, plot_y, alpha=.5)
        ax.fill_between(plot_x, plot_y - sd, plot_y + sd, alpha=.2)
        return ax, line
