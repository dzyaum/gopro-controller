from goprocam import GoProCamera, constants

print("Connecting to GoPro...")
cam = GoProCamera.GoPro(constants.gpcontrol)
print("Connected!")
print(cam.getStatus(constants.Status.Status, constants.Status.STATUS.Mode))
