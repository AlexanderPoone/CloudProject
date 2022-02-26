# Cloud Computing Project
**DRAFT**

There are quite a few works that tackle real-time computer vision computations on the cloud, like object detection, semantic segmentation and collision avoidance. However, some critical issues are often neglected. For example, the paper by Liu and Boehm does not address the issue of fairness. A bad scenario would be, the live vehicle counts of some CCTVs are not updating because they do not get the fair share. The other extreme would be a deadlock, the master keeps waiting for some CCTV to respond. Scalability would be another issue. As the system network keeps expanding, some suboptimal cloud systems need a lot of hardwiring or manual configuration.

Thus, we are building an alternative system that is lightweight and scalable. In a nutshell, the user can add or remove URLs of CCTV live streams (*.m3u8) to the application. Once such URL is added, a new EC2 instance will be created to do object detection. Then the real-time vehicle count will be collected and visualized. Instead of the sequential pipeline like the Liu/Boehm paper, we will use the pub/sub model to communicate between EC2 instances.

Each CCTV subscribes to the master. If CCTV is removed, then the EC2 instance will be terminated, it unsubscribes from the pub/sub model
Real case: new CCTV installed, you add it; CCTV under maintenance, you disconnect it. Or for energy-conserving purpose the operation hours are limited, you disconnect it.
