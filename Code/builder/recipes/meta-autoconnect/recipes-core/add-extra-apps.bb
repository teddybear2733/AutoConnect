
LICENSE = "GPL-3.0"

#SRC_URI += "file://${TOPDIR}/../../ExtraApps"

APP_DIR = "${TOPDIR}/../recipes/meta-autoconnect/Apps/ExtraApps"

do_install() {
    install -m 0644 ${APP_DIR}/myDir ${D}/home/root
}
FILES_${PN} += "/home/root"
