import bpy
for q in range(5):
    bpy.ops.mesh.primitive_cylinder_add(location=(q*5,0,0))
print("老婆是耐刮")