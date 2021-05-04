# BAE305 Final Project - Autonomous Safety System: Determining Various Limitations of lidar Sensors
Lindsey Campbell, John Mann, Samantha Schultz, Ben Shacklett

## Summary
With an increasing popularity in autonomous machines (cars, drones, lawnmowers, vacuums, etc. …), it is crucial for us as engineers to understand how the safety systems of this technology work. Sensors act as the eyes and ears for the machines, so knowing the limitations and primary functions of the most common sensors has a lot of utility when designing such systems.

We set out to test the limitations and accuracy of a lidar sensor. As a simplified explanation: the lidar spins constantly, emitting a laser (invisible to the human eye) which is reflected off surfaces and received by a light-sensitive portion of the sensor. Depending on coding, a map will be generated of the room, consisting of small dots that represent the different points that were received. In our code, there were 360 data points collected with each rotation, one for each degree. Thus, there were 360 points displayed, each with a distance assigned to it for each rotation of the sensor.

We tested the sensor in varying conditions (low light, bright light, mist) and with varying target materials (dummy standard for autonomous vehicle safety systems: heavy plastic, aluminum foil, a mirror). All different target materials were tested in bright light conditions. The sensor had extremely accurate readings for all variances, typically within .03 meters of the true distance, with spotty exceptions for the aluminum foil and mirror. The foil had an error of more than .03 meters at times, while the mirror had errors roughly 2 times the true distance.

Overall, the system was accurate, never indicating a clear danger zone when there was something within 1.5 meters. Exceptions to the accuracy were erratic at best, and uncommon. A lidar sensor will perform well as long as the targets aren’t extremely reflective and are level with the laser.

## Design
### Materials:
- RaspberryPi
  - Model: RaspberryPi4
- Computer monitor 
- Lidar device driver
- Lidar
  - Model: RPLIDAR A1M8
- Keyboard and Mouse
- Cables/wires
- Trolley

### Setting Up the RaspberryPi:
Plug the RaspberryPi into power and connect it to the monitor, mouse and keyboard using an HDMI cable and USB cables respectively. Once the RaspberryPi is booted up, let it check for any updates it may need and install those accordingly. Once the RaspberryPi is up to date, open the IDLE programming tool on the Pi. The code provided can be copied and pasted or manually typed to change how or what the lidar will output. At this stage, the lidar device driver can be plugged into the RaspberryPi using the micro USB cable. Once the driver is plugged in, the power light should be displayed on the driver. From here, the lidar’s ribbon connection can be used to connect the lidar to its driver. Once the lidar is connected, it will automatically start running. However, no data will be gathered or output until a program is run on the RaspberryPi. From here, all connection in the wiring schematic should be complete. The program which was either typed or pasted into the IDLE on the RaspberryPi can now be run and the lidar will gather the desired data and output it to the monitor. The final construction is seen below:
<img src="https://github.com/sschultz858/BAE305---Final-Project/blob/65f1dc3365f63e79cacdeb90b3f4db1a5a9544e7/BAE305_ProjectCircuitDrawing.png" width="1200">


### Assembling Test Dummy/Target:
During the assembly process of the test dummy there are some important things to note. This test was designed to model an adult human in a seated position. For this specific test a human sized/shaped test dummy was used.

<img src="https://github.com/sschultz858/BAE305---Final-Project/blob/65f1dc3365f63e79cacdeb90b3f4db1a5a9544e7/TestDummyPic.jpg" width="300">

It was necessary to use a trolley when conducting the experiment with the test dummy (filled with water) because having it on a platform with wheels increased ease of movement significantly.

For any other desired tests personal design and research must be conducted. Some measurements to note for assembly of the test dummy: an average human torso length is approximately 19", the average height and width of a human head is approximately 8.5” and 6.5” respectively. Many materials can work to model the torso and head. It was found that the construction seen in the image above could be used to fit the criteria for these measurements. Once the desired size and shape of the test dummy is completed, different testing scenarios can be designed to recorded how the sensor reacts. For this example, scenarios such as bright light, dim light, light rain, slightly reflective clothing , and super reflective clothing were tested. Daylight and night can be tested using either outdoor conditions or indoor conditions - by turning lights on or off.

<insert time lapse video here>

Light rain is recommended to be tested indoors in a controlled environment since the equipment is not weather resistant. Light rain can be resembled by misting water droplets into the path of the laser from the lidar.

<img src="https://github.com/sschultz858/BAE305---Final-Project/blob/65f1dc3365f63e79cacdeb90b3f4db1a5a9544e7/MisterPic.jpg" width="300">

For the slightly reflective and super reflective clothing tests, items like aluminum foil and mirrors can be placed on the side of the test dummy which is facing the Lidar. Seen below are the individual target materials (aluminum foil and mirror respectively), not as they were oriented during the experiment.

<img src="https://github.com/sschultz858/BAE305---Final-Project/blob/65f1dc3365f63e79cacdeb90b3f4db1a5a9544e7/AluminumPic.jpg" width="300">

<img src="https://github.com/sschultz858/BAE305---Final-Project/blob/65f1dc3365f63e79cacdeb90b3f4db1a5a9544e7/MirrorPic.jpg" width="300">

Throughout these tests the data from the lidar can be monitored and recorded to show how the lidar reacted to the testing scenarios.

## Testing Procedures
1. Connect RaspberryPi, lidar sensor, keyboard, mouse, and monitor.
   - We did connected our RaspberryPi to the HDMI supported display screen, keyboard, mouse, and sensor.
2. Set up the physical testing site.
   - Using a tape measure, we measured three meters away from the wall and placed a 1 foot tall bucket at that distance. The Lidar sensor was placed on the bucket with the front of the sensor lying flush with the edge of the bucket, with the programmed origin perpendicular to the wall. Then using duct tape we placed a piece of tape on the floor from the front of the bucket to the previously measured portion of the wall. Again, using the tape measure and a marker, we marked the duct tape at significant values: 0.50m, 1.00m, 1.50m, 2.00m, and 2.50m with reference to the sensor.
3. Run a control.
   - A control test was conducted to test the accuracy of the sensor. The test dummy was rolled to each significant distance (2.50, 2.00, 1.50, 1.00, .50); the edge of the barrel was overtopping the measurement line. The code was run with 3 trials conducted and no movement of the target between each trial. The minimum calculated distance for a given angle was recorded, and for the following 2 trials, the same angle was used as the reference for our data. For example, if angle 358 (within our range of 350-10) displayed the lowest value of 2.012m, the distance associated with angle 358 would be recorded in the next two trials, even if a different angle had a shorter distance associated. Next, we tested the threshold of the danger distance set in our code where the program would print "stop". We began with the dummy against the wall, rolling it slowly forward until "stop" was displayed.
4. Run trials for each condition and record data.
   - The test dummy was positioned first at the 2 meter mark followed by the 1 meter mark. To decide which distance should be recorded, the method used in our control was replicated for each condition and distance. Distance values and danger detection output were recorded. The same procedure was carried out for each condition in the following order: test dummy in bright light, aluminum foil, test dummy in dim light (turned off all lights in the room with only the light from the projector present), mirror, test dummy with mist.
       - A note about the mirror: the mirror was on a hinge in the center. For testing, it was closely approximated to be perpendicular to the path of the laser.

## Design Decision Discussion
In our project, there were several variables that we chose in order to better achieve our goal or to make processes easier.

One major way that our hardware was limited was the available stock. A group from a previous semester began a project similar to ours, so the funding and equipment was provided. We were limited to using the model of sensor and RaspberryPi bought. We were also extremely limited with our time and environmental resources. The only area we could accurately predict environmental conditions was inside a somewhat small classroom (~24x24ft). Our lighting and testing range (distance and angle) were the conditions that were affected most. Access to the materials tested was heavily influenced by availability; all of our varying materials were common household items. In our code, the classroom environment demanded that we make our ranges for both distance and angle somewhat small. In our testing, because our danger distance was set to 1.5m, we wanted to record values 1 distance inside and 1 distance outside this range. Because of that, we chose 1m and 2m.

With more funding and time, one could perform similar tests with a significantly more powerful sensor, increased amount of target materials and sizes, more environmental conditions (even testing outside with varying weather patterns and other factors), wider range of both distance and angle, and more distances tested.

## Test Results
### Control Results:
<img src="https://github.com/sschultz858/BAE305---Final-Project/blob/13f11f98bd06236f380d4a06056bf0b8c7d7de44/Control%20Test%20Results.png" width="900">

### Test Conditions:
<img src="https://github.com/sschultz858/BAE305---Final-Project/blob/13f11f98bd06236f380d4a06056bf0b8c7d7de44/Figure%202%20Conditions.png" width="900">

### Results:
<img src="https://github.com/sschultz858/BAE305---Final-Project/blob/13f11f98bd06236f380d4a06056bf0b8c7d7de44/Test%20Results.png" width="900">

## Results Discussion
### Control:
This preliminary test was intended to establish whether a baseline systematic error in the lidar distance readings was present. At 0.50m and 2.00m we see the expected outcome, the lidar reads precisely the same distance each time. At 1.00m, 1.50m, and 2.50m we see an approximate error of 0.002m, 0.003m, and 0.005m, respectively. The target and lidar were completely stationary, and we chose to record distances at the same angle each time to ensure consistency. Therefore, the error suggests there is some deviation inherent to our lidar sensor.

However, because the error is merely in the millimeter range, we determined the inconsistency is small enough to ensure no real-world consequences. The purpose of this project was to determine the limitations of lidar sensors as they apply to autonomous vehicles. If a safety system utilizing a lidar sensor were programmed to stop a car 1.5m away for example, a readings fluctuation of a few millimeters wouldn’t cause the system to fail. The “stop” sequence in the vehicle would begin within a few millimeters of the true distance.

To improve our control data, we would analyze a much larger sample size. A sample of at least 30 distance readings would be ideal to discuss standard deviation more accurately in the lidar readings. However, three trials were enough to establish the baseline understand that our lidar does not return the same distance every time.

### Test Results:
The purpose of this test was to compare the lidar distance readings and function under a variety of environmental conditions. The goal was to find limitations on lidar sensors to keep in mind for design and engineering of autonomous vehicles. Our goal accomplished by testing 5 conditions as described in Table 1 (see **Test Results** above). The control/baseline setup was bright light with the plastic target. Each of the other 4 conditions involved one change to the basic setup either changing the target or the environmental conditions.

The “danger distance” was set to 1.50m, so each condition was tested at 1.00m and 2.00m to ensure the code printed “clear” and “stop” beyond and within the danger distance, respectively. Figure 2 shows the results that the code always printed stop when needed. Additionally, we rolled the target across the 1.50m mark while running the lidar and code real-time. The system was able to sensitively detect when the object came within 1.50m and printed “stop” in real time. This pertains to the real-world application of lidar sensors in autonomous vehicles. Safety systems need to send commands as soon as the threat is detected.

We expected to see the lidar system malfunction in the presence of mist. Because lidar sensors work by emitting laser lights and calculating time for the light to return, obstructions or erroneous detections can cause the system to malfunction and even fail. In the autonomous vehicle industry, a challenge is designing the best lidar system for inclement weather, including heavy precipitation. The sensors could detect large raindrops instead of the intended target. Our lidar system returned distances consistent with the error established in the control trial of only 0.002m, and the mist caused no strange behavior in the system.

The shiny target caused strange behavior in the system. For example, at the 2.00m testing mark, angle 359 had inconsistent readings not explained by systematic error. The code printed 2.157m then 2.039m, a change of 0.118m without the target ever moving. This strange pattern happened for several iterations. Therefore we conclude some shiny surfaces may cause a malfunction in lidar sensor systems.

The mirror caused substantial malfunctions in the lidar system. Although the distance readings in the Test Results table (see **Test Results** above) seem consistent, they do not provide the full picture. At the 2.00m mark, the sensor returned 4.00m several times. The vast majority of readings were accurate, but roughly once per iteration of code we’d see a distance double the true distance. We tried angling the mirror, and the distance readings seemed to fluctuate depending on where the mirror was reflecting. This “seeing double” phenomenon may have been explained by the mirror reflecting the laser right back effectively doubling the distance. Because highly reflective objects can bounce the lasers around creating "noise" in the lidar, we expected to see problems with this condition.

In hindsight, results would have been much more comprehensive with a large sample size. The patterns described were observable from several iterations of code and hundreds of distance readings, but not all intricacies were observable in our 3-trial results table. Providing a sample of 30+ distances for each condition would have allowed a more detailed comparison between standard deviations in data and a more illustrative understanding of the limitations of the sensor.

Our results have a few implications for the use of lidar sensor systems in autonomous vehicles. For one, lidar function is not dependent on bright or dark surrounding light, so these systems should not falter from day to night. Light mist did not affect the lidar function, but larger particles or water droplets could catch the sensor’s attention reading faulty distances. Shiny and highly reflective surfaces were the biggest obstacle we found. Strange reflections bounce the laser lights around unpredictably causing system malfunction because distances are calculated based on time for the light to return.


