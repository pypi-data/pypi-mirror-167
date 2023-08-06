Description of the project
--------------------------

pyStressTest
============

pyStressTest is a simple module for stress testing web resources.

::

   from stress_test import StressTest
   from monitor import ChartMonitor

   stress = StressTest('http://127.0.0.1:8000')
   stress.timeout = 0.5
   stress.max_execution_time = 10
   stress.max_thread_count = 100
   monitor = ChartMonitor(stress)
   monitor.start()
   monitor.build_graph()

pyStressTest allows you to easily test your web resources with just a
few lines of code. The project works with the help of threads, you can
set their maximum number

::

   stress.max_thread_count = 100

otherwise, they will be constantly created.

You can specify timeout, this variable affects the speed of sending
requests and the speed of creating threads.

::

   stress.timeout = 0.5

You can specify a maximum resource testing time.

::

   stress.max_execution_time = 10

pyStressTest can automatically display test statistics, for this you can
use two classes:
1) CMDMonitor - statistics will be displayed in the
terminal;
2) ChartMonitor - statistics will be displayed as two graphs
(using matplotlib).

You can read more in the class documentation.

pyStressTest, if the response code from the resource is != 200, it will
consider this an error and display a message about this in the terminal
and display it in the statistics.
