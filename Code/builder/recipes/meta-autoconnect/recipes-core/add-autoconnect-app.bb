LICENSE = "GPL-3.0"


APP_DIR = "${TOPDIR}/../recipes/meta-autoconnect/Apps/AutoConnectAApp"

do_install() {
    install -m 0644 ${APP_DIR}/myDir ${D}/home/root
}
FILES_${PN} += "/home/root"
