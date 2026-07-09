from magtrace.fields import ToroidalField
from magtrace.integrator import FieldTracer

field = ToroidalField()

tracer = FieldTracer(field)

solution = tracer.trace(
    r0=[1.5,0,0],
    length=40
)

print(solution.y.shape)