# Base this image on core-image-base
include recipes-extended/images/core-image-full-cmdline.bb

COMPATIBLE_MACHINE = "^rpi$"

IMAGE_FEATURES += " splash x11-base hwcodecs"

IMAGE_INSTALL = "\
	packagegroup-core-boot \
	packagegroup-core-full-cmdline \
	packagegroup-rpi-test \
    psplash \
    sudo nano usbutils \
	python3 \
	python3-kivy \
	python3-pip \
	openjre-8 \
	"


LICENSE = "MIT"

inherit core-image
