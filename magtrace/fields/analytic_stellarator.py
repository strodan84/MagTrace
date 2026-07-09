import numpy as np


class AnalyticStellarator:
    """
    Simple analytic stellarator geometry model.

    Generates magnetic axis and nested flux surfaces.

    Parameters
    ----------
    R0 : float
        Average major radius.

    axis_amplitude : float
        Radial displacement of magnetic axis.

    Nfp : int
        Number of field periods.

    """

    def __init__(
        self,
        R0=3.0,
        axis_amplitude=0.3,
        Nfp=5,
        iota=0.4,   #rotational transform
    ):

        self.R0 = R0
        self.axis_amplitude = axis_amplitude
        self.Nfp = Nfp
        self.iota = iota
        # self.kappa = kappa
        # self.delta = delta


    def magnetic_axis(self, phi):
        """
        Compute stellarator magnetic axis.

        Parameters
        ----------
        phi : array
            Toroidal angle.

        Returns
        -------
        R, Z
            Cylindrical coordinates of magnetic axis.
        """

        R = (
            self.R0
            + self.axis_amplitude
            * np.cos(self.Nfp * phi)
        )

        Z = (
            self.axis_amplitude
            * np.sin(self.Nfp * phi)
        )

        return R, Z



    def flux_surface(self, r, theta, phi):

        R_axis, Z_axis = self.magnetic_axis(phi)

        '''
        The shaping (kappa and delta) is allowed 
        to vary with toroidal angle phi because stellarator 
        cross-sections evolve around the torus, but the 
        poloidal angle itself remains a geometric coordinate.
        '''
        shape = self.Nfp * phi

        kappa = 1.0 + 0.5*np.cos(shape)     #elongation
        delta = 0.25*np.sin(shape)          #triangularity
 
        R = (
            R_axis
            + r*np.cos(theta)
            + delta*r*np.sin(theta)
        )

        Z = (
            Z_axis
            + kappa*r*np.sin(theta)
        )

        return R, Z


    def trace_field_line(
        self,
        r=0.5,
        theta0=0.0,
        turns=20,
        points_per_turn=500,
    ):
        """
        Trace a magnetic field line on a flux surface.

        Parameters
        ----------
        r : float
            Minor radius.

        theta0 : float
            Initial poloidal angle.

        turns : int
            Number of toroidal revolutions.

        Returns
        -------
        x,y,z
        """

        phi = np.linspace(
            0,
            turns*2*np.pi,
            turns*points_per_turn
        )

        theta = theta0 + self.iota*phi

        R, Z = self.flux_surface(
            r,
            theta,
            phi
        )

        return self.cylindrical_to_cartesian(
            R,
            phi,
            Z
        )




    def cylindrical_to_cartesian(
        self,
        R,
        phi,
        Z
    ):
        """
        Convert cylindrical coordinates to Cartesian.
        """

        x = R*np.cos(phi)
        y = R*np.sin(phi)

        return x, y, Z