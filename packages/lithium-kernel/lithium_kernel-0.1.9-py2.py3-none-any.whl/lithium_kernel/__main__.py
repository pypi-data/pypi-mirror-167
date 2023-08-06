from ipykernel.kernelapp import IPKernelApp
from .kernel import LithiumKernel, load_definitions

definitions = load_definitions()
IPKernelApp.launch_instance(kernel_class=LithiumKernel)
