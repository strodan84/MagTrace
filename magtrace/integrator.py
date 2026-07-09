import numpy as np
from scipy.integrate import solve_ivp



def field_line_equation(s, r, field):
    """
    Differential equation for magnetic field line tracing.

    Parameters
    ----------
    s : float
        Path length (independent variable)

    r : array_like
        Position [x,y,z]

    field : MagneticField
        Magnetic field object
    """

    x, y, z = r

    B = field.field(x, y, z)

    norm = np.linalg.norm(B)

    if norm < 1e-12:
        return np.zeros(3)

    return B / norm



class FieldTracer:
    """
    Numerically traces magnetic field lines using scipy.solve_ivp.

    Parameters
    ----------
    field : MagneticField
    Magnetic field model to integrate.
    """

    def __init__(self, field):
        self.field = field


    def trace(
        self,
        r0,
        length=20.0,
        npoints=2000
    ):
        
        
        t_eval = np.linspace(0, length, npoints)

        solution = solve_ivp(
            field_line_equation,
            (0, length),
            r0,
            args=(self.field,),
            t_eval=t_eval,
            rtol=1e-8,
            atol=1e-10
        )

        if not solution.success:
            raise RuntimeError(solution.message)
    
        return {
            "x": solution.y[0],
            "y": solution.y[1],
            "z": solution.y[2],
            "s": solution.t,
            "solution": solution,
        }