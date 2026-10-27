import sys
import platform

print("Hello from Python!")
print(f"版本: {sys.version.split()[0]}")
print(f"平台: {platform.system()} {platform.release()} ({platform.machine()})")
