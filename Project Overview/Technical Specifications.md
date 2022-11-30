<!-----

Yay, no errors, warnings, or alerts!

Conversion time: 0.581 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β33
* Tue Nov 29 2022 05:49:29 GMT-0800 (PST)
* Source doc: AutoConnect Technical Specifications
* Tables are currently converted to HTML tables.
----->


AutoConnect Technical Specifications

Section A - Hardware

**Hardware**

**General:**

Below is a set of compatible tested hardware for the AutoConnect Project. This is not an exhaustive list, however it is designed to give a general idea of tested compatible hardware for the end user.

**Raspberry Pi Hardware List:**

**	**Below contains a chart of all the supported Raspberry Pi Hardware platforms that have been tested and list of accompanying displays.

Figure 1.1


<table>
  <tr>
   <td><strong>Supported Platforms</strong>
   </td>
   <td><strong>Untested Platforms</strong>
   </td>
   <td><strong>Displays (Tested)</strong>
   </td>
  </tr>
  <tr>
   <td>Raspberry Pi 3B
   </td>
   <td>Raspberry Pi 3A+
   </td>
   <td>Official Raspberry Pi 7” Display
   </td>
  </tr>
  <tr>
   <td>Raspberry Pi 3B+
   </td>
   <td>Raspberry Pi 4A
   </td>
   <td>ElecLab Raspberry Pi 5” Display
   </td>
  </tr>
  <tr>
   <td>Raspberry Pi 4 A
   </td>
   <td>
   </td>
   <td>7 Inch Generic HDMI Touchscreen
   </td>
  </tr>
</table>


 

**Device I/O Specifications:**

**	**Below contains a chart of the hardware I/O that the OS will need to be present to fully function.

Untested devices that do not contain all of these I/O options will not be able to fully utilize the AutoConnect software.

	This chart is to be referred to when deciding on the accompanying hardware for your choice of device

Figure 1.2


<table>
  <tr>
   <td><strong>Supported Device</strong>
   </td>
   <td><strong>Input</strong>
   </td>
   <td><strong>Output</strong>
   </td>
   <td><strong>Power (Recommended)</strong>
   </td>
  </tr>
  <tr>
   <td>Raspberry Pi 3B
   </td>
   <td>40 GPIO pins 
<p>
Micro SD Card
   </td>
   <td>40 GPIO pins 
<p>
HDMI Output
<p>
Aux Output
<p>
Display Connector
<p>
Camera Connector
<p>
4x USB
<p>
1x Ethernet
   </td>
   <td>5v ~1 Amp - Micro USB
   </td>
  </tr>
  <tr>
   <td>Raspberry Pi 3B+
   </td>
   <td>40 GPIO pins 
<p>
Micro SD Card
   </td>
   <td>40 GPIO pins 
<p>
HDMI Output
<p>
Aux Output
<p>
Display Connector
<p>
Camera Connector
<p>
4x USB
<p>
1x Ethernet
   </td>
   <td>5v ~1 Amp - Micro USB
   </td>
  </tr>
  <tr>
   <td>Raspberry Pi 4 A
   </td>
   <td>40 GPIO pins 
<p>
Micro SD Card
   </td>
   <td>40 GPIO pins 
<p>
2x Micro HDMI
<p>
4x USB A
<p>
Aux Output
<p>
DSI Display Connector
<p>
Camera Connector
   </td>
   <td>5v ~3.0 Amp - USB C
<p>
Or POE
   </td>
  </tr>
</table>


**Note: **If using a screen that draws power from the device, it is recommended to supply at least 2.5Amps at 5v.

**Car ECU Connection Devices:**

**	**These are the only tested ECU connection devices, others may work.


          Figure 1.3


<table>
  <tr>
   <td><strong>Tested ECU Connectors</strong>
   </td>
  </tr>
  <tr>
   <td>RadioShack 6’ Serial Cable
   </td>
  </tr>
  <tr>
   <td>Built In Bluetooth module in applicable ECU cases
   </td>
  </tr>
</table>


**ECU’s:**

**	**The AutoConnect Project has been tested with the following ECU’s

      Figure 1.4


<table>
  <tr>
   <td><strong>Tested ECU’s</strong>
   </td>
  </tr>
  <tr>
   <td>MSPNP2 - (With TunerStudioMS)
   </td>
  </tr>
  <tr>
   <td>MS3 Pro PNP - (With TunerStudioMS)
   </td>
  </tr>
</table>


Section B - Software

**Software**

**General:**

This Section will contain all of the technical specifications for the software platform.

**Operating System:**

The AutoConnect platform utilizes a modified fork of Raspian running on a raspberry pi. 

Specifically the fork will be based on (Raspberry PI os Desktop 64-bit Kernel 5.15 - Debian 11). 

**Yocto Build Tools:**

**	**The prebuilt versions of the OS for supported platforms will be built using the - Honister - release of Yocto.

**	**While the OS will come pre-built for all the supported platforms, all unsupported platforms will be attempted through the release of a Pocky Build Guide. 

**Tested ECU Software:**

**	**The AutoConnect project is known and tested to be compatible with the following ECU software.

The OS will have a built in version of TunerStudioMS and MegaLogViewMS preintstalled but software activate keys for full features will need to be purchased by the respective software distributors

	     Figure 1.5


<table>
  <tr>
   <td><strong>Tested ECU Software - Latest Releases</strong>
   </td>
  </tr>
  <tr>
   <td>TunerStudioMS Lite
   </td>
  </tr>
  <tr>
   <td>TunerStudioMS
   </td>
  </tr>
  <tr>
   <td>MegaLogViewer MS - Lite
   </td>
  </tr>
  <tr>
   <td>MegaLogViewer MS
   </td>
  </tr>
  <tr>
   <td>MegaLogViewerHD - Lite
   </td>
  </tr>
  <tr>
   <td>MegaLogViewerHD
   </td>
  </tr>
</table>


**Tested Audio Software:**

**	**The OS supports Android Auto and will be preinstalled.

