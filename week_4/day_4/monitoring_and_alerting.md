# Monitoring and Alerting

### How to set up automated alerts for your EC2 instances CPU Utilization.

1. Navigate to the Cloudwatch page:

![img.png](images/monitoring/image-b.png)

2. In the Alarms section, navigate to the All Alarms section:

![img.png](images/monitoring/image-a.png)

3. Click the Create Alarm button:

![img.png](images/monitoring/image.png)

4. Select Metric:

![img.png](images/monitoring/image-1.png)

5. Copy your instances ID:

![img.png](images/monitoring/image-2.png)

6. While in the Select Metric page, paste your copied ID into the search bar, in the Browse Tab:

![img.png](images/monitoring/image-3.png)

7. Select the EC2 area:

![img.png](images/monitoring/image-4.png)

8. Per-Instance Metrics:

![img.png](images/monitoring/image-5.png)

9. This should lead you to a page that contains monitoring techniques specific to your EC2. Select the CPU Utilization Id:

![img.png](images/monitoring/image-6.png)

10. Press Select Metric.
11. Specific the conditions:
    1.  Do not change the name.
    2.  Give it an appropriate Period (i.e., 1 minute)
    3.  Choose your % in the `than` box in the conditions section.

![img.png](images/monitoring/image-7.png)

12. Specify where the alarm email will be sent to.
    1.  May have to be configured.

![img.png](images/monitoring/image-8.png)

13. Give it an appropriate name:

![img.png](images/monitoring/image-9.png)

14. If all metrics and configurations look correct, create the alarm.

15. The alarm will start with insufficent data, but will begin to fill in over time.

16. Push your CPU utilization to check if the alarm works.
    1.  This means give your instance multiple commands to push the cpu workload.

![img.png](images/monitoring/image-10.png)

17. Do this multiple times in quick succession to push up the workload.

18. Watch as the CPU utilization begins to rise. This may take a minute.

![img.png](images/monitoring/image-11.png)

19. As the CPU utilization breaches 20%, the alarm is triggered:

![img.png](images/monitoring/image-12.png)

20. You will have received an email:

![img.png](images/monitoring/image-13.png)